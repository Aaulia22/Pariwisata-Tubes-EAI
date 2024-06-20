# Pariwisata-Tubes-EAI
# Pariwisata Project

## Deskripsi
Proyek ini terdiri dari dua layanan utama:
- Layanan Pemesanan Tiket: Memfasilitasi pemesanan tiket pesawat, kereta, hotel, dan objek wisata.
- Layanan Informasi Wisata: Menyediakan informasi tentang tempat wisata, objek wisata, dan acara lokal.

## Struktur Microservices & Endpoint API

### Layanan Pemesanan Tiket
- **GET /bookings**: Mengambil semua pemesanan.
- **POST /bookings**: Membuat pemesanan baru.
- **PUT /bookings/{id}**: Memperbarui pemesanan berdasarkan ID.
- **DELETE /bookings/{id}**: Menghapus pemesanan berdasarkan ID.

### Layanan Informasi Wisata
- **GET /info**: Mengambil semua informasi wisata.
- **POST /info**: Menambahkan informasi wisata baru.
- **PUT /info/{id}**: Memperbarui informasi wisata berdasarkan ID.
- **DELETE /info/{id}**: Menghapus informasi wisata berdasarkan ID.

## Cara Menjalankan
Jalankan perintah berikut untuk memulai layanan:
```sh
docker run -d --name ticket-booking-service --network tourism-network -p 3000:3000 ticket-booking-service
docker run -d --name tourist-info-service --network tourism-network -p 5000:5000 tourist-info-service
docker run -d --name main-application --network tourism-network -p 8000:8000 main-application
