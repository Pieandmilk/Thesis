import os

folder_path = r'E:\code\Thesis\Dataset\Lean Pork'

# Step 1: Get image files
image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
image_files.sort()

# Step 2: Rename all files to temporary names
for idx, filename in enumerate(image_files, start=1):
    ext = os.path.splitext(filename)[1]
    temp_name = f'temp_cb{idx}{ext}'
    src = os.path.join(folder_path, filename)
    dst = os.path.join(folder_path, temp_name)
    os.rename(src, dst)

# Step 3: Rename temporary files to final names
temp_files = [f for f in os.listdir(folder_path) if f.startswith('temp_cb')]
temp_files.sort()

for idx, filename in enumerate(temp_files, start=1):
    ext = os.path.splitext(filename)[1]
    final_name = f'lp{idx}{ext}'
    src = os.path.join(folder_path, filename)
    dst = os.path.join(folder_path, final_name)
    os.rename(src, dst)
    print(f'Renamed: {filename} → {final_name}')
