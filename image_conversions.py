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

def convert_png_to_bmp(file_path):
    if not file_path.lower().endswith(".png"):
        raise ValueError("Please select a PNG file")
    image = Image.open(file_path)
    output_file = os.path.splitext(file_path)[0] + ".bmp"
    image.save(output_file, "BMP")
    return output_file

def convert_bmp_to_png(file_path):
    if not file_path.lower().endswith(".bmp"):
        raise ValueError("Please select a BMP file")
    image = Image.open(file_path)
    output_file = os.path.splitext(file_path)[0] + ".png"
    image.save(output_file, "PNG")
    return output_file