# Mekanisme Operasi Sistem HVAC

Sistem HVAC (Heating, Ventilation, and Air Conditioning) dirancang untuk beroperasi secara otomatis dengan mengandalkan logika kontrol pada PLC (Programmable Logic Controller). Mekanisme operasi ini memastikan seluruh proses berjalan efisien, aman, dan dapat dipantau secara real-time melalui HMI (Human Machine Interface).

## 1. Start/Stop
Pengoperasian sistem dapat dimulai atau dihentikan melalui HMI. Operator memiliki kontrol penuh untuk melakukan start atau stop seluruh proses, baik secara manual maupun otomatis sesuai jadwal atau kondisi tertentu.

## 2. Pengambilan Air (Intake)
Pompa intake akan aktif secara otomatis jika level air pada tangki ground berada di bawah ambang batas minimum dan seluruh kondisi pra-perlakuan telah terpenuhi. Sistem akan memastikan bahwa air baku yang diambil memenuhi syarat untuk diproses lebih lanjut.

## 3. Pra-perlakuan
Pada tahap ini, air baku melewati filter untuk menghilangkan partikel kasar dan kotoran. Jika tekanan diferensial pada filter melebihi batas yang ditentukan, sistem akan menjalankan proses backwash (pencucian balik) secara otomatis untuk menjaga performa filter.

## 4. Reverse Osmosis (RO)
Pompa RO akan aktif jika proses pra-perlakuan selesai dan level air pada tangki cukup. Sistem akan memantau tekanan dan parameter lain secara kontinu. Jika terdeteksi tekanan abnormal atau kondisi tidak aman, pompa RO akan berhenti secara otomatis untuk mencegah kerusakan.

## 5. Pasca-perlakuan
Setelah proses RO, air hasil olahan akan melalui tahap remineralisasi dan desinfeksi. Kedua proses ini berjalan secara paralel dengan output RO untuk memastikan air yang dihasilkan memenuhi standar kualitas.

## 6. Distribusi
Pompa transfer dan booster akan aktif berdasarkan level air pada tangki rooftop. Sistem akan memastikan distribusi air ke jaringan pelanggan berjalan lancar dan tekanan tetap stabil.

## 7. Alarm dan Proteksi
Jika terjadi kondisi abnormal seperti tekanan berlebih, level air tidak normal, atau turbidity tinggi, sistem akan memicu alarm dan secara otomatis mematikan pompa terkait untuk mencegah kerusakan lebih lanjut.

## 8. Monitoring dan Kontrol
Seluruh parameter proses (tekanan, level, kualitas air, status pompa, dsb.) dapat dipantau secara real-time melalui HMI. Operator dapat melakukan penyesuaian setpoint, melihat histori alarm, dan melakukan troubleshooting jika diperlukan.

Dengan mekanisme operasi ini, sistem HVAC dapat berjalan secara otomatis, efisien, dan aman, serta memudahkan pemantauan dan pengendalian oleh operator.
