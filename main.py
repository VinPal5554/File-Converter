import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import threading
from image_conversions import convert_png_to_jpg, convert_jpg_to_png
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

def handle_png_to_jpg():
    global file_path
    if not file_path:
        messagebox.showerror("Error", "No file selected!")
        return
    try:
        output = convert_png_to_jpg(file_path)
        messagebox.showinfo("Success", f"Converted to {output}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def handle_jpg_to_png():
    global file_path
    if not file_path:
        messagebox.showerror("Error", "No file selected!")
        return
    try:
        output = convert_jpg_to_png(file_path)
        messagebox.showinfo("Success", f"Converted to {output}")
    except Exception as e:
        messagebox.showerror("Error", str(e))




def handle_mp4_to_gif():
    global file_path
    if not file_path:
        messagebox.showerror("Error", "No file selected!")
        return
    try:
        file_label.config(text="Converting to GIF...")
        output = convert_mp4_to_gif(file_path, start=0, end=5, fps=10)
        messagebox.showinfo("Success", f"Converted to {output}")
        file_label.config(text=f"Saved: {os.path.basename(output)}")
    except Exception as e:
        messagebox.showerror("Error", str(e))
        file_label.config(text="Conversion failed")

def handle_gif_to_mp4():
    global file_path
    if not file_path:
        messagebox.showerror("Error", "No file selected!")
        return
    try:
        file_label.config(text="Converting to MP4...")
        output = convert_gif_to_mp4(file_path)
        messagebox.showinfo("Success", f"Converted to {output}")
        file_label.config(text=f"Saved: {os.path.basename(output)}")
    except Exception as e:
        messagebox.showerror("Error", str(e))
        file_label.config(text="Conversion failed")



def handle_mp4_to_avi():
    global file_path
    if not file_path:
        messagebox.showerror("Error", "No file selected!")
        return
    try:
        file_label.config(text="Converting to AVI...")

        codec = codec_var.get()

        output = convert_mp4_to_avi(file_path, start=0, end=5, fps=10, codec=codec)
        messagebox.showinfo("Success", f"Converted to {output}")
        file_label.config(text=f"Saved: {os.path.basename(output)}")
    except Exception as e:
        messagebox.showerror("Error", str(e))
        file_label.config(text="Conversion failed")

def handle_avi_to_mp4():
    global file_path
    if not file_path:
        messagebox.showerror("Error", "No file selected!")
        return
    try:
        file_label.config(text="Converting to MP4...")
        output = convert_avi_to_mp4(file_path, start=0, end=5, fps=10)
        messagebox.showinfo("Success", f"Converted to {output}")
        file_label.config(text=f"Saved: {os.path.basename(output)}")
    except Exception as e:
        messagebox.showerror("Error", str(e))
        file_label.config(text="Conversion failed")



def handle_pdf_to_txt():
    global file_path
    if not file_path:
        messagebox.showerror("Error", "No file selected!")
        return
    try:
        file_label.config(text="Converting to TXT...")
        output = convert_pdf_to_txt(file_path)
        messagebox.showinfo("Success", f"Converted to {output}")
        file_label.config(text=f"Saved: {os.path.basename(output)}")
    except Exception as e:
        messagebox.showerror("Error", str(e))
        file_label.config(text="Conversion failed")

def handle_docx_to_pdf():
    global file_path
    if not file_path:
        messagebox.showerror("Error", "No file selected!")
        return
    try:
        file_label.config(text="Converting to PDF...")
        output = convert_docx_to_pdf(file_path)
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

convert_btn = ttk.Button(root, text="Convert PNG to JPG", command=lambda: run_in_thread(handle_png_to_jpg))
convert_btn.pack(pady=5)

convert_btn2 = ttk.Button(root, text="Convert JPG to PNG", command=lambda: run_in_thread(handle_jpg_to_png))
convert_btn2.pack(pady=5)

# Video Conversion Buttons
tk.Label(root, text="Video Conversions", font=("Arial", 10, "bold")).pack()

# Codec Selection Dropdown
tk.Label(root, text="Select Codec", font=("Arial", 10)).pack()
codec_var = tk.StringVar(value="mpeg4")  # default
codec_options = ["mpeg4", "libx264", "png", "rawvideo"]
codec_menu = tk.OptionMenu(root, codec_var, *codec_options)
codec_menu.pack(pady=5)


gif_convert_btn = ttk.Button(root, text="Convert MP4 to GIF", command=lambda: run_in_thread(handle_mp4_to_gif))
gif_convert_btn.pack(pady=5)

gif_to_mp4_btn = ttk.Button(root, text="Convert GIF to MP4", command=lambda: run_in_thread(handle_gif_to_mp4))
gif_to_mp4_btn.pack(pady=5)

mp4_to_avi_btn = ttk.Button(root, text="Convert MP4 to AVI", command=lambda: run_in_thread(handle_mp4_to_avi))
mp4_to_avi_btn.pack(pady=5)

avi_to_mp4_btn = ttk.Button(root, text="Convert AVI to MP4", command=lambda: run_in_thread(handle_avi_to_mp4))
avi_to_mp4_btn.pack(pady=5)

# Document Conversion Buttons
tk.Label(root, text="Document Conversions", font=("Arial", 10, "bold")).pack()

pdf_to_txt_btn = ttk.Button(root, text="Convert PDF to TXT", command=handle_pdf_to_txt)
pdf_to_txt_btn.pack(pady=5)



# Run the Tkinter loop
root.mainloop()