import tkinter as tk
import threading
import time
from hvac_sim import HVACSystem

class LEDIndicator(tk.Canvas):
    def __init__(self, parent, size=15, color_on='#22ff22', color_off='#444444', **kwargs):
        super().__init__(parent, width=size, height=size, bd=0, highlightthickness=0, **kwargs)
        self.size = size
        self.color_on = color_on
        self.color_off = color_off
        self.state = False
        self._draw()
    
    def _draw(self):
        self.delete('all')
        color = self.color_on if self.state else self.color_off
        # Draw main circle
        self.create_oval(2, 2, self.size-2, self.size-2, fill=color, outline='#222222')
        if self.state:
            # Add highlight for "on" state
            self.create_oval(4, 4, self.size-4, self.size-4, fill='', outline='#ffffff', width=1)
    
    def set_state(self, state):
        self.state = bool(state)
        self._draw()

class HVACScadaGUI:
    def __init__(self, root, system: HVACSystem):
        self.root = root
        self.system = system
        self.vars = {k: tk.StringVar() for k in [
            'system_status','mode','MAT','SAT','AF_SF','AF_RF',
            'Z1T','Z2T','Z3T','CO2_1','CO2_2','CO2_3',
            'VAV1A','VAV2A','VAV3A','SF_Cool','SF_Heat','RF','CC_A','HC_A','alarm',
            'amb_temp','setpoint','fan_rpm','coil_temp']}
        self._build_gui()
        self._running = False

    def _set_status_color(self, var, label_widget, on_value, off_value):
        # Helper to set color based on value
        value = var.get()
        if value == on_value:
            label_widget.config(fg='green')
        elif value == off_value:
            label_widget.config(fg='red')
        else:
            label_widget.config(fg='black')

    def _build_gui(self):
        # Color scheme
        colors = {
            'bg_dark': '#1e1e2f',           # Dark blue-gray background
            'bg_darker': '#27293d',         # Darker panel background
            'text_light': '#e9ecef',        # Light text
            'text_dim': '#8f9ba6',          # Dimmed text
            'accent_blue': '#4f7b9f',       # Pastel blue
            'accent_green': '#68b784',      # Pastel green
            'accent_orange': '#e6935c',     # Pastel orange
            'accent_red': '#e85f5c',        # Pastel red
            'accent_yellow': '#e8c15c',     # Pastel yellow
            'accent_purple': '#b784a7',     # Pastel purple
            'accent_cyan': '#5cbbe8',       # Pastel cyan
        }

        self.root.title("HVAC System - Compact SCADA HMI")
        self.root.configure(bg=colors['bg_dark'])

        # --- HEADER ---
        header = tk.Frame(self.root, bg=colors['bg_darker'], bd=2, relief='groove')
        header.grid(row=0, column=0, columnspan=2, sticky='ew', padx=2, pady=2)
        
        self.status_label = tk.Label(header, text="SYSTEM STOPPED", font=("Arial", 18, "bold"), 
                                   fg=colors['accent_blue'], bg=colors['bg_darker'])
        self.status_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        
        # Control buttons with updated colors
        self.start_btn = tk.Button(header, text="START", width=8, command=self.start_system,
                                 font=("Arial", 11, "bold"), bg=colors['accent_green'], 
                                 fg=colors['text_light'], activebackground=colors['bg_darker'])
        self.start_btn.grid(row=0, column=1, padx=5)
        
        self.stop_btn = tk.Button(header, text="STOP", width=8, command=self.stop_system,
                                font=("Arial", 11, "bold"), bg=colors['bg_darker'], 
                                fg=colors['text_light'], activebackground=colors['bg_dark'])
        self.stop_btn.grid(row=0, column=2, padx=5)
        
        self.emergency_btn = tk.Button(header, text="E-STOP", width=8, command=self.emergency_stop,
                                     font=("Arial", 11, "bold"), bg=colors['accent_red'], 
                                     fg=colors['text_light'], activebackground=colors['bg_darker'])
        self.emergency_btn.grid(row=0, column=3, padx=5)

        # --- TOP SUMMARY ---
        summary = tk.Frame(self.root, bg=colors['bg_darker'], bd=2, relief='groove')
        summary.grid(row=1, column=0, columnspan=2, sticky='ew', padx=2, pady=2)
        
        summary_labels = [
            ("Mode", self.vars['mode'], colors['accent_green']),
            ("MAT", self.vars['MAT'], colors['accent_cyan']),
            ("SAT", self.vars['SAT'], colors['accent_cyan']),
            ("Fan RPM", self.vars['fan_rpm'], colors['accent_purple']),
            ("Coil Temp", self.vars['coil_temp'], colors['accent_orange']),
        ]
        
        for i, (lbl, var, color) in enumerate(summary_labels):
            tk.Label(summary, text=lbl, font=("Arial", 10, "bold"), 
                    bg=colors['bg_darker'], fg=colors['text_light']).grid(row=0, column=i*2, padx=5, sticky='e')
            tk.Label(summary, textvariable=var, font=("Arial", 10, "bold"), 
                    fg=color, bg=colors['bg_darker']).grid(row=0, column=i*2+1, padx=5, sticky='w')

        # --- MAIN BODY ---
        body = tk.Frame(self.root, bg=colors['bg_dark'])
        body.grid(row=2, column=0, sticky='nsew', padx=2, pady=2)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Left panel
        left = tk.Frame(body, bg=colors['bg_dark'])
        left.grid(row=0, column=0, sticky='nsw', padx=2, pady=2)

        # Components section
        comp = tk.LabelFrame(left, text="Components", font=("Arial", 11, "bold"), 
                           bg=colors['bg_darker'], fg=colors['text_light'])
        comp.grid(row=0, column=0, sticky='ew', padx=2, pady=2)

        # Zones
        tk.Label(comp, text="- Zones", font=("Arial", 10, "bold"), 
                bg=colors['bg_darker'], fg=colors['text_light']).grid(row=0, column=0, sticky='w')
        
        for i in range(3):
            tk.Label(comp, text=f"   Zone {i+1} Temp", font=("Arial", 10), 
                    bg=colors['bg_darker'], fg=colors['text_dim']).grid(row=i+1, column=0, sticky='w')
            tk.Label(comp, textvariable=self.vars[f'Z{i+1}T'], font=("Arial", 10, "bold"), 
                    bg=colors['bg_darker'], fg=colors['accent_orange']).grid(row=i+1, column=1, sticky='w')
            tk.Label(comp, text=f"   Zone {i+1} CO₂", font=("Arial", 10), 
                    bg=colors['bg_darker'], fg=colors['text_dim']).grid(row=i+1, column=2, sticky='w')
            tk.Label(comp, textvariable=self.vars[f'CO2_{i+1}'], font=("Arial", 10, "bold"), 
                    bg=colors['bg_darker'], fg=colors['accent_yellow']).grid(row=i+1, column=3, sticky='w')

        # Actuators
        tk.Label(comp, text="- Actuators", font=("Arial", 10, "bold"), 
                bg=colors['bg_darker'], fg=colors['text_light']).grid(row=5, column=0, sticky='w')
        
        actuators = [
            ("Supply Fan (Cooling)", 'SF_Cool', '#5cbbe8'),  # cyan
            ("Supply Fan (Heating)", 'SF_Heat', '#e6935c'),  # orange
            ("Return Fan", 'RF', '#4f7b9f'),                 # blue
            ("Cooling Coil Valve", 'CC_A', '#5cbbe8'),       # cyan
            ("Heating Coil Valve", 'HC_A', '#e85f5c'),       # red
            ("Alarm", 'alarm', '#ff4444'),                   # bright red
        ]
        
        self.led_indicators = {}
        for i, (label, varname, color) in enumerate(actuators):
            tk.Label(comp, text=f"   {label}", font=("Arial", 10), 
                    bg=colors['bg_darker'], fg=colors['text_dim']).grid(row=6+i, column=0, sticky='w')
            
            led = LEDIndicator(comp, size=15, color_on=color, bg=colors['bg_darker'])
            led.grid(row=6+i, column=1, sticky='w', padx=5)
            self.led_indicators[varname] = led
            
            tk.Label(comp, textvariable=self.vars[varname], font=("Arial", 10, "bold"), 
                    bg=colors['bg_darker'], fg=color).grid(row=6+i, column=2, sticky='w')

        # Setpoints section
        setp = tk.LabelFrame(left, text="Setpoint & Ambience", font=("Arial", 11, "bold"), 
                           bg=colors['bg_darker'], fg=colors['text_light'])
        setp.grid(row=1, column=0, sticky='ew', padx=2, pady=2)
        
        tk.Label(setp, text="Ambience Temp (°C):", font=("Arial", 10), 
                bg=colors['bg_darker'], fg=colors['text_dim']).grid(row=0, column=0, sticky='e')
        amb_entry = tk.Entry(setp, textvariable=self.vars['amb_temp'], width=6, 
                           font=("Arial", 10, "bold"), bg=colors['bg_dark'], 
                           fg=colors['text_light'], insertbackground=colors['text_light'])
        amb_entry.grid(row=0, column=1, sticky='w')
        amb_entry.bind('<KeyRelease>', lambda e: self._realtime_amb_update())

        tk.Label(setp, text="Zone Setpoint (°C):", font=("Arial", 10), 
                bg=colors['bg_darker'], fg=colors['text_dim']).grid(row=1, column=0, sticky='e')
        set_entry = tk.Entry(setp, textvariable=self.vars['setpoint'], width=6, 
                           font=("Arial", 10, "bold"), bg=colors['bg_dark'], 
                           fg=colors['text_light'], insertbackground=colors['text_light'])
        set_entry.grid(row=1, column=1, sticky='w')
        set_entry.bind('<KeyRelease>', lambda e: self._realtime_setpoint_update())

        tk.Button(setp, text="Apply", width=10, command=self.apply_setpoints, 
                 font=("Arial", 10, "bold"), bg=colors['accent_blue'], 
                 fg=colors['text_light'], activebackground=colors['bg_darker']).grid(row=0, column=2, rowspan=2, padx=10)

        # System Alarms section
        alarms = tk.LabelFrame(left, text="System Alarms", font=("Arial", 11, "bold"), 
                             bg=colors['bg_darker'], fg=colors['text_light'])
        alarms.grid(row=2, column=0, sticky='ew', padx=2, pady=2)
        
        alarm_list = [
            "Emergency Stop", "Low Temp", "High Temp", "CO2 High", "Fan Fault", "General Alarm"
        ]
        
        for i, alarm in enumerate(alarm_list):
            tk.Checkbutton(alarms, text=alarm, font=("Arial", 10), 
                         bg=colors['bg_darker'], fg=colors['text_dim'], 
                         selectcolor=colors['bg_dark'], state='disabled').grid(row=i, column=0, sticky='w')
        
        tk.Label(alarms, text="Active: None", font=("Arial", 10, "italic"), 
                fg=colors['accent_green'], bg=colors['bg_darker']).grid(row=len(alarm_list), column=0, sticky='w')

        # Process Diagram
        diagram = tk.LabelFrame(body, text="Process Diagram", font=("Arial", 11, "bold"), 
                              bg=colors['bg_darker'], fg=colors['text_light'])
        diagram.grid(row=0, column=1, sticky='nsew', padx=2, pady=2)        # Load and display HVAC diagram
        img = tk.PhotoImage(file="HVAC.png")
        img_label = tk.Label(diagram, image=img, bg=colors['bg_darker'])
        img_label.image = img  # Keep a reference to prevent garbage collection
        img_label.pack(expand=True, fill='both', padx=20, pady=20)

        # Trends section
        trends = tk.LabelFrame(self.root, text="Real-Time Trends", font=("Arial", 11, "bold"), 
                             bg=colors['bg_darker'], fg=colors['accent_cyan'])
        trends.grid(row=3, column=0, columnspan=2, sticky='ew', padx=2, pady=2)
        tk.Label(trends, text="[Trend Graphs Placeholder]", font=("Arial", 12, "italic"), 
                bg=colors['bg_darker'], fg=colors['text_dim']).pack(expand=True, fill='both', padx=20, pady=20)

        # Demo Controls
        demo = tk.Frame(self.root, bg=colors['bg_dark'])
        demo.grid(row=4, column=0, columnspan=2, sticky='ew', padx=2, pady=2)
        tk.Label(demo, text="Demo Controls:", font=("Arial", 10, "bold"), 
                bg=colors['bg_dark'], fg=colors['text_light']).pack(side='left', padx=5)
        
        btns = [
            ("Normal Operation", colors['accent_green']),
            ("Pressure Variations", colors['accent_blue']),
            ("Temp Setpoint Changes", colors['accent_purple']),
            ("Mixed Scenario", colors['accent_yellow']),
            ("Stop Demo", colors['accent_red']),
        ]
        
        for txt, color in btns:
            tk.Button(demo, text=txt, font=("Arial", 10, "bold"), bg=color, 
                     fg=colors['bg_dark'], width=16, state='disabled').pack(side='left', padx=2)

    def apply_setpoints(self):
        try:
            amb = float(self.vars['amb_temp'].get())
            self.system.amb_temp = amb
            sp = float(self.vars['setpoint'].get())
            self.system.temp_setpoint = sp
        except Exception:
            pass

    def update(self):
        s = self.system.status()
        self.vars['system_status'].set(s['system_status'])
        self.vars['mode'].set(s['mode'].title())
        self.vars['MAT'].set(f"{s['MAT']:.1f} °C")
        self.vars['SAT'].set(f"{s['SAT']:.1f} °C")
        self.vars['AF_SF'].set(f"{s['AF_SF']:.2f}")
        self.vars['AF_RF'].set(f"{s['AF_RF']:.2f}")
        self.vars['fan_rpm'].set(f"{s['fan_rpm']:.0f} RPM")
        self.vars['coil_temp'].set(f"{s['coil_temp']:.1f} °C")
        for i in range(3):
            self.vars[f'Z{i+1}T'].set(f"{s['ZoneTemps'][i]:.1f} °C")
            self.vars[f'CO2_{i+1}'].set(f"{int(s['CO2'][i])} ppm")
            self.vars[f'VAV{i+1}A'].set(f"{s['VAV'][i]:.2f}")
        self.vars['SF_Cool'].set('ON' if s['SF_Cool'] else 'OFF')
        self.vars['SF_Heat'].set('ON' if s['SF_Heat'] else 'OFF')
        self.vars['RF'].set('ON' if s['RF'] else 'OFF')
        self.vars['CC_A'].set('OPEN' if s['CC_A'] else 'CLOSED')
        self.vars['HC_A'].set('OPEN' if s['HC_A'] else 'CLOSED')
        self.vars['alarm'].set('YES' if s['alarm'] else 'NO')
        self.vars['amb_temp'].set(f"{getattr(self.system, 'amb_temp', 28.0):.1f}")
        self.vars['setpoint'].set(f"{self.system.temp_setpoint:.1f}")
        
        # Update LED indicators
        self.led_indicators['SF_Cool'].set_state(s['SF_Cool'])
        self.led_indicators['SF_Heat'].set_state(s['SF_Heat'])
        self.led_indicators['RF'].set_state(s['RF'])
        self.led_indicators['CC_A'].set_state(s['CC_A'])
        self.led_indicators['HC_A'].set_state(s['HC_A'])
        self.led_indicators['alarm'].set_state(s['alarm'])
        
        self.root.update()

    def start_system(self):
        self.system.start()
        if not self._running:
            self._running = True
            threading.Thread(target=self._run_loop, daemon=True).start()

    def stop_system(self):
        self.system.stop()
        self._running = False
        # Reset all HMI display variables to initial values
        self.vars['system_status'].set('OFF')
        self.vars['mode'].set('Cooling')
        self.vars['MAT'].set('24.0 °C')
        self.vars['SAT'].set('18.0 °C')
        self.vars['AF_SF'].set('1.00')
        self.vars['AF_RF'].set('1.00')
        self.vars['fan_rpm'].set('1200 RPM')
        self.vars['coil_temp'].set('7.0 °C')
        for i in range(3):
            self.vars[f'Z{i+1}T'].set('24.0 °C')
            self.vars[f'CO2_{i+1}'].set('500 ppm')
            self.vars[f'VAV{i+1}A'].set('0.50')
        self.vars['SF_Cool'].set('OFF')
        self.vars['SF_Heat'].set('OFF')
        self.vars['RF'].set('OFF')
        self.vars['CC_A'].set('CLOSED')
        self.vars['HC_A'].set('CLOSED')
        self.vars['alarm'].set('NO')
        self.vars['amb_temp'].set('28.0')
        self.vars['setpoint'].set('22.0')
        self.root.update()

    def emergency_stop(self):
        self.system.stop()
        self._running = False
        for var in self.vars.values():
            var.set('EMERGENCY')
        self.vars['alarm'].set('YES')
        self.root.update()
        self.start_btn.config(state='disabled')
        self.emergency_btn.config(text='Reset', command=self.reset_emergency, bg='orange')

    def reset_emergency(self):
        self.system.alarm = False
        self.system.running = False
        self.update()
        self.start_btn.config(state='normal')
        self.emergency_btn.config(text='Emergency', command=self.emergency_stop, bg='red')
        self.vars['alarm'].set('NO')
        self.root.update()

    def _run_loop(self):
        while self._running and self.system.running:
            self.system.step()
            self.update()
            time.sleep(0.5)

    def _realtime_setpoint_update(self):
        try:
            sp = float(self.vars['setpoint'].get())
            self.system.temp_setpoint = sp
        except Exception:
            pass

    def _realtime_amb_update(self):
        try:
            amb = float(self.vars['amb_temp'].get())
            self.system.amb_temp = amb
        except Exception:
            pass

if __name__ == "__main__":
    from hvac_sim import HVACSystem
    root = tk.Tk()
    system = HVACSystem()
    gui = HVACScadaGUI(root, system)
    gui.update()
    root.mainloop()
