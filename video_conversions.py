import os
from moviepy import VideoFileClip

def convert_mp4_to_gif(file_path, start=0, end=5, fps=10):
    if not file_path.lower().endswith(".mp4"):
        raise ValueError("Not an MP4 file")
    video = VideoFileClip(file_path).subclipped(start, end)
    base, _ = os.path.splitext(file_path)
    output_file = base + ".gif"
    video.write_gif(output_file, fps=fps)
    video.close()
    return output_file

def convert_gif_to_mp4(file_path):
    if not file_path.lower().endswith(".gif"):
        raise ValueError("Not a GIF file")
    video = VideoFileClip(file_path)
    base, _ = os.path.splitext(file_path)
    output_file = base + "_converted.mp4"
    video.write_videofile(output_file, codec="libx264")
    video.close()
    return output_file