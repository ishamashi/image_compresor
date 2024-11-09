import os
from PIL import Image

def convert_to_webp(input_dir, quality=80):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                file_path = os.path.join(root, file)
                output_file = os.path.splitext(file_path)[0] + '.webp'

                try:
                    img = Image.open(file_path)
                    
                    img.save(output_file, 'webp', quality=quality)
                    print(f"Converted {file_path} to {output_file}")
                
                    os.remove(file_path)
                    print(f"Deleted original file: {file_path}")
                except Exception as e:
                    print(f"Error converting {file_path}: {e}")

if __name__ == "__main__":
    public_folder = "./new"  
    convert_to_webp(public_folder, quality=60)  
