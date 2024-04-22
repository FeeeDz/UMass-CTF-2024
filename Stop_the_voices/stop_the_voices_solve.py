import cv2
import os
import numpy as np

# Percorso della cartella contenente le immagini
input_folder_path = "./samples"

# Lista per memorizzare tutte le immagini
images = []

# Loop attraverso tutte le immagini nella cartella di input
for filename in os.listdir(input_folder_path):
    if filename.endswith(".png"):
        # Carica l'immagine
        image_path = os.path.join(input_folder_path, filename)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if image is None:
            print(f"Errore nel caricamento dell'immagine: {filename}")
            continue

        # Aggiungi l'immagine alla lista
        images.append(image)

# Somma tutte le immagini nella lista
sum_image = np.sum(images, axis=0)  # Somma lungo l'asse 0 (lungo le immagini)

# Calcola la media delle immagini sommate
mean_image = sum_image / len(images)

# Salva l'immagine media
output_folder_path = "./denoised_samples"
os.makedirs(output_folder_path, exist_ok=True)
output_path = os.path.join(output_folder_path, "mean_image.png")
cv2.imwrite(output_path, mean_image)

print("Processo completato. Immagine media salvata.")
# Converti l'immagine media a 8-bit in scala di grigi
mean_image_8bit = cv2.normalize(mean_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Applica il filtro CLAHE per migliorare la definizione dell'immagine media
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
mean_image_clahe = clahe.apply(mean_image_8bit)

# Salva l'immagine media con CLAHE
output_path_clahe = os.path.join(output_folder_path, "mean_image_clahe.png")
cv2.imwrite(output_path_clahe, mean_image_clahe)

print("Processo completato. Immagine media salvata con CLAHE.")
# UMASS{#id31n9_L1k3_@_c#Am3_le0n}
