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

## Library yang Digunakan  
- **NumPy**: Untuk operasi array dan pengolahan data numerik.  
- **OpenCV**: Untuk memproses gambar.  
- **Scikit-Image**: Untuk ekstraksi fitur GLCM.  
- **Matplotlib** *(opsional)*: Untuk visualisasi hasil.  

## Kontribusi  
Kontribusi sangat diterima! Anda dapat:  
1. Melaporkan bug melalui [Issues](https://github.com/username/Klasifikasi-GLCM---Bakso/issues).  
2. Membuat pull request untuk fitur baru.  
