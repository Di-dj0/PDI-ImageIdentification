from PIL import Image
import os

# Directories
input_dir = 'Imagens Originais'
output_dir = 'images_png'

# Create the directory for output
os.makedirs(output_dir, exist_ok=True)

# Convert the images with Pillow
for filename in os.listdir(input_dir):
    if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
        img = Image.open(os.path.join(input_dir, filename))
        output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.png")
        img.save(output_path, 'PNG')
        print(f"Convertida: {filename} -> {output_path}")

print("Conversão concluída.")
