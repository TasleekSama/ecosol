from PIL import Image
import os

# Directory containing the images
folder_path = 'projects'

# Output directory to save resized images
output_folder = 'projectspy'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  # Add any file types as needed
        image_path = os.path.join(folder_path, filename)
        img = Image.open(image_path)
        img = img.resize((600, 400), Image.Resampling.LANCZOS)  # Resize the image using high-quality downsampling filter
        # Save the image in PNG format in the output folder
        img.save(os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.png"))

print("Resizing complete.")
