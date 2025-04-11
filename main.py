import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image


# Initialize Tkinter
root = tk.Tk()
root.title("Universal File Converter")
root.geometry("500x400")

# Global variables
file_path = ""

# Function to select a file
def select_file():
    global file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        file_label.config(text=f"Selected: {os.path.basename(file_path)}")

# Function to convert PNG to JPG
def convert_png_to_jpg():
    global file_path
    if not file_path:
        messagebox.showerror("Error", "No file selected!")
        return

    # Convert extension to lowercase for uniformity
    file_ext = os.path.splitext(file_path)[1].lower()

    if file_ext != ".png":
        messagebox.showerror("Error", "Please select a PNG file!")
        return

    try:
        image = Image.open(file_path)
        base, _ = os.path.splitext(file_path)  # Split filename and extension
        output_file = base + ".jpg"  # Save as JPG
        rgb_image = image.convert("RGB")  # Convert to RGB mode
        rgb_image.save(output_file, "JPEG")
        messagebox.showinfo("Success", f"Converted to {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Conversion failed: {str(e)}")


# UI Elements
file_label = tk.Label(root, text="No file selected", font=("Arial", 12))
file_label.pack(pady=10)

select_btn = tk.Button(root, text="Select File", command=select_file)
select_btn.pack(pady=5)

# Image Conversion Buttons
tk.Label(root, text="Image Conversions", font=("Arial", 10, "bold")).pack()
convert_btn = tk.Button(root, text="Convert PNG to JPG", command=convert_png_to_jpg)
convert_btn.pack(pady=5)


# Run the Tkinter loop
root.mainloop()