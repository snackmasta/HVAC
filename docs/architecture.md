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
