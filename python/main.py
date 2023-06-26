import tkinter as tk
import yt_dlp
import threading
from tkinter import ttk
import customtkinter

print("////////// Developed by Sathira Sri Sathra //////////")


def startDownload():
    try:
        ytLink = link.get()
        selected_quality = quality_selection.get()
        options = {
            'format': selected_quality,
            'outtmpl': '%(title)s.%(ext)s',
            'progress_hooks': [updateProgress],
        }
        # Create a new thread for downloading the video
        download_thread = threading.Thread(target=downloadVideo, args=(ytLink, options))
        download_thread.start()
    except Exception as e:
        print("An error occurred:", str(e))
    finishLable.configure(text="Downloaded")


def downloadVideo(ytLink, options):
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([ytLink])
    print("Your Video Has Been Downloaded.")


def updateProgress(progress):
    if progress['status'] == 'downloading':
        total_bytes = progress.get('total_bytes', None)
        downloaded_bytes = progress.get('downloaded_bytes', None)
        if total_bytes and downloaded_bytes:
            percent = downloaded_bytes * 100 / total_bytes
            pPercentage.configure(text=f"{percent:.2f}%")
            progressBar['value'] = percent


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("800x600")
root.title("Youtube Video Downloader Beta Version 01")
root.resizable(False, False)  # Disable window maximize option

title = customtkinter.CTkLabel(root, text="Insert a YouTube link")
title.pack(padx=10, pady=10)

link = customtkinter.CTkEntry(root, width=550)
link.pack()

quality_label = customtkinter.CTkLabel(root, text="Video Quality:")
quality_label.pack(padx=10, pady=5)

quality_options = ["best", "worst", "bestvideo", "worstvideo", "bestaudio", "worstaudio"]
quality_selection = tk.StringVar()
quality_selection.set("best")  # Set default quality

frame_1 = customtkinter.CTkFrame(master=root)
frame_1.pack(pady=5, padx=5,)

optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=quality_options)
optionmenu_1.place(relx=0.5, rely=0.5, anchor="center")

finishLable = customtkinter.CTkLabel(root, text="")
finishLable.pack()

pPercentage = customtkinter.CTkLabel(root, text="0%")
pPercentage.pack()

progressBar = ttk.Progressbar(root, mode='determinate', length=400)
progressBar.pack(padx=10, pady=10)

download = customtkinter.CTkButton(root, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

title = customtkinter.CTkLabel(root, text="Developed By Sathira Sri Sathsara")
title.pack(padx=10, pady=180)

root.mainloop()
