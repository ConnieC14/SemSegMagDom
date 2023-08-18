import os
import numpy as np
from PIL import Image

# Function to convert dataloop mask to segmentation mask
def convert_dataloop_to_segmentation(dataloop_mask_path, seg_mask_path, class_mapping):
    # Load dataloop mask
    dataloop_mask = Image.open(dataloop_mask_path)
    dataloop_mask = np.array(dataloop_mask)

    H, W, _ = dataloop_mask.shape
    # Initialize segmentation mask  # 1 x height x width
    segmentation_mask = np.zeros_like(dataloop_mask, dtype=np.uint8)

    # Map segmentation classes
    for color, segmentation_class in class_mapping.items():
        segmentation_mask[np.all(dataloop_mask == color, axis=-1)] = segmentation_class

    segmentation_mask = segmentation_mask[:,:,0]#[np.newaxis, :, :,0]
    os.makedirs(os.path.dirname(seg_mask_path), exist_ok=True)

    # Save new mask
    output_mask_image = Image.fromarray(segmentation_mask)
    output_mask_image.save(seg_mask_path)


if __name__ == "__main__":
    # Red, Green, Blue, alpha
    class_mapping = {
        # dataloop Class : Segmentation Class
        (149, 0, 255, 255) : 0, # purple
        (30, 0, 255, 255): 1, # blue
        (255, 0, 0, 255): 2 # red
    }

    dataloop_directory = './data/NormalizedMagDom/AllLabels/'
    output_directory = './data/NormalizedMagDom/PNGMasks/'

    # Iterate through dataloop mask files in the directory
    for filename in os.listdir(dataloop_directory):
        if filename.endswith('.png'):
            dataloop_mask_path = os.path.join(dataloop_directory, filename)
            aug_seg_mask_filename = filename.split(' ')[0] + '.png'
            out_mask_path = os.path.join(output_directory, aug_seg_mask_filename)

            convert_dataloop_to_segmentation(dataloop_mask_path, out_mask_path, class_mapping)
    
    print('complete')
