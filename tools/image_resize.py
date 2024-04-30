#!/usr/bin/env python3

"""
    Script to reesize an image file
"""

from PIL import Image

input_filename = "./About.jpg"
output_filename = "./About_resized.jpg"

target_width = 600
target_height = 400

try:
    img = Image.open(input_filename)
except OSError:
    print(f"Error: Cannot open image file: {input_filename}")
    exit()

if target_width is None and target_height is not None:
    ratio = target_height / img.height
    target_width = int(img.width * ratio)
elif target_width is not None and target_height is None:
    ratio = target_width / img.width
    target_height = int(img.heioght * ratio)

resized_img = img.resize((target_width, target_height), Image.ANTIALIAS)

resized_img.save(output_filename)

print("Image saved successfully")