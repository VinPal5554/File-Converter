import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import threading
from moviepy import VideoFileClip

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

# Function to convert JPG to PNG
def convert_jpg_to_png():
    global file_path
    if not file_path:
        messagebox.showerror("Error", "No file selected!")
        return

    # Convert extension to lowercase for uniformity
    file_ext = os.path.splitext(file_path)[1].lower()

    if file_ext not in [".jpg", ".jpeg"]:
        messagebox.showerror("Error", "Please select a JPG file!")
        return

    try:
        image = Image.open(file_path)
        base, _ = os.path.splitext(file_path)
        output_file = base + ".png"  # Save as PNG
        image.save(output_file, "PNG")
        messagebox.showinfo("Success", f"Converted to {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Conversion failed: {str(e)}")

# Function to convert MP4 to GIF
def convert_mp4_to_gif():
    threading.Thread(target=_convert_mp4_to_gif_worker, daemon=True).start()

def _convert_mp4_to_gif_worker():
    global file_path
    if not file_path:
        messagebox.showerror("Error", "No file selected!")
        return

    file_ext = os.path.splitext(file_path)[1].lower()
    if file_ext != ".mp4":
        messagebox.showerror("Error", "Please select an MP4 file!")
        return

    try:
        # Optional: show feedback in the UI
        file_label.config(text="Converting to GIF...")

        # Try loading the video
        try:
            video = VideoFileClip(file_path)
            print("Video loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error loading video: {e}")
            return

        # Try subclipping (make sure it's in seconds, e.g., 0-5 seconds)
        try:
            sub_video = video.subclipped(0, 5)
            #    sub_video = sub_video.resize(0.5)  # Optional: Resize to 50%
            print("Subclip created successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error creating subclip: {e}")
            return

        base, _ = os.path.splitext(file_path)
        output_file = base + ".gif"
        sub_video.write_gif(output_file, fps=10)
        sub_video.close()
        video.close()

        # Notify user after success — must be called from the main thread
        root.after(0, lambda: messagebox.showinfo("Success", f"Converted to {output_file}"))
        root.after(0, lambda: file_label.config(text=f"Saved: {os.path.basename(output_file)}"))

    except Exception as e:
        root.after(0, lambda: messagebox.showerror("Error", f"GIF conversion failed: {str(e)}"))
        root.after(0, lambda: file_label.config(text="Conversion failed"))

# UI Elements
file_label = tk.Label(root, text="No file selected", font=("Arial", 12))
file_label.pack(pady=10)

select_btn = tk.Button(root, text="Select File", command=select_file)
select_btn.pack(pady=5)

# Image Conversion Buttons
tk.Label(root, text="Image Conversions", font=("Arial", 10, "bold")).pack()

convert_btn = tk.Button(root, text="Convert PNG to JPG", command=convert_png_to_jpg)
convert_btn.pack(pady=5)

convert_btn2 = tk.Button(root, text="Convert JPG to PNG", command=convert_jpg_to_png)
convert_btn2.pack(pady=5)

# Video Conversion Buttons
tk.Label(root, text="Video Conversions", font=("Arial", 10, "bold")).pack()

# MP4 to GIF conversion button
gif_convert_btn = tk.Button(root, text="Convert MP4 to GIF", command=convert_mp4_to_gif)
gif_convert_btn.pack(pady=5)

# Run the Tkinter loop
root.mainloop()