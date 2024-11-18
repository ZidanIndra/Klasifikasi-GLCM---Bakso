import cv2
import os
import numpy as np
import pandas as pd
from skimage import feature
from skimage.util import img_as_ubyte

# Fungsi untuk menghitung rata-rata nilai RGB dari gambar
def extract_rgb_from_image(image):
    B, G, R = cv2.split(image)
    mean_R = np.mean(R)
    mean_G = np.mean(G)
    mean_B = np.mean(B)
    return mean_R, mean_G, mean_B

# Fungsi untuk menghitung fitur GLCM dari gambar channel
def calculate_glcm_features(image_channel):
    bins = np.array([0, 16, 32, 48, 64, 80, 96, 112, 128,
                    144, 160, 176, 192, 208, 224, 240, 255])
    inds = np.digitize(image_channel, bins)
    max_value = inds.max() + 1
    glcm = feature.graycomatrix(inds, [1], [
                                0, np.pi/4, np.pi/2, 3*np.pi/4], levels=max_value, normed=True, symmetric=True)

    contrast = feature.graycoprops(glcm, 'contrast')
    dissimilarity = feature.graycoprops(glcm, 'dissimilarity')
    homogeneity = feature.graycoprops(glcm, 'homogeneity')
    energy = feature.graycoprops(glcm, 'energy')
    correlation = feature.graycoprops(glcm, 'correlation')
    asm = feature.graycoprops(glcm, 'ASM')

    # Hitung Entropi
    glcm = glcm + 1e-10  # Tambahkan nilai kecil untuk menghindari log(0)
    entropy = -np.sum(glcm * np.log2(glcm))

    # Rata-rata fitur di semua arah
    return np.mean(contrast), np.mean(dissimilarity), np.mean(homogeneity), np.mean(energy), np.mean(correlation), np.mean(asm), entropy

# Fungsi untuk memproses semua gambar dalam folder dan menghasilkan CSV
def process_images_in_folder(folder_path, output_csv):
    results = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            image_path = os.path.join(folder_path, filename)
            image = cv2.imread(image_path)

            # Hitung fitur RGB
            mean_R, mean_G, mean_B = extract_rgb_from_image(image)

            # Ekstrak channel warna dan hitung fitur GLCM untuk masing-masing channel
            red_channel = img_as_ubyte(image[:, :, 2])
            green_channel = img_as_ubyte(image[:, :, 1])
            blue_channel = img_as_ubyte(image[:, :, 0])

            contrast_R, dissimilarity_R, homogeneity_R, energy_R, correlation_R, asm_R, entropy_R = calculate_glcm_features(
                red_channel)
            contrast_G, dissimilarity_G, homogeneity_G, energy_G, correlation_G, asm_G, entropy_G = calculate_glcm_features(
                green_channel)
            contrast_B, dissimilarity_B, homogeneity_B, energy_B, correlation_B, asm_B, entropy_B = calculate_glcm_features(
                blue_channel)

            results.append({
                'filename': filename,
                'mean_R': mean_R,
                'mean_G': mean_G,
                'mean_B': mean_B,
                'contrast_R': contrast_R,
                'dissimilarity_R': dissimilarity_R,
                'homogeneity_R': homogeneity_R,
                'energy_R': energy_R,
                'correlation_R': correlation_R,
                'asm_R': asm_R,
                'entropy_R': entropy_R,
                'contrast_G': contrast_G,
                'dissimilarity_G': dissimilarity_G,
                'homogeneity_G': homogeneity_G,
                'energy_G': energy_G,
                'correlation_G': correlation_G,
                'asm_G': asm_G,
                'entropy_G': entropy_G,
                'contrast_B': contrast_B,
                'dissimilarity_B': dissimilarity_B,
                'homogeneity_B': homogeneity_B,
                'energy_B': energy_B,
                'correlation_B': correlation_B,
                'asm_B': asm_B,
                'entropy_B': entropy_B
            })
    df = pd.DataFrame(results)
    df.to_csv(output_csv, index=False)
    print(f'Hasil telah disimpan ke {output_csv}')

# Fungsi untuk memproses semua folder dalam folder utama
def process_all_folders(main_folder_path, output_folder_path):
    os.makedirs(output_folder_path, exist_ok=True)
    for folder_name in os.listdir(main_folder_path):
        folder_path = os.path.join(main_folder_path, folder_name)
        if os.path.isdir(folder_path):
            output_csv = f'{folder_name}_glcm_result.csv'
            output_csv_path = os.path.join(output_folder_path, output_csv)
            process_images_in_folder(folder_path, output_csv_path)

# Path folder utama yang berisi sub-folder gambar dan folder output
main_folder_path = 'D:\Zidan\Citra Digital\sampel'
output_folder_path = 'D:\Zidan\Citra Digital\outputs'

# Proses semua folder dalam folder utama dan simpan hasil ke CSV
process_all_folders(main_folder_path, output_folder_path)
