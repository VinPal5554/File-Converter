import os
from PIL import Image

def convert_png_to_jpg(file_path):
    if not file_path.lower().endswith(".png"):
        raise ValueError("Not a PNG file")
    image = Image.open(file_path)
    base, _ = os.path.splitext(file_path)
    output_file = base + ".jpg"
    image.convert("RGB").save(output_file, "JPEG")
    return output_file

def convert_jpg_to_png(file_path):
    if not file_path.lower().endswith((".jpg", ".jpeg")):
        raise ValueError("Not a JPG file")
    image = Image.open(file_path)
    base, _ = os.path.splitext(file_path)
    output_file = base + ".png"
    image.save(output_file, "PNG")
    return output_file