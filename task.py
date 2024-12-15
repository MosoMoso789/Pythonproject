import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_video(resolution):
    link = url_entry.get()
    if not link:
        messagebox.showerror("Error", "Please paste a YouTube link!")
        return
    
    try:
        yt = YouTube(link)
        if resolution == "high":
            stream = yt.streams.get_highest_resolution()
        elif resolution == "low":
            stream = yt.streams.filter(progressive=True, file_extension='mp4').get_lowest_resolution()
        elif resolution == "audio":
            stream = yt.streams.filter(only_audio=True).first()
        else:
            messagebox.showerror("Error", "Invalid option!")
            return

        messagebox.showinfo("Downloading", f"Downloading {stream.title}...")
        stream.download()
        messagebox.showinfo("Success", "Download complete!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create GUI
app = tk.Tk()
app.title("YouTube Downloader")

tk.Label(app, text="Paste Link Here:").pack(pady=5)
url_entry = tk.Entry(app, width=50)
url_entry.pack(pady=5)

tk.Button(app, text="High Resolution", command=lambda: download_video("high")).pack(pady=5)
tk.Button(app, text="Low Resolution", command=lambda: download_video("low")).pack(pady=5)
tk.Button(app, text="Audio Only", command=lambda: download_video("audio")).pack(pady=5)

app.mainloop()