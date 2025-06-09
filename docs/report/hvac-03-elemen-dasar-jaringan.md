# 3. Elemen Dasar dan Jaringan Sistem HVAC

## 3.1 Pendahuluan

Sistem Heating, Ventilation, and Air Conditioning (HVAC) merupakan sistem kompleks yang terdiri dari berbagai komponen yang saling terintegrasi. Pemahaman tentang elemen dasar dan arsitektur jaringan sistem ini sangat penting untuk merancang sistem yang efisien, handal, dan mudah dioperasikan. Bab ini akan menguraikan komponen-komponen fundamental sistem HVAC serta topologi jaringan yang menghubungkan seluruh elemen sistem.

## 3.2 Elemen Dasar Sistem HVAC

### 3.2.1 Sistem Instrumentasi dan Sensor

Sistem instrumentasi merupakan mata dan telinga dari sistem HVAC yang bertugas mengumpulkan data operasional secara real-time.

#### a) Level Transmitter
- **Fungsi**: Mengukur ketinggian air dalam tangki reservoir, clarifier, dan filter tank
- **Teknologi**: Ultrasonic, radar, atau pressure-based measurement
- **Range pengukuran**: 0-10 meter dengan akurasi ±0.1%
- **Output signal**: 4-20 mA analog atau digital Modbus

#### b) Flow Meter
- **Fungsi**: Mengukur laju aliran air pada berbagai titik dalam sistem
- **Jenis**: Electromagnetic flow meter untuk akurasi tinggi
- **Kapasitas**: 0-500 L/min dengan akurasi ±0.5%
- **Aplikasi**: Monitoring flow rate air baku, produk, dan reject water

#### c) Pressure Sensor
- **Fungsi**: Monitoring tekanan pada membran RO, pompa, dan pipa distribusi
- **Range**: 0-10 bar dengan resolusi 0.01 bar
- **Kritikalitas**: Essential untuk proteksi membran RO
- **Alarm setting**: High pressure >8 bar, Low pressure <2 bar

#### d) Turbidity Sensor
- **Fungsi**: Mengukur kekeruhan air untuk quality control
- **Range**: 0-1000 NTU
- **Lokasi**: Pre-treatment, post-treatment, dan product water
- **Standard**: Sesuai WHO guidelines untuk air minum

#### e) Conductivity/TDS Meter
- **Fungsi**: Mengukur konduktivitas dan Total Dissolved Solids
- **Range**: 0-2000 μS/cm untuk monitoring efektivitas desalinasi
- **Lokasi**: Feed water, permeate, dan concentrate streams

### 3.2.2 Sistem Aktuator dan Kontrol

#### a) Sistem Pompa
- **Intake Pump**: Pompa sentrifugal 5 HP untuk pengambilan air baku
- **High Pressure Pump**: Pompa bertekanan tinggi 15 HP untuk sistem RO
- **Transfer Pump**: Pompa 3 HP untuk transfer antar tangki
- **Booster Pump**: Pompa tekanan rendah 2 HP untuk distribusi
- **Kontrol**: Variable Frequency Drive (VFD) untuk efisiensi energi

#### b) Valve Motorized
- **Jenis**: Ball valve dan butterfly valve dengan electric actuator
- **Fungsi**: Flow control, isolation, dan backwash operations
- **Control signal**: 4-20 mA atau digital on/off
- **Response time**: <30 detik untuk full stroke

#### c) Sistem Disinfeksi UV
- **Kapasitas**: UV lamp 40W dengan intensitas 30 mJ/cm²
- **Fungsi**: Sterilisasi mikroorganisme patogen
- **Monitoring**: UV intensity sensor dan lamp status
- **Maintenance**: Automatic cleaning system

#### d) Sistem Alarm dan Indikasi
- **Visual**: LED indicator panel dan HMI display
- **Audio**: Horn alarm untuk kondisi emergency
- **Remote**: SMS notification dan email alert
- **Logging**: Event logging dengan timestamp

### 3.2.3 Sistem Kontrol PLC/HMI

#### a) Programmable Logic Controller (PLC)
- **Model**: Siemens S7-1200 atau Allen-Bradley CompactLogix
- **I/O capacity**: 32 Digital Input, 16 Digital Output, 16 Analog Input
- **Communication**: Ethernet, Modbus RTU/TCP, Profinet
- **Programming**: Ladder logic dan Function Block Diagram
- **Redundancy**: Hot standby untuk critical applications

#### b) Human Machine Interface (HMI)
- **Display**: 15" touchscreen dengan resolusi 1024x768
- **Software**: WinCC, FactoryTalk View, atau open-source SCADA
- **Features**: Real-time monitoring, trending, alarm management
- **User management**: Multi-level access control
- **Data logging**: Historical data storage dan reporting

### 3.2.4 Panel Kontrol dan Proteksi

#### a) Main Control Panel (MCP)
- **Enclosure**: IP65 stainless steel untuk outdoor installation
- **Components**: PLC, power supply, circuit breakers, relays
- **Cooling**: Forced air circulation dengan air filter
- **Dimensions**: 800x600x300mm dengan cable management

#### b) Motor Control Center (MCC)
- **Function**: Start/stop control dan protection untuk semua motor
- **Protection**: Thermal overload, phase loss, undervoltage
- **Indication**: Running status dan fault indication
- **Control mode**: Local/Remote selection switch

## 3.3 Arsitektur Jaringan Sistem

### 3.3.1 Topologi Jaringan Kontrol

Sistem HVAC menggunakan arsitektur jaringan berlapis (layered architecture) untuk memastikan komunikasi yang handal dan secure:

#### a) Field Level Network
- **Protokol**: Modbus RTU (RS-485) untuk sensor dan aktuator
- **Topology**: Bus topology dengan terminasi resistor
- **Baud rate**: 9600 bps dengan parity checking
- **Cable**: Shielded twisted pair dengan impedansi 120Ω

#### b) Control Level Network
- **Protokol**: Ethernet/IP atau Profinet untuk PLC communication
- **Topology**: Star topology dengan managed switch
- **Speed**: 100 Mbps full duplex
- **Redundancy**: Ring topology untuk fault tolerance

#### c) Supervision Level Network
- **Protokol**: TCP/IP untuk HMI dan SCADA communication
- **Security**: VPN dan firewall untuk remote access
- **Bandwidth**: Minimum 10 Mbps untuk real-time data
- **Cloud connectivity**: IoT gateway untuk remote monitoring

### 3.3.2 Sistem Distribusi Air

#### a) Pipa Distribusi Utama
- **Material**: Stainless steel 316L atau HDPE grade PE100
- **Diameter**: 4" untuk main distribution, 2" untuk secondary
- **Pressure rating**: PN16 (16 bar working pressure)
- **Insulation**: Thermal insulation untuk pipe outdoor

#### b) Valve dan Fitting
- **Isolation valve**: Manual ball valve pada setiap branch
- **Check valve**: Untuk mencegah backflow
- **Pressure relief valve**: Set pada 90% working pressure
- **Flow control valve**: Motorized valve untuk flow regulation

#### c) Storage dan Buffer Tank
- **Material**: Food grade stainless steel atau fiberglass
- **Kapasitas**: 5000L untuk product water storage
- **Features**: Level indicator, overflow protection, drain valve
- **Cleaning**: CIP (Clean-in-Place) system untuk sanitasi

## 3.4 Integrasi Sistem dan Komunikasi

### 3.4.1 Data Acquisition dan Processing

Sistem HVAC mengimplementasikan SCADA (Supervisory Control and Data Acquisition) untuk:
- Real-time data collection dari semua sensor
- Automatic control logic execution
- Alarm management dan notification
- Historical data trending dan analysis
- Report generation untuk compliance

### 3.4.2 Remote Monitoring dan Maintenance

- **Remote access**: VPN connection untuk troubleshooting
- **Predictive maintenance**: Vibration analysis dan thermal monitoring
- **Cloud integration**: Data backup dan analytics
- **Mobile application**: Operator interface untuk mobile devices

## 3.5 Standar dan Compliance

### 3.5.1 Standar Industri
- **IEC 61131-3**: Programming standard untuk PLC
- **ISA-95**: Manufacturing operations management
- **IEC 62443**: Industrial cybersecurity standard
- **WHO Guidelines**: Drinking water quality standards

### 3.5.2 Safety dan Environmental
- **IP rating**: Minimum IP54 untuk semua outdoor equipment
- **Explosion proof**: ATEX certification jika diperlukan
- **EMC compliance**: CE marking untuk electromagnetic compatibility
- **Environmental**: RoHS compliance untuk material

## 3.6 Kesimpulan

Elemen dasar sistem HVAC yang terdiri dari sensor, aktuator, PLC/HMI, jaringan komunikasi, dan panel kontrol membentuk suatu sistem terintegrasi yang mampu beroperasi secara otomatis dengan monitoring real-time. Arsitektur jaringan berlapis memungkinkan komunikasi yang handal antara semua komponen, mulai dari level field device hingga level supervisory. Integrasi yang baik antara semua elemen ini akan menghasilkan sistem HVAC yang efisien, handal, dan mudah dioperasikan serta dipelihara.
