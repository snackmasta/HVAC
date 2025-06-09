# 7. Posisi Utilitas HVAC

Penataan posisi utilitas dalam sistem HVAC sangat penting untuk memastikan efisiensi operasional, kemudahan pemeliharaan, dan keamanan sistem secara keseluruhan. Berikut penjelasan posisi dan peran strategis masing-masing utilitas:

## 7.1 Diagram Posisi Utilitas

```mermaid
block-beta
  columns 3
  Intake["Pompa Intake\n(Sumur/Laut)"] space:2
  PraPerlakuan["Unit Pra-perlakuan\n(Filter, Sensor)"] space:2
  HVAC["Unit HVAC\n(Filter, Pompa)"] space:2
  TangkiGround["Tangki Ground"] TransferBooster["Pompa Transfer & Booster"] TangkiRooftop["Tangki Rooftop"]
  PanelKontrol["Panel Kontrol\n(PLC, HMI)"] Sensor["Sensor\n(Level, Tekanan, dsb.)"] space

  Intake --> PraPerlakuan
  PraPerlakuan --> HVAC
  HVAC --> TangkiGround
  TangkiGround --> TransferBooster
  TransferBooster --> TangkiRooftop

  PanelKontrol --- Intake
  PanelKontrol --- PraPerlakuan
  PanelKontrol --- HVAC
  PanelKontrol --- TransferBooster
  PanelKontrol --- TangkiRooftop

  Sensor --- Intake
  Sensor --- PraPerlakuan
  Sensor --- HVAC
  Sensor --- TangkiGround
  Sensor --- TransferBooster
  Sensor --- TangkiRooftop
```

## 7.2 Panel Kontrol
Panel kontrol ditempatkan di ruang kontrol atau dekat area proses utama. Lokasi ini dipilih agar operator mudah memantau dan mengendalikan seluruh sistem, serta memudahkan akses saat troubleshooting atau pemeliharaan.

## 7.3 Pompa Intake
Pompa intake dipasang di area sumber udara (luar ruangan) untuk memudahkan pengambilan udara secara langsung dan mengurangi kehilangan tekanan akibat jarak distribusi.

## 7.4 Unit Pra-perlakuan
Unit pra-perlakuan ditempatkan dekat intake dan sebelum unit HVAC. Penempatan ini memastikan udara yang masuk ke sistem sudah melalui proses penyaringan awal, sehingga memperpanjang umur komponen sistem.

## 7.5 Unit HVAC
Unit HVAC berada di ruang proses utama, biasanya terpusat dengan akses mudah untuk pemantauan dan perawatan. Penempatan ini juga mempertimbangkan kebutuhan ruang dan keamanan dari paparan lingkungan luar.

## 7.6 Tangki Ground
Tangki ground diletakkan setelah unit HVAC dan sebelum pompa transfer. Fungsinya sebagai penampung sementara udara hasil olahan sebelum didistribusikan lebih lanjut.

## 7.7 Pompa Transfer & Booster
Pompa transfer dan booster ditempatkan di ruang pompa, di antara tangki ground dan tangki rooftop. Penempatan ini memudahkan pengaturan tekanan dan aliran udara ke tangki rooftop maupun ke jaringan distribusi.

## 7.8 Tangki Rooftop
Tangki rooftop dipasang di atap bangunan untuk memanfaatkan gravitasi dalam distribusi udara ke seluruh jaringan pelanggan, serta sebagai cadangan saat terjadi gangguan pasokan.

## 7.9 Sensor
Sensor (level, tekanan, flow, turbidity) dipasang pada titik-titik strategis di seluruh sistem, seperti pada tangki, pipa, dan unit proses. Penempatan sensor disesuaikan dengan kebutuhan monitoring dan kontrol otomatis.

Dengan penataan posisi utilitas yang tepat, sistem HVAC dapat beroperasi secara optimal, mudah dipantau, dan efisien dalam pemeliharaan.
