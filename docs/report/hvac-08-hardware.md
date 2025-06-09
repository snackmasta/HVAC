# Perangkat Keras Kendali Utilitas Dalam Sistem HVAC

Perangkat keras utama pada sistem HVAC (Heating, Ventilation, and Air Conditioning) meliputi:
- **PLC (Programmable Logic Controller)**: Mengendalikan seluruh proses otomatisasi pengolahan air. PLC yang digunakan tipe Siemens S7-1200, mendukung komunikasi Modbus/TCP dan integrasi HMI.
- **Sensor Level (LT-101, LT-102)**: Sensor ultrasonik untuk mengukur ketinggian air pada tangki ground dan rooftop, dengan output analog 4-20mA.
- **Sensor Tekanan (PT-101, PT-102)**: Transmitter tekanan tipe digital, range 0-10 bar, untuk memantau tekanan pada feed RO dan permeate.
- **Sensor Flow (FT-101, FT-102)**: Flowmeter elektromagnetik, range 0-20 m3/jam, untuk mengukur laju aliran air pada intake dan output RO.
- **Sensor Turbidity (TU-101)**: Sensor kekeruhan tipe optik, range 0-100 NTU, untuk memantau kualitas air pada outlet pra-perlakuan.
- **Pompa**: Pompa sentrifugal untuk intake, RO, transfer, booster, dan post-treatment, masing-masing dilengkapi proteksi thermal dan overload.
- **Valve Motorized (V-101 s/d V-106)**: Katup bermotor tipe on/off, dikendalikan otomatis oleh PLC untuk mengatur aliran air pada berbagai jalur proses.
- **Unit UV Disinfection (UV-101)**: Modul UV kapasitas 2 m3/jam untuk desinfeksi air hasil RO.
- **Alarm (ALM-101)**: Sirine dan lampu indikator untuk memberikan peringatan kondisi abnormal (misal: level rendah, tekanan tinggi, kegagalan pompa).
- **Panel Kontrol**: Panel berbahan mild steel IP54, berisi PLC, relay, terminal, proteksi, dan HMI touchscreen 7 inci.

---

### Tabel Ringkasan Spesifikasi Perangkat Keras

| Perangkat         | Tipe/Model         | Fungsi Utama                        | Lokasi Pemasangan         |
|------------------|--------------------|-------------------------------------|--------------------------|
| PLC              | Siemens S7-1200    | Otomasi & kendali proses            | Panel Kontrol            |
| Sensor Level     | Ultrasonik 4-20mA  | Deteksi ketinggian air              | Tangki Ground/Rooftop    |
| Sensor Tekanan   | Digital 0-10 bar   | Monitoring tekanan                  | Pipa Feed/Permeate       |
| Sensor Flow      | Elektromagnetik    | Monitoring laju aliran              | Intake/Output RO         |
| Sensor Turbidity | Optik 0-100 NTU    | Monitoring kekeruhan                | Outlet Pra-perlakuan     |
| Pompa            | Cetrifugal 1-5 kW  | Sirkulasi & transfer air            | Intake, RO, dst          |
| Valve Motorized  | On/Off AC 220V     | Pengaturan aliran                   | Jalur distribusi         |
| UV Disinfection  | 2 m3/jam           | Desinfeksi air                      | Output RO                |
| Alarm            | Sirine + Lampu     | Indikasi kondisi abnormal           | Panel Kontrol            |
| Panel Kontrol    | Mild Steel IP54    | Integrasi & proteksi sistem         | Ruang Panel              |

---

## Lampiran: Spesifikasi Hardware Sistem HVAC

(Lihat detail pada dokumen hardware-spec.md untuk spesifikasi lengkap pompa, filter, sensor, dan panel kontrol yang digunakan pada sistem HVAC.)

---

*Catatan: Semua perangkat keras di atas telah diintegrasikan dan dikendalikan secara otomatis melalui PLC dan HMI sesuai dengan dokumentasi dan program pada project ini.*
