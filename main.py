import os
import tkinter as tk
from tkinter import filedialog, messagebox

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


# UI Elements
file_label = tk.Label(root, text="No file selected", font=("Arial", 12))
file_label.pack(pady=10)

select_btn = tk.Button(root, text="Select File", command=select_file)
select_btn.pack(pady=5)

# Image Conversion Buttons
tk.Label(root, text="Image Conversions", font=("Arial", 10, "bold")).pack()


# Run the Tkinter loop
root.mainloop()