# HVAC System Architecture (Single Duct, Multiple Zone, VAV System)

This diagram illustrates the architecture of a single duct, multiple zone, VAV (Variable Air Volume) HVAC system, now including a heating coil (HC) with a separate supply fan, activated conditionally.

```mermaid
flowchart LR
    OA["Outside Air"]
    RA["Return Air"]
    EA["Exhaust Air"]
    Mixing["Mixing Box"]
    CC["Cooling Coil (CC)"]
    SF_Cool["Supply Fan (Cooling)"]
    HC["Heating Coil (HC)"]
    SF_Heat["Supply Fan (Heating)"]
    SD["Supply Duct"]
    VAV1["VAV Unit (Zone 1)"]
    VAV2["VAV Unit (Zone 2)"]
    VAV3["VAV Unit (Zone 3)"]
    Z1["Zone 1"]
    Z2["Zone 2"]
    Z3["Zone 3"]
    RD["Return Duct"]
    RF["Return Fan"]

    OA --> Mixing
    RA --> Mixing
    Mixing --> CC --> SF_Cool
    Mixing --> HC --> SF_Heat
    SF_Cool --> SD
    SF_Heat --> SD
    SD --> VAV1 --> Z1
    SD --> VAV2 --> Z2
    SD --> VAV3 --> Z3
    Z1 --> RD
    Z2 --> RD
    Z3 --> RD
    RD --> RF
    RF --> RA
    RF --> EA
```

- Outside and return air are mixed, then either cooled or heated depending on demand.
- Cooling and heating coils each have their own supply fan, operating conditionally.
- Air is supplied to all zones via a single duct, with VAV units for each zone.
- Return air is collected and partially exhausted.

---

## Detailed Architecture with Sensors and Actuators

```mermaid
%%{init: { 'layout': 'elk', 'theme': 'base' }}%%
flowchart LR
    Start([System Start])
    Stop([System Stop])
    OA["Outside Air"]
    RA["Return Air"]
    EA["Exhaust Air"]
    Mixing["Mixing Box"]
    CC["Cooling Coil (CC)"]
    HC["Heating Coil (HC)"]
    SF_Cool["Supply Fan (Cooling)"]
    SF_Heat["Supply Fan (Heating)"]
    SD["Supply Duct"]
    VAV1["VAV Unit (Zone 1)"]
    VAV2["VAV Unit (Zone 2)"]
    VAV3["VAV Unit (Zone 3)"]
    Z1["Zone 1"]
    Z2["Zone 2"]
    Z3["Zone 3"]
    RD["Return Duct"]
    RF["Return Fan"]
    PLC["PLC"]

    subgraph Sensors
        MAT["Mixed Air Temp Sensor"]
        SAT["Supply Air Temp Sensor"]
        AF_SF["Airflow Sensor (Supply Fan)"]
        AF_RF["Airflow Sensor (Return Fan)"]
        CO2_1["CO₂ Sensor (Zone 1)"]
        CO2_2["CO₂ Sensor (Zone 2)"]
        CO2_3["CO₂ Sensor (Zone 3)"]
        Z1T["Zone 1 Temp Sensor"]
        Z2T["Zone 2 Temp Sensor"]
        Z3T["Zone 3 Temp Sensor"]
    end

    subgraph Actuators
        VAV1A["VAV Actuator (Zone 1)"]
        VAV2A["VAV Actuator (Zone 2)"]
        VAV3A["VAV Actuator (Zone 3)"]
        CC_A["Cooling Coil Valve"]
        HC_A["Heating Coil Valve"]
        SF_Cool["Supply Fan (Cooling)"]
        SF_Heat["Supply Fan (Heating)"]
        RF["Return Fan"]
    end

    Start --> Mixing
    OA --> Mixing
    RA --> Mixing
    Mixing --> MAT
    Mixing --> SAT
    Mixing --> CC --> SF_Cool
    Mixing --> HC --> SF_Heat
    CC --> SAP
    SF_Cool --> AF_SF
    SF_Heat --> AF_SF
    SF_Cool --> SD
    SF_Heat --> SD
    SD --> VAV1 --> Z1
    SD --> VAV2 --> Z2
    SD --> VAV3 --> Z3
    Z1 --> Z1T
    Z2 --> Z2T
    Z3 --> Z3T
    Z1 --> CO2_1
    Z2 --> CO2_2
    Z3 --> CO2_3
    Z1 --> RD
    Z2 --> RD
    Z3 --> RD
    RD --> RF
    RF --> AF_RF
    RF --> RA
    RF --> EA
    DP_F -.-> SF_Cool
    DP_F -.-> SF_Heat
    VAV1A -.-> VAV1
    VAV2A -.-> VAV2
    VAV3A -.-> VAV3
    CC_A -.-> CC
    HC_A -.-> HC
    EA --> Stop
    RF --> Stop
    MAT -- Measured --> PLC
    SAT -- Measured --> PLC
    AF_SF -- Measured --> PLC
    AF_RF -- Measured --> PLC
    CO2_1 -- Measured --> PLC
    CO2_2 -- Measured --> PLC
    CO2_3 -- Measured --> PLC
    Z1T -- Measured --> PLC
    Z2T -- Measured --> PLC
    Z3T -- Measured --> PLC
    PLC -- Control --> VAV1A
    PLC -- Control --> VAV2A
    PLC -- Control --> VAV3A
    PLC -- Control --> CC_A
    PLC -- Control --> HC_A
    PLC -- Control --> SF_Cool
    PLC -- Control --> SF_Heat
    PLC -- Control --> RF
```

- This detailed architecture groups all sensors and actuators for clarity, showing their placement and function in the HVAC system. Start and stop points are now included for system operation.
- A PLC (Programmable Logic Controller) node is added, with all sensors connected as inputs and all actuators as outputs, representing the control logic and signal flow.
