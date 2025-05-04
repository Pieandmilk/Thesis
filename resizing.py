from PIL import Image
import os

# Source folder containing the original images
source_folder = r'E:\code\Thesis\Dataset\valid'

# Destination folder for resized images
destination_folder = r'E:\code\Thesis\Dataset\resized_valid'

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Desired size
target_size = (512, 512)

# Process each image
for filename in os.listdir(source_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        with Image.open(source_path) as img:
            resized_img = img.resize(target_size, Image.Resampling.LANCZOS)
            resized_img.save(destination_path)
            print(f'Resized and saved: {filename} → {destination_folder}')
