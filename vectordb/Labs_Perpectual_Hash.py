from PIL import Image
import imagehash
import os

# Function to generate perceptual hash for a set of images
def generate_hashes(image_folder):
    image_hashes = {}
    for filename in os.listdir(image_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(image_folder, filename)
            image = Image.open(image_path)
            image_hash = imagehash.phash(image)
            image_hashes[filename] = image_hash
    return image_hashes

# Function to search for duplicates or similar images
def search_similar_images(input_image_path, image_hashes):
    input_image = Image.open(input_image_path)
    input_image_hash = imagehash.phash(input_image)
    
    similar_images = []
    for filename, stored_hash in image_hashes.items():
        print(filename ,input_image_hash - stored_hash );
        if input_image_hash - stored_hash < 20:  # Threshold for similarity. This is very critical parameter to tune. Based on this value the results vary significantly
            similar_images.append(filename)
    
    return similar_images

# Example usage
image_folder = "C://KAN//code//data"
input_image_path = "C://KAN//Code//data//animalsafari1.jpg"

# Generate hashes for the set of images
image_hashes = generate_hashes(image_folder)

# Search for duplicates or similar images
similar_images = search_similar_images(input_image_path, image_hashes)

print(f"Similar images found: {similar_images}")