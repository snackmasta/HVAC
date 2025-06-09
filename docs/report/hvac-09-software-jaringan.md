# Perangkat Lunak Jaringan Kendali HVAC

Perangkat lunak jaringan kendali HVAC terdiri dari:
- **PLC Program**: Logika kontrol utama (Structured Text/ladder) untuk mengatur urutan operasi, safety, dan fault handling.
- **HMI/SCADA**: Antarmuka operator berbasis software (misal: Python Tkinter, WinCC, Wonderware) untuk monitoring status, alarm, dan kontrol manual.
- **Komunikasi**: Protokol komunikasi industri (Modbus, Ethernet/IP) untuk pertukaran data antara PLC, HMI, dan perangkat lain.
- **Simulasi**: Program simulasi (misal: Python) untuk pengujian logika dan visualisasi proses sebelum implementasi fisik.
- **Data Logging**: Fitur pencatatan data proses untuk analisis dan troubleshooting.

## Lampiran: Control System Plan and I/O Table

### 1. Control Philosophy
- The system is fully automated with manual override for all pumps and valves.
- Main control logic is based on water levels, flow, pressure, and turbidity.
- Alarms are generated for abnormal conditions (low/high level, high turbidity, low pressure, etc.).
- All critical parameters are monitored and logged.
- Local HMI/SCADA for operator interface; remote monitoring optional.
- **Architecture Update:** The system now uses a modular process and control architecture, with clear separation of sensors, logic, and actuators as shown in the updated flowcharts. PLC/SCADA or software logic group handles all process decisions and actuator commands.

### 2. Main Control Logic
- **Seawater Intake Pump**: Starts if pre-treatment and RO are ready, stops on low ground tank level or alarm.
- **Pre-treatment**: Backwash cycle triggered by high differential pressure or timer.
- **RO High-Pressure Pump**: Starts if pre-treatment is OK and ground tank has sufficient level; stops on low pressure, high pressure, or low ground tank level.
- **Post-treatment**: Disinfection and remineralization run in parallel with RO output.
- **Transfer Pump to Roof Tank**: Starts if roof tank is not full and ground tank has water; stops if roof tank is full or ground tank is low.
- **Alarms**: Any abnormal sensor reading triggers alarm and can stop relevant equipment.
- **Architecture Update:** Logic is now explicitly mapped from sensors to logic functions to actuators, as per the new flowcharts. All sensor values are routed to a central logic group (PLC or software), which then controls actuators.

### 3. I/O Table
| Tag/Name                | Type      | Description                                 | Location                | PLC Variable    | HMI Display |
|-------------------------|-----------|---------------------------------------------|-------------------------|-----------------|-------------|
| LT-101                  | AI        | Ground Tank Level Transmitter               | Ground Tank             | LT_101          | ground      |
| LT-102                  | AI        | Roof Tank Level Transmitter                 | Roof Tank               | LT_102          | roof        |
| FT-101                  | AI        | Intake Flow Transmitter                     | Intake Line             | FT_101          | (not displayed) |
| FT-102                  | AI        | RO Permeate Flow Transmitter                | RO Outlet               | FT_102          | (not displayed) |
| PT-101                  | AI        | RO Feed Pressure Transmitter                | RO Feed                 | PT_101          | press       |
| PT-102                  | AI        | RO Permeate Pressure Transmitter            | RO Outlet               | PT_102          | (not displayed) |
| TU-101                  | AI        | Pre-treatment Turbidity Sensor              | Pre-treatment Outlet    | TU_101          | turb        |
| P-101                   | DO        | Seawater Intake Pump Start/Stop             | Intake                  | P_101           | intake      |
| P-102                   | DO        | RO High-Pressure Pump Start/Stop            | RO Feed                 | P_102           | ro          |
| P-103                   | DO        | Post-treatment Pump Start/Stop              | Post-treatment          | P_103           | p103        |
| P-104                   | DO        | Transfer Pump to Ground Tank                | Post-treatment          | P_104           | p104        |
| P-105                   | DO        | Pump to Rooftop                             | Pump Room               | P_105           | p105        |
| P-106                   | DO        | Transfer Pump to Roof Tank                  | Pump Room               | P_106           | p106        |
| V-101                   | DO        | Motorized Valve (Primary)                   | Main Process Line       | V_101           | v101        |
| V-102                   | DO        | RO Feed Valve                               | RO Feed Line            | V_102           | (not displayed) |
| V-103                   | DO        | Post-treatment Valve                        | Post-treatment Line     | V_103           | (not displayed) |
| V-104                   | DO        | Ground Transfer Valve                       | Ground Transfer Line    | V_104           | (not displayed) |
| V-105                   | DO        | Rooftop Pump Valve                          | Rooftop Line            | V_105           | (not displayed) |
| V-106                   | DO        | Roof Tank Transfer Valve                    | Roof Transfer Line      | V_106           | (not displayed) |
| UV-101                  | DO        | UV Disinfection Unit On/Off                 | Post-treatment          | UV_101          | uv101       |
| ALM-101                 | DO        | General Alarm Output                        | Control Panel           | ALM_101         | alm101      |
| PRV-101                 | DO        | Pressure Relief Valve Open/Close            | RO Membrane/Brine Line  | PRV_101         | prv101      |
| SYSTEM_RUNNING          | DI/DO     | System Running State                        | Control Logic           | System_Running  | step        |
| EMERGENCY_STOP          | DI/DO     | Emergency Stop Active                       | Control Logic           | Emergency_Stop  | step        |

**Internal Logic Variables (PLC Only):**
| Variable                | Type      | Description                                 |
|-------------------------|-----------|---------------------------------------------|
| PreTreatment_OK         | BOOL      | Pre-treatment conditions satisfied          |
| RO_OK                   | BOOL      | RO system conditions satisfied              |
| PostTreatment_OK        | BOOL      | Post-treatment conditions satisfied         |
| Alarm                   | BOOL      | Internal alarm condition                    |
| P103_OK                 | BOOL      | P-103 activation condition                  |
| P104_OK                 | BOOL      | P-104 activation condition                  |
| P105_OK                 | BOOL      | P-105 activation condition                  |
| P106_OK                 | BOOL      | P-106 activation condition                  |
| PRV_FAULT               | BOOL      | Pressure relief valve fault condition       |

**Legend:**
- AI: Analog Input
- AO: Analog Output  
- DO: Digital Output
- DI: Digital Input
- Comm: Communication

### 4. Control Logic Summary

#### System States:
1. **Emergency Stop**: All actuators OFF, ALM-101 ON, System_Running = FALSE
2. **System Stopped**: All actuators OFF, System_Running = FALSE  
3. **System Running**: Normal operation logic active, System_Running = TRUE

#### Key Logic Conditions (from PLC implementation):
- **PreTreatment_OK**: TU_101 < 5.0 NTU
- **RO_OK**: PreTreatment_OK AND LT_101 > 20% AND PT_101 50-70 bar
- **P_101 (Intake)**: RO_OK AND LT_101 < 95%
- **P_102 (RO Pump)**: RO_OK
- **P_103 (Post-treatment)**: LT_101 > 30%
- **P_104 (Transfer to Ground)**: RO_OK AND LT_101 < 95%
- **P_105 (Pump to Rooftop)**: LT_101 > 40% AND LT_102 < 95%
- **P_106 (Transfer to Roof)**: LT_102 < 98%
- **UV_101**: RO_OK (UV on when RO running)
- **V_101**: P_101 OR P_102 (open when intake or RO active)
- **PRV_101**: PT_101 > 70 bar (pressure relief)
- **Alarm**: TU_101 > 10 NTU OR PT_101 < 45 OR PT_101 > 75 OR LT_101 < 10% OR LT_102 > 98%

### 5. Notes
- All analog signals are 4–20 mA.
- All pumps and valves have local/remote and manual/auto modes.
- System can be expanded for remote monitoring, data logging, and advanced diagnostics.
- **Architecture Update:** The I/O table now includes all actuators and sensors as per the new architecture, including additional pumps (P-103 to P-106), system control variables (System_Running, Emergency_Stop), and explicit mapping between PLC variables and HMI display elements.
- **Synchronization**: I/O table fully matches current PLC implementation (plc file) and HMI display (hmi.py) as of latest update.
