import hashlib
from PIL import Image
import os

def calculate_image_hash(image_path):
    """Calculate SHA-256 hash of the given image file."""
    with Image.open(image_path) as img:
        # Convert image to RGB and resize to a consistent size for hashing
        img = img.convert("RGB").resize((256, 256))
        # Get image data as bytes
        img_data = img.tobytes()
        # Create a SHA-256 hash object
        hash_obj = hashlib.sha256()
        # Update the hash object with the image data
        hash_obj.update(img_data)
        # Get the hexadecimal hash string
        return hash_obj.hexdigest()

def compare_hashes(hash1, hash2):
    """Compare two SHA-256 hashes and return True if they are similar."""
    print(f"Comapring images :",hash1,hash2)
    return hash1 == hash2

def find_similar_images(folder_path):
    """Find and compare similar images in the given folder."""
    image_hashes = {}
    for image_file in os.listdir(folder_path):
        image_path = os.path.join(folder_path, image_file)
        if os.path.isfile(image_path) and image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            print(f"Comapring images :",image_path)

            image_hash = calculate_image_hash(image_path)
            if image_hash in image_hashes:
                print(f"Duplicate found: {image_file} is similar to {image_hashes[image_hash]}")
            else:
                image_hashes[image_hash] = image_file

# Usage example
folder_path = "C://KAN//code//data"
find_similar_images(folder_path)
