# HVAC Control Plan

This document outlines the control plan for the HVAC system, including control logic, sensors, actuators, and operational sequences. Adapted from the Desalination project structure.

## Overview
- Description of the HVAC system's control objectives for multiple rooms
- Key components: sensors, actuators, controllers for each room
- Designed in accordance with industrial standards (e.g., ASHRAE, ISO 16484, IEC 61131 for PLCs)

## Control Logic
- Independent temperature and humidity regulation for each room
- Fan and compressor control per room
- Shared and dedicated equipment handling
- Safety and fault handling (room-specific and global)
- Control logic follows best practices from industrial standards for reliability and safety

## Sequence of Operations
1. System startup and initialization (all rooms)
2. Monitoring environmental conditions in each room
3. Adjusting outputs based on setpoints for each room
4. Shutdown and safety procedures (room and system level)

## Sensors and Actuators
- List of sensors (temperature, humidity, etc.) for each room
- List of actuators (fans, dampers, compressors) per room
- All components selected to meet relevant industrial standards

## Diagrams
- (Insert control logic diagrams for multi-room setup as needed)

# I/O Table for HVAC System (Single Duct, Multiple Zone, VAV)

| Tag/Name         | Type   | Description                        | Location/Function           |
|------------------|--------|------------------------------------|-----------------------------|
| MAT              | AI     | Mixed Air Temp Sensor              | Mixing Box                  |
| SAT              | AI     | Supply Air Temp Sensor             | Supply Duct                 |
| AF_SF            | AI     | Airflow Sensor (Supply Fan)        | Supply Fan                  |
| AF_RF            | AI     | Airflow Sensor (Return Fan)        | Return Fan                  |
| CO2_1            | AI     | CO₂ Sensor (Zone 1)                | Zone 1                      |
| CO2_2            | AI     | CO₂ Sensor (Zone 2)                | Zone 2                      |
| CO2_3            | AI     | CO₂ Sensor (Zone 3)                | Zone 3                      |
| Z1T              | AI     | Zone 1 Temp Sensor                 | Zone 1                      |
| Z2T              | AI     | Zone 2 Temp Sensor                 | Zone 2                      |
| Z3T              | AI     | Zone 3 Temp Sensor                 | Zone 3                      |
| VAV1A            | AO/DO  | VAV Actuator (Zone 1)              | VAV Unit Zone 1             |
| VAV2A            | AO/DO  | VAV Actuator (Zone 2)              | VAV Unit Zone 2             |
| VAV3A            | AO/DO  | VAV Actuator (Zone 3)              | VAV Unit Zone 3             |
| CC_A             | AO/DO  | Cooling Coil Valve                 | Cooling Coil                |
| HC_A             | AO/DO  | Heating Coil Valve                 | Heating Coil                |
| SF_Cool          | AO/DO  | Supply Fan (Cooling)               | Cooling Supply Fan          |
| SF_Heat          | AO/DO  | Supply Fan (Heating)               | Heating Supply Fan          |
| RF               | AO/DO  | Return Fan                         | Return Duct                 |
| PLC              | Comm   | Programmable Logic Controller      | Control Panel               |

**Legend:**
- AI: Analog Input
- AO: Analog Output
- DO: Digital Output
- Comm: Communication

This table matches the detailed architecture and flowchart, listing all sensors (inputs), actuators (outputs), and the PLC as the controller.
