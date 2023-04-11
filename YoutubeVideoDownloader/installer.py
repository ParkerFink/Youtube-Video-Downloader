import os
from pyshortcuts import make_shortcut

os.system("pip install pytube")
os.system("pip install pyshortcuts")

cwd = os.getcwd()

make_shortcut(cwd + "/YoutubeDownloader.py/" , name="Video Downloader")

