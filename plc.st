(* plc.st - Main PLC Program for Multi-Room HVAC Control *)

PROGRAM HVAC_Control
VAR
    (* Analog Inputs *)
    MAT      : REAL;   (* Mixed Air Temp Sensor *)
    SAT      : REAL;   (* Supply Air Temp Sensor *)
    AF_SF    : REAL;   (* Airflow Sensor - Supply Fan *)
    AF_RF    : REAL;   (* Airflow Sensor - Return Fan *)
    CO2_1    : REAL;   (* CO2 Sensor Zone 1 *)
    CO2_2    : REAL;   (* CO2 Sensor Zone 2 *)
    CO2_3    : REAL;   (* CO2 Sensor Zone 3 *)
    Z1T      : REAL;   (* Zone 1 Temp Sensor *)
    Z2T      : REAL;   (* Zone 2 Temp Sensor *)
    Z3T      : REAL;   (* Zone 3 Temp Sensor *)

    (* Analog/Digital Outputs *)
    VAV1A    : REAL;   (* VAV Actuator Zone 1 *)
    VAV2A    : REAL;   (* VAV Actuator Zone 2 *)
    VAV3A    : REAL;   (* VAV Actuator Zone 3 *)
    CC_A     : REAL;   (* Cooling Coil Valve *)
    HC_A     : REAL;   (* Heating Coil Valve *)
    SF_Cool  : BOOL;   (* Supply Fan Cooling *)
    SF_Heat  : BOOL;   (* Supply Fan Heating *)
    RF       : BOOL;   (* Return Fan *)

    (* Setpoints *)
    Z1T_SP   : REAL := 22.0;  (* Zone 1 Temp Setpoint *)
    Z2T_SP   : REAL := 22.0;  (* Zone 2 Temp Setpoint *)
    Z3T_SP   : REAL := 22.0;  (* Zone 3 Temp Setpoint *)
    CO2_SP   : REAL := 800.0; (* CO2 Setpoint ppm *)

    (* Internal Variables *)
    StartupDone : BOOL := FALSE;
    Fault       : BOOL := FALSE;
END_VAR

(* System Startup and Initialization *)
IF NOT StartupDone THEN
    (* Initialize outputs to safe state *)
    VAV1A := 0.0;
    VAV2A := 0.0;
    VAV3A := 0.0;
    CC_A := 0.0;
    HC_A := 0.0;
    SF_Cool := FALSE;
    SF_Heat := FALSE;
    RF := FALSE;
    StartupDone := TRUE;
END_IF;

(* Monitoring and Control Logic for Each Zone *)
(* Zone 1 *)
IF Z1T > Z1T_SP THEN
    CC_A := 1.0;      (* Open cooling coil *)
    HC_A := 0.0;
    SF_Cool := TRUE;
    SF_Heat := FALSE;
ELSIF Z1T < Z1T_SP THEN
    CC_A := 0.0;
    HC_A := 1.0;      (* Open heating coil *)
    SF_Cool := FALSE;
    SF_Heat := TRUE;
ELSE
    CC_A := 0.0;
    HC_A := 0.0;
    SF_Cool := FALSE;
    SF_Heat := FALSE;
END_IF;

(* VAV Actuator Control - Example: Proportional to Temp Deviation *)
VAV1A := LIMIT(0.0, (Z1T_SP - Z1T) * 10.0, 100.0);

(* Repeat for Zone 2 *)
IF Z2T > Z2T_SP THEN
    (* ...similar logic for cooling/heating... *)
END_IF;
VAV2A := LIMIT(0.0, (Z2T_SP - Z2T) * 10.0, 100.0);

(* Repeat for Zone 3 *)
IF Z3T > Z3T_SP THEN
    (* ...similar logic for cooling/heating... *)
END_IF;
VAV3A := LIMIT(0.0, (Z3T_SP - Z3T) * 10.0, 100.0);

(* CO2 Control - Example: Open VAV if CO2 high *)
IF CO2_1 > CO2_SP THEN
    VAV1A := 100.0;
END_IF;
IF CO2_2 > CO2_SP THEN
    VAV2A := 100.0;
END_IF;
IF CO2_3 > CO2_SP THEN
    VAV3A := 100.0;
END_IF;

(* Safety and Fault Handling *)
IF (MAT < 0.0) OR (SAT > 50.0) THEN
    Fault := TRUE;
    (* Shut down outputs *)
    VAV1A := 0.0;
    VAV2A := 0.0;
    VAV3A := 0.0;
    CC_A := 0.0;
    HC_A := 0.0;
    SF_Cool := FALSE;
    SF_Heat := FALSE;
    RF := FALSE;
END_IF;

(* Shutdown Procedure *)
(* Add logic for system shutdown as needed *)

END_PROGRAM
