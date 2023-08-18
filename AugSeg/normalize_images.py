from PIL import Image
import os
import numpy as np

def normalize_image(image_path):
    img = Image.open(image_path)
    img_array = np.array(img, dtype=np.float32)

    if len(img_array.shape) == 3 and img_array.shape[2] == 3:
        img_array = img_array / 255.0  # Normalize pixel values to [0, 1] for RGB images

    return img_array

def enhance_contrast(img_array):
    min_val = img_array.min()
    max_val = img_array.max()
    diff = max_val - min_val

    if diff == 0:
        stretched_img = np.zeros_like(img_array)
    else:
        stretched_img = (img_array - min_val) / diff
    
    return stretched_img

def save_normalized_images(image_list, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for img_path in image_list:
        img_array_normalized = normalize_image(img_path)
        img_name = os.path.basename(img_path)
        
        # This was added to make domain distinction more apparent
        enhanced_img_array = enhance_contrast(img_array_normalized)
        
        # save data as png
        output_path = os.path.join(output_dir, os.path.splitext(img_name)[0] + ".png")

        normalized_img = Image.fromarray((enhanced_img_array * 255).astype(np.uint8))

        # Change grayscale image to rgb
        if normalized_img.mode != "RGB":
            normalized_img = normalized_img.convert("RGB")

        normalized_img.save(output_path)

if __name__ == "__main__":
    image_dir = "./data/MagneticDomainRaw/UnnormalizedMagDom/"#"./data/NormalizedMagDom/NormalizedMagDomPNG/"
    output_dir = "./data/NormalizedMagDom/NormalizedMagDomRaw01/"
    image_list = [os.path.join(image_dir, img_file) for img_file in os.listdir(image_dir) if img_file.lower().endswith(('.png', '.tiff', '.tif'))]

    if not image_list:
        print("No PNG or TIFF images found in the specified directory.")
    else:
        save_normalized_images(image_list, output_dir)
        print("Images normalized and saved to", output_dir)