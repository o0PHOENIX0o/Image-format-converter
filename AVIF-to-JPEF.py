from PIL import Image
import os

# Folder containing images
folder = 'banners'

# Input and output directories
input_dir = f'C:/Users/User/...{folder}'
output_dir = f'C:/Users/User/...{folder}'

# Dictionary of image formats and their respective slice lengths
image_formats = {
    'jpg': -4,
    'jpeg': -5,
    'avif': -5,
    # Add more formats here as needed
}

# Convert images to the following output format
output_format = 'png'

# Convert images for each specified format
for ImgType, sliceLength in image_formats.items():
    for filename in os.listdir(input_dir):
        if filename.endswith(f'.{ImgType}'):
            print(filename[:sliceLength])

            img = Image.open(os.path.join(input_dir, filename))
            img.save(os.path.join(output_dir, f'{filename[:sliceLength]}.{output_format}'))

            os.unlink(os.path.join(input_dir, filename))
