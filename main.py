import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import threading
from image_conversions import convert_png_to_jpg, convert_jpg_to_png, convert_png_to_bmp, convert_bmp_to_png
from video_conversions import convert_mp4_to_gif, convert_gif_to_mp4, convert_avi_to_mp4, convert_mp4_to_avi
from document_conversions import convert_pdf_to_txt
from ttkthemes import ThemedTk

# Initialize Tkinter
root = ThemedTk()
root.title("Universal File Converter")
root.geometry("600x600")
root.get_themes()
root.set_theme("radiance")

# Global variables
file_path = ""

# Function to select a file
def select_file():
    global file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        file_label.config(text=f"Selected: {os.path.basename(file_path)}")

def run_in_thread(func):
    threading.Thread(target=func, daemon=True).start()

def handle_conversion(conversion_function, file_types=None, **kwargs):
    global file_path
    if not file_path:
        messagebox.showerror("Error", "No file selected!")
        return

    try:
        file_label.config(text="Converting...")
        output = conversion_function(file_path, **kwargs)
        messagebox.showinfo("Success", f"Converted to {output}")
        file_label.config(text=f"Saved: {os.path.basename(output)}")
    except Exception as e:
        messagebox.showerror("Error", str(e))
        file_label.config(text="Conversion failed")

# UI Elements
file_label = tk.Label(root, text="No file selected", font=("Helvetica", 14, "bold"))
file_label.pack(pady=10)

select_btn = tk.Button(root, text="Select File", command=select_file)
select_btn.pack(pady=5)

# Image Conversion Buttons
tk.Label(root, text="Image Conversions", font=("Arial", 10, "bold")).pack()

convert_btn = ttk.Button(root, text="Convert PNG to JPG", command=lambda: handle_conversion(convert_png_to_jpg))
convert_btn.pack(pady=5)

convert_btn2 = ttk.Button(root, text="Convert JPG to PNG", command=lambda: handle_conversion(convert_jpg_to_png))
convert_btn2.pack(pady=5)

convert_btn3 = ttk.Button(root, text="Convert PNG to BMP", command=lambda: handle_conversion(convert_png_to_bmp))
convert_btn3.pack(pady=5)

convert_btn4 = ttk.Button(root, text="Convert BMP to PNG", command=lambda: handle_conversion(convert_bmp_to_png))
convert_btn4.pack(pady=5)

# Video Conversion Buttons
tk.Label(root, text="Video Conversions", font=("Arial", 10, "bold")).pack()

# Codec Selection Dropdown
tk.Label(root, text="Select Codec", font=("Arial", 10)).pack()
codec_var = tk.StringVar(value="mpeg4")  # default
codec_options = ["mpeg4", "libx264", "png", "rawvideo"]
codec_menu = tk.OptionMenu(root, codec_var, *codec_options)
codec_menu.pack(pady=5)


gif_convert_btn = ttk.Button(root, text="Convert MP4 to GIF", command=lambda: handle_conversion(convert_mp4_to_gif))
gif_convert_btn.pack(pady=5)

gif_to_mp4_btn = ttk.Button(root, text="Convert GIF to MP4", command=lambda: handle_conversion(convert_gif_to_mp4))
gif_to_mp4_btn.pack(pady=5)

mp4_to_avi_btn = ttk.Button(root, text="Convert MP4 to AVI", command=lambda: handle_conversion(convert_mp4_to_avi))
mp4_to_avi_btn.pack(pady=5)

avi_to_mp4_btn = ttk.Button(root, text="Convert AVI to MP4", command=lambda: handle_conversion(convert_avi_to_mp4))
avi_to_mp4_btn.pack(pady=5)

# Document Conversion Buttons
tk.Label(root, text="Document Conversions", font=("Arial", 10, "bold")).pack()

pdf_to_txt_btn = ttk.Button(root, text="Convert PDF to TXT", command=lambda: handle_conversion(convert_pdf_to_txt))
pdf_to_txt_btn.pack(pady=5)

# Audio Conversion Buttons
tk.Label(root, text="Audio Conversions", font=("Arial", 10, "bold")).pack()



# Run the Tkinter loop
root.mainloop()