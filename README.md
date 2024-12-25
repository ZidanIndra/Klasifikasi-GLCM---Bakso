# Klasifikasi GLCM - Bakso  
Repository ini berisi program untuk mengekstraksi fitur gambar bakso menggunakan metode **Gray Level Co-occurrence Matrix (GLCM)**. Program ini bertujuan untuk mengolah citra bakso dan menganalisis teksturnya sebagai fitur yang relevan untuk klasifikasi atau analisis lainnya.  

## Fitur Utama  
- Ekstraksi fitur tekstur dari gambar menggunakan GLCM.  
- Penyimpanan hasil ekstraksi fitur dalam format yang mudah dianalisis.  
- Proyek ini cocok untuk pengembangan aplikasi klasifikasi berbasis gambar bakso.  

## Struktur Folder  
```
Klasifikasi-GLCM---Bakso/
│
├── dataset/                 # Folder untuk menyimpan gambar bakso
├── script/                     # Folder untuk script Python
│   └── glcm_extraction.py   # Script utama untuk ekstraksi fitur GLCM
├── requirements.txt         # Daftar library yang dibutuhkan
└── README.md                # Dokumentasi proyek
```

## Prasyarat  
Sebelum menjalankan program, pastikan Anda memiliki:  
- Python 3.7 atau versi lebih baru.  
- Gambar dataset bakso yang akan diproses, simpan di folder `dataset/`.  

## Cara Instalasi  
1. **Clone Repository**  
   Jalankan perintah berikut di terminal Anda untuk mengunduh repository ini:  
   ```bash
   git clone https://github.com/username/Klasifikasi-GLCM---Bakso.git
   cd Klasifikasi-GLCM---Bakso
   ```  

2. **Install Library yang Dibutuhkan**  
   Semua library yang diperlukan sudah tercantum di file `requirements.txt`. Gunakan perintah berikut untuk menginstalnya:  
   ```bash
   pip install -r requirements.txt
   ```  

3. **Jalankan Program**  
   Setelah semua library terinstal, Anda dapat menjalankan script utama:  
   ```bash
   python src/glcm_extraction.py
   ```

4. Hasil Analisis
Pada penelitian ini, dilakukan ekstraksi fitur citra bakso menggunakan metode Gray Level Co-occurrence Matrix (GLCM). Fitur yang diekstraksi adalah Contrast dan Homogeneity pada saluran warna (Blue, Green, dan Red). Citra bakso diambil pada interval waktu yang berbeda (fresh, >4 jam, >8 jam, >12 jam, >16 jam, >20 jam, >24 jam, >28 jam) untuk menganalisis perubahan tekstur dan distribusi warna seiring waktu.

![download (6)](https://github.com/user-attachments/assets/e4d8f572-93c1-4dd6-bc4c-2278a3ada58d)

Grafik Atas (Contrast Across Blue, Green, Red Channels):
Grafik ini menunjukkan nilai rata-rata contrast untuk setiap saluran warna. Nilai contrast cenderung menurun seiring waktu, yang mengindikasikan penurunan detail tekstur pada permukaan bakso.

Grafik Bawah (Homogeneity Across Blue, Green, Red Channels):
Grafik ini menunjukkan nilai rata-rata homogeneity untuk setiap saluran warna. Nilai homogeneity cenderung meningkat seiring waktu, mengindikasikan distribusi warna pada citra bakso menjadi semakin seragam seiring proses perubahan.



## Library yang Digunakan  
- **NumPy**: Untuk operasi array dan pengolahan data numerik.  
- **OpenCV**: Untuk memproses gambar.  
- **Scikit-Image**: Untuk ekstraksi fitur GLCM.  
- **Matplotlib** *(opsional)*: Untuk visualisasi hasil.  

## Kontribusi  
Kontribusi sangat diterima! Anda dapat:  
1. Melaporkan bug melalui [Issues](https://github.com/username/Klasifikasi-GLCM---Bakso/issues).  
2. Membuat pull request untuk fitur baru.  
