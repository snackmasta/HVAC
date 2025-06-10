# 8. Perangkat Keras Kendali Utilitas Dalam Sistem HVAC

Perangkat keras utama pada sistem HVAC (Heating, Ventilation, and Air Conditioning) single duct, multi-zone, VAV meliputi:

- **PLC (Programmable Logic Controller)**: Mengendalikan seluruh proses otomatisasi HVAC, menerima input dari sensor dan mengatur aktuator (VAV, katup coil, fan) sesuai logika kontrol. Contoh: Siemens S7-1200 atau setara, mendukung standar IEC 61131, komunikasi Modbus/TCP, dan integrasi HMI.
- **Sensor Suhu Udara**:
  - MAT (Mixed Air Temp Sensor): Sensor suhu udara campuran di mixing box, tipe PT100/NTC/DS18B20, akurasi industri.
  - SAT (Supply Air Temp Sensor): Sensor suhu udara suplai di supply duct, tipe PT100/NTC/DS18B20.
  - Z1T, Z2T, Z3T (Zone Temp Sensor): Sensor suhu di masing-masing zona, tipe PT100/NTC/DS18B20.
- **Sensor Aliran Udara**:
  - AF_SF (Airflow Sensor Supply Fan): Sensor airflow pada supply fan, tipe differential pressure/ultrasonic.
  - AF_RF (Airflow Sensor Return Fan): Sensor airflow pada return fan, tipe differential pressure/ultrasonic.
- **Sensor CO₂**:
  - CO2_1, CO2_2, CO2_3: Sensor CO₂ di tiap zona, tipe NDIR, untuk monitoring kualitas udara.
- **VAV Actuator**:
  - VAV1A, VAV2A, VAV3A: Motorized damper actuator untuk pengaturan volume udara di tiap zona (VAV Unit Zone 1/2/3).
- **Katup Coil**:
  - CC_A (Cooling Coil Valve): Motorized valve untuk cooling coil.
  - HC_A (Heating Coil Valve): Motorized valve untuk heating coil.
- **Supply Fan**:
  - SF_Cool (Supply Fan Cooling): Kipas suplai mode pendinginan, AC/EC Fan 3~ 380V.
  - SF_Heat (Supply Fan Heating): Kipas suplai mode pemanasan, AC/EC Fan 3~ 380V.
- **Return Fan (RF)**: Kipas return, AC/EC Fan 3~ 380V, untuk sirkulasi udara return.
- **Panel Kontrol**: Panel mild steel IP54, berisi PLC, relay, terminal, proteksi, dan HMI touchscreen 7 inci.

---

## 8.1 Tabel Ringkasan Spesifikasi Perangkat Keras

| Tag/Perangkat    | Tipe/Model         | Fungsi Utama                        | Lokasi/Spesifikasi             |
|------------------|--------------------|-------------------------------------|-------------------------------|
| PLC              | Siemens S7-1200 / setara | Otomasi & kendali sistem HVAC      | Panel Kontrol, IEC 61131      |
| MAT              | PT100/NTC/DS18B20  | Mixed Air Temp Sensor               | Mixing Box, Akurasi industri  |
| SAT              | PT100/NTC/DS18B20  | Supply Air Temp Sensor              | Supply Duct                   |
| Z1T, Z2T, Z3T    | PT100/NTC/DS18B20  | Zone Temp Sensor                    | Zona 1/2/3                    |
| AF_SF            | DP/Ultrasonic      | Airflow Sensor (Supply Fan)         | Supply Fan                    |
| AF_RF            | DP/Ultrasonic      | Airflow Sensor (Return Fan)         | Return Fan                    |
| CO2_1, CO2_2, CO2_3 | NDIR CO₂ Sensor | CO₂ Sensor (tiap zona)              | Zona 1/2/3                    |
| VAV1A, VAV2A, VAV3A | Motorized Damper | VAV Actuator (tiap zona)            | VAV Unit Zone 1/2/3           |
| CC_A             | Motorized Valve    | Cooling Coil Valve                  | Cooling Coil                  |
| HC_A             | Motorized Valve    | Heating Coil Valve                  | Heating Coil                  |
| SF_Cool          | AC/EC Fan 3~ 380V  | Supply Fan (Cooling)                | Supply Duct                   |
| SF_Heat          | AC/EC Fan 3~ 380V  | Supply Fan (Heating)                | Supply Duct                   |
| RF               | AC/EC Fan 3~ 380V  | Return Fan                          | Return Duct                   |
| Panel Kontrol    | Mild Steel IP54    | Integrasi & proteksi sistem         | Ruang Panel                   |

---

## 8.2 Spesifikasi Hardware Sistem HVAC


### PLC/Controller

- Siemens S7-1200 atau setara, mendukung multi-zona, standar IEC 61131
- Komunikasi: Modbus/TCP, Ethernet
- HMI touchscreen 7 inci


### Sensor

- Suhu: PT100/NTC/DS18B20, akurasi industri, pemasangan di mixing box, supply duct, dan tiap zona
- Airflow: Differential pressure/ultrasonic, pemasangan di supply dan return fan
- CO₂: NDIR, pemasangan di tiap zona


### Aktuator

- VAV: Motorized damper, kontrol analog/digital, satu per zona
- Katup coil: Motorized valve, kontrol analog/digital, untuk cooling dan heating coil


### Fan

- Supply Fan: AC/EC Fan 3~ 380V, satu untuk cooling, satu untuk heating
- Return Fan: AC/EC Fan 3~ 380V


### Panel Kontrol

- Mild steel IP54, berisi PLC, relay, terminal, proteksi, HMI touchscreen
- Wiring sesuai standar industri HVAC (color coding, labeling, grounding)


### Power

- Tegangan dan arus sesuai kebutuhan fan, aktuator, sensor, dan PLC
- Power supply sesuai standar IEC dan lokal


### Lain-lain

- Semua hardware dan instalasi mengikuti standar industri (ASHRAE, ISO 16484, IEC 61131)
- Tersedia daftar suku cadang dan prosedur maintenance

---

*Catatan: Semua perangkat keras di atas telah diintegrasikan dan dikendalikan secara otomatis melalui PLC dan HMI sesuai dengan dokumentasi dan program pada project ini. Sistem HVAC ini didesain untuk pengkondisian dan distribusi udara pada multi-zona dengan kontrol VAV, serta memenuhi standar industri HVAC modern.*
