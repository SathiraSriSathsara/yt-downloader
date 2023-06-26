import tkinter
import customtkinter
import yt_dlp
import json
import sys
import os  

print("////////// Developed by Sathira Sri Sathra //////////")

def startDownload():
    try:
        ytLink = link.get()
        options = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([ytLink])
        print("Your Video Has Been Downloaded.")
    except Exception as e:
        print("An error occurred:", str(e))
    finishLable.configure(text="Downloaded")

customtkinter.set_appearance_mode("dark")

# Set the base path to the directory where the script is located
BASE_PATH = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# Add the themes folder to the system path
sys.path.append(os.path.join(BASE_PATH, 'assets', 'themes'))

# Load theme from JSON file
theme_file = os.path.join(BASE_PATH, 'assets', 'themes', 'theme.json')
with open(theme_file) as f:
    theme_data = json.load(f)
    theme_name = theme_data["default_color_theme"]
    customtkinter.set_default_color_theme(theme_name)

app = customtkinter.CTk()
app.geometry("800x600")
app.title("Youtube Video Downloader Beta Version 01")

title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=550, height=40, textvariable=url_var)
link.pack()

finishLable = customtkinter.CTkLabel(app, text="")

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

title = customtkinter.CTkLabel(app, text="Developed By Sathira Sri Sathsara")
title.pack(padx=10, pady=10)

app.mainloop()
