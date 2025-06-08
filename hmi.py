import tkinter as tk
import threading
import time
from hvac_sim import HVACSystem

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

    def _build_gui(self):
        self.root.title("HVAC System SCADA HMI Simulation")
        frame_status = tk.LabelFrame(self.root, text="System Status", padx=10, pady=5, font=("Arial", 11, "bold"))
        frame_status.grid(row=0, column=0, padx=10, pady=5, sticky='ew')
        frame_zones = tk.LabelFrame(self.root, text="Zones", padx=10, pady=5, font=("Arial", 11, "bold"))
        frame_zones.grid(row=1, column=0, padx=10, pady=5, sticky='ew')
        frame_act = tk.LabelFrame(self.root, text="Actuators", padx=10, pady=5, font=("Arial", 11, "bold"))
        frame_act.grid(row=2, column=0, padx=10, pady=5, sticky='ew')
        frame_ctrl = tk.LabelFrame(self.root, text="Controls", padx=10, pady=5, font=("Arial", 11, "bold"))
        frame_ctrl.grid(row=3, column=0, padx=10, pady=10, sticky='ew')
        frame_set = tk.LabelFrame(self.root, text="Setpoint & Ambience", padx=10, pady=5, font=("Arial", 11, "bold"))
        frame_set.grid(row=4, column=0, padx=10, pady=5, sticky='ew')
        # Status
        tk.Label(frame_status, text="System Status:", font=("Arial", 11)).grid(row=0, column=0, sticky='e')
        tk.Label(frame_status, textvariable=self.vars['system_status'], font=("Arial", 11, "bold")).grid(row=0, column=1, sticky='w')
        tk.Label(frame_status, text="Mode:", font=("Arial", 11)).grid(row=1, column=0, sticky='e')
        tk.Label(frame_status, textvariable=self.vars['mode'], font=("Arial", 11)).grid(row=1, column=1, sticky='w')
        tk.Label(frame_status, text="MAT:", font=("Arial", 11)).grid(row=2, column=0, sticky='e')
        tk.Label(frame_status, textvariable=self.vars['MAT'], font=("Arial", 11)).grid(row=2, column=1, sticky='w')
        tk.Label(frame_status, text="SAT:", font=("Arial", 11)).grid(row=3, column=0, sticky='e')
        tk.Label(frame_status, textvariable=self.vars['SAT'], font=("Arial", 11)).grid(row=3, column=1, sticky='w')
        tk.Label(frame_status, text="AF_SF:", font=("Arial", 11)).grid(row=4, column=0, sticky='e')
        tk.Label(frame_status, textvariable=self.vars['AF_SF'], font=("Arial", 11)).grid(row=4, column=1, sticky='w')
        tk.Label(frame_status, text="AF_RF:", font=("Arial", 11)).grid(row=5, column=0, sticky='e')
        tk.Label(frame_status, textvariable=self.vars['AF_RF'], font=("Arial", 11)).grid(row=5, column=1, sticky='w')
        tk.Label(frame_status, text="Fan RPM:", font=("Arial", 11)).grid(row=6, column=0, sticky='e')
        tk.Label(frame_status, textvariable=self.vars['fan_rpm'], font=("Arial", 11)).grid(row=6, column=1, sticky='w')
        tk.Label(frame_status, text="Coil Output Temp:", font=("Arial", 11)).grid(row=7, column=0, sticky='e')
        tk.Label(frame_status, textvariable=self.vars['coil_temp'], font=("Arial", 11)).grid(row=7, column=1, sticky='w')
        # Zones
        for i in range(3):
            tk.Label(frame_zones, text=f"Zone {i+1} Temp:", font=("Arial", 11)).grid(row=i, column=0, sticky='e')
            tk.Label(frame_zones, textvariable=self.vars[f'Z{i+1}T'], font=("Arial", 11)).grid(row=i, column=1, sticky='w')
            tk.Label(frame_zones, text=f"Zone {i+1} CO₂:", font=("Arial", 11)).grid(row=i, column=2, sticky='e')
            tk.Label(frame_zones, textvariable=self.vars[f'CO2_{i+1}'], font=("Arial", 11)).grid(row=i, column=3, sticky='w')
            tk.Label(frame_zones, text=f"VAV {i+1} Pos:", font=("Arial", 11)).grid(row=i, column=4, sticky='e')
            tk.Label(frame_zones, textvariable=self.vars[f'VAV{i+1}A'], font=("Arial", 11)).grid(row=i, column=5, sticky='w')
        # Actuators
        tk.Label(frame_act, text="Supply Fan (Cooling):", font=("Arial", 11)).grid(row=0, column=0, sticky='e')
        tk.Label(frame_act, textvariable=self.vars['SF_Cool'], font=("Arial", 11)).grid(row=0, column=1, sticky='w')
        tk.Label(frame_act, text="Supply Fan (Heating):", font=("Arial", 11)).grid(row=1, column=0, sticky='e')
        tk.Label(frame_act, textvariable=self.vars['SF_Heat'], font=("Arial", 11)).grid(row=1, column=1, sticky='w')
        tk.Label(frame_act, text="Return Fan:", font=("Arial", 11)).grid(row=2, column=0, sticky='e')
        tk.Label(frame_act, textvariable=self.vars['RF'], font=("Arial", 11)).grid(row=2, column=1, sticky='w')
        tk.Label(frame_act, text="Cooling Coil Valve:", font=("Arial", 11)).grid(row=3, column=0, sticky='e')
        tk.Label(frame_act, textvariable=self.vars['CC_A'], font=("Arial", 11)).grid(row=3, column=1, sticky='w')
        tk.Label(frame_act, text="Heating Coil Valve:", font=("Arial", 11)).grid(row=4, column=0, sticky='e')
        tk.Label(frame_act, textvariable=self.vars['HC_A'], font=("Arial", 11)).grid(row=4, column=1, sticky='w')
        tk.Label(frame_act, text="Alarm:", font=("Arial", 11, "bold")).grid(row=5, column=0, sticky='e')
        tk.Label(frame_act, textvariable=self.vars['alarm'], font=("Arial", 11, "bold")).grid(row=5, column=1, sticky='w')
        # Controls
        self.start_btn = tk.Button(frame_ctrl, text="Start", width=10, command=self.start_system)
        self.start_btn.grid(row=0, column=0, padx=5)
        self.stop_btn = tk.Button(frame_ctrl, text="Stop", width=10, command=self.stop_system)
        self.stop_btn.grid(row=0, column=1, padx=5)
        self.quit_btn = tk.Button(frame_ctrl, text="Quit", width=10, command=self.root.quit)
        self.quit_btn.grid(row=0, column=2, padx=5)
        self.emergency_btn = tk.Button(frame_ctrl, text="Emergency", width=12, command=self.emergency_stop, bg='red', fg='white')
        self.emergency_btn.grid(row=0, column=3, padx=5)
        # Setpoints & Ambience
        tk.Label(frame_set, text="Ambience Temp (°C):", font=("Arial", 11)).grid(row=0, column=0, sticky='e')
        amb_entry = tk.Entry(frame_set, textvariable=self.vars['amb_temp'], width=6)
        amb_entry.grid(row=0, column=1, sticky='w')
        amb_entry.bind('<KeyRelease>', lambda e: self._realtime_amb_update())
        tk.Label(frame_set, text="Zone Setpoint (°C):", font=("Arial", 11)).grid(row=1, column=0, sticky='e')
        set_entry = tk.Entry(frame_set, textvariable=self.vars['setpoint'], width=6)
        set_entry.grid(row=1, column=1, sticky='w')
        set_entry.bind('<KeyRelease>', lambda e: self._realtime_setpoint_update())
        tk.Button(frame_set, text="Apply", width=10, command=self.apply_setpoints).grid(row=0, column=2, rowspan=2, padx=10)

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
