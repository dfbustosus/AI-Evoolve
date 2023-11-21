import os
import requests
from PIL import Image
from io import BytesIO

folder_path = './images/generation'  # Path to the folder containing image files

def download_and_save_images(folder_path):
    # Check if the directory exists
    if not os.path.exists(folder_path):
        print(f"The directory '{folder_path}' does not exist.")
        return
    
    # Iterate through files in the directory
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                url = file.readline().strip()  # Read the URL from the file
                try:
                    response = requests.get(url)
                    if response.status_code == 200:
                        image = Image.open(BytesIO(response.content))
                        image.save(f"{filename}.png", "PNG")  # Save the image as PNG file
                        print(f"Image downloaded and saved: {filename}.png")
                    else:
                        print(f"Failed to download image from '{url}'")
                except Exception as e:
                    print(f"Error downloading image from '{url}': {e}")

download_and_save_images(folder_path)
