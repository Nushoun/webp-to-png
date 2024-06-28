from PIL import Image
import os

def convert_webp_to_png(input_folder, output_folder):
    """
    Converts a WEBP image to PNG format.
    
    :param input_path: Path to the input WEBP image.
    :param output_path: Path to save the output PNG image.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.webp'):
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + '.png'
            output_path = os.path.join(output_folder, output_filename)
            
            try:
                # Open the WEBP image
                with Image.open(input_path) as img:
                    # Convert and save as PNG
                    img.save(output_path, 'PNG')
                print(f"Converted: {input_path} to {output_path}")
            except Exception as e:
                print(f"Error converting {input_path}: {e}")

# Example usage
input_file = 'path_to_input_image.webp'
output_file = 'path_to_output_image.png'
convert_webp_to_png("input_folder", "output_folder")
