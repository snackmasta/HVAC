import random
import time

class HVACSystem:
    def __init__(self):
        # Sensors (AI)
        self.MAT = 24.0  # Mixed Air Temp
        self.SAT = 18.0  # Supply Air Temp
        self.AF_SF = 1.0 # Airflow Supply Fan
        self.AF_RF = 1.0 # Airflow Return Fan
        self.CO2 = [500, 500, 500]  # CO2 per zone
        self.ZT = [24.0, 24.0, 24.0]  # Zone Temps
        # Actuators (AO/DO)
        self.VAV = [0.5, 0.5, 0.5]  # VAV position (0-1)
        self.CC_A = 0  # Cooling Coil Valve
        self.HC_A = 0  # Heating Coil Valve
        self.SF_Cool = 0  # Supply Fan Cooling
        self.SF_Heat = 0  # Supply Fan Heating
        self.RF = 0  # Return Fan
        # Setpoints
        self.temp_setpoint = 22.0
        self.co2_setpoint = 800
        self.mode = 'cooling'
        self.running = False
        self.alarm = False
        self.amb_temp = 28.0  # Default ambient temperature
        self.fan_rpm = 1200  # Supply/Return Fan RPM
        self.coil_temp = 7.0  # Cooling Coil Output Temp (°C)
        self.system_status = 'OFF'

    def start(self):
        self.running = True
        self.alarm = False
        print("[START] HVAC system started.")

    def stop(self):
        self.running = False
        # Turn off all actuators and reset all process variables to initial state
        self.SF_Cool = 0
        self.SF_Heat = 0
        self.RF = 0
        self.CC_A = 0
        self.HC_A = 0
        self.fan_rpm = 1200
        self.coil_temp = 7.0
        self.VAV = [0.5, 0.5, 0.5]
        self.ZT = [24.0, 24.0, 24.0]
        self.CO2 = [500, 500, 500]
        self.MAT = 24.0
        self.SAT = 18.0
        self.AF_SF = 1.0
        self.AF_RF = 1.0
        self.amb_temp = 28.0
        self.temp_setpoint = 22.0
        self.mode = 'cooling'
        self.alarm = False
        self.system_status = 'OFF'
        print("[STOP] HVAC system stopped and reset. All fans, coils, VAVs, and process variables reset.")

    def step(self):
        if not self.running:
            self.system_status = 'OFF'
            return
        # Use single setpoint for all zones
        for i in range(3):
            error = self.temp_setpoint - self.ZT[i]
            self.VAV[i] += 0.2 * error
            self.VAV[i] = max(0.0, min(1.0, self.VAV[i]))
        # Mode selection: use ambient temperature
        if self.alarm:
            self.system_status = 'EMERGENCY'
        elif self.amb_temp > self.temp_setpoint + 0.5:
            self.system_status = 'COOLING'
        elif self.amb_temp < self.temp_setpoint - 0.5:
            self.system_status = 'HEATING'
        else:
            self.system_status = 'OFF'
        # Fan and coil logic
        self.SF_Cool = int(self.mode == 'cooling')
        self.SF_Heat = int(self.mode == 'heating')
        self.CC_A = int(self.mode == 'cooling')
        self.HC_A = int(self.mode == 'heating')
        self.RF = int(self.SF_Cool or self.SF_Heat)
        # Fan RPM and coil temp logic (dynamic)
        if self.mode == 'cooling':
            self.fan_rpm = 1200 + 400 * max(self.VAV)
            self.coil_temp = max(self.temp_setpoint - 2, 12.0)  # Never below 12°C
        elif self.mode == 'heating':
            self.fan_rpm = 1200 + 400 * max(self.VAV)
            self.coil_temp = min(self.temp_setpoint + 6, 40.0)  # Never above 40°C
        else:
            self.fan_rpm = 1200
            self.coil_temp = 20.0
        # SAT tracks coil temp
        self.SAT = self.coil_temp + 1.0
        # Simulate environment
        for i in range(3):
            vav = self.VAV[i]
            drift = (self.amb_temp - self.ZT[i]) * 0.01
            # Only cool if above setpoint+deadband, only heat if below setpoint-deadband
            if self.mode == 'cooling' and self.SF_Cool and self.ZT[i] > self.temp_setpoint + 0.2:
                cooling_effect = min(0.1 * vav, self.ZT[i] - self.temp_setpoint)
                self.ZT[i] -= cooling_effect + drift + random.uniform(-0.05, 0.05)
            elif self.mode == 'heating' and self.SF_Heat and self.ZT[i] < self.temp_setpoint - 0.2:
                heating_effect = min(0.1 * vav, self.temp_setpoint - self.ZT[i])
                self.ZT[i] += heating_effect + drift + random.uniform(-0.05, 0.05)
            else:
                self.ZT[i] += drift + random.uniform(-0.05, 0.05)
            # CO2 dynamics
            self.CO2[i] += (1-vav)*5 - vav*10 + random.uniform(-2,2)
            self.CO2[i] = max(400, min(2000, self.CO2[i]))
        # Update air temps and flows
        self.MAT = sum(self.ZT) / 3 + random.uniform(-0.2,0.2)
        self.AF_SF = 1.0 + 0.5 * (self.SF_Cool or self.SF_Heat)
        self.AF_RF = 1.0 + 0.5 * self.RF
        # Alarm logic
        self.alarm = any([
            any(z < 16 or z > 30 for z in self.ZT),
            any(c > 1500 for c in self.CO2)
        ])
        if self.alarm:
            print("[ALARM] Condition detected! Check temperature or CO₂ levels.")

    def status(self):
        s = {
            'system_status': self.system_status,
            'mode': self.mode,
            'MAT': self.MAT,
            'SAT': self.SAT,
            'AF_SF': self.AF_SF,
            'AF_RF': self.AF_RF,
            'ZoneTemps': self.ZT,
            'CO2': self.CO2,
            'VAV': self.VAV,
            'SF_Cool': self.SF_Cool,
            'SF_Heat': self.SF_Heat,
            'RF': self.RF,
            'CC_A': self.CC_A,
            'HC_A': self.HC_A,
            'alarm': self.alarm,
            'amb_temp': self.amb_temp,
            'temp_setpoint': self.temp_setpoint,
            'fan_rpm': self.fan_rpm,
            'coil_temp': self.coil_temp,
        }
        return s

if __name__ == "__main__":
    system = HVACSystem()
    system.start()
    for step in range(1, 31):
        system.step()
        s = system.status()
        print(f"\n--- Step {step} --- Mode: {s['mode'].title()} ---")
        for i in range(3):
            print(f"Zone {i+1}: Temp={s['ZoneTemps'][i]:.1f}°C, CO₂={int(s['CO2'][i])} ppm, VAV={s['VAV'][i]:.2f}")
        print(f"Supply Fan (Cooling): {s['SF_Cool']} | Supply Fan (Heating): {s['SF_Heat']} | Return Fan: {s['RF']}")
        print(f"Cooling Coil Valve: {s['CC_A']} | Heating Coil Valve: {s['HC_A']}")
        print(f"MAT: {s['MAT']:.1f}°C | SAT: {s['SAT']:.1f}°C | AF_SF: {s['AF_SF']:.2f} | AF_RF: {s['AF_RF']:.2f}")
        print(f"Fan RPM: {s['fan_rpm']:.0f} | Coil Output Temp: {s['coil_temp']:.1f}°C")
        if s['alarm']:
            print("[ALARM] System alarm is active!")
        time.sleep(0.5)
