import unreal as ue
from PIL import Image
import os

editor_util = ue.EditorUtilityLibrary()
system_lib = ue.SystemLibrary()
editor_asset_library = ue.EditorAssetLibrary()


map_height = 1024
map_width = 1024

# Create an empty pixel data array (list)
pixel_data = []

for y in range(map_width) :
    for x in range(map_height):
        #red = int(((x + y) / (map_width + map_height)) * 255) // bitmap red for one channel
        red = int((x/ map_height)*255)
        green=int((y/map_width)*255)
        blue=int(((x+y)/(map_width+map_width))*255)
        alpha=255

        pixel_data.extend([red,green,blue,alpha])


# Convert the list of pixel values to bytes
pixel_bytes = bytes(pixel_data)

# Create a PIL Image object from the pixel data
pil_image = Image.frombytes("RGBA", (map_width, map_height), pixel_bytes)

# Get the project's content directory
content_dir = ue.SystemLibrary.get_project_content_directory()

# Define the image file path (adjust the path as needed)
image_path = os.path.join(content_dir, "GeneratedImage.png")

# Save the image
pil_image.save(image_path)

# Notify the user that the image has been saved
editor_util.message_dialog("Image saved: " + image_path)