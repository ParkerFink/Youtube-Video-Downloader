from pytube import YouTube
from pytube import Playlist
from cmd import Cmd

import os



version = '1.3'




class Terminal(Cmd):

    prompt = "v" + version + ">"




    def do_download(self, url):
        yt = YouTube(url).streams.get_highest_resolution().download('videos/')


    def help_download(self):
        print("It is used to download a single video at a time.")
        print("EX: download https://www.youtube.com/watch?v=DYcLFHgVCn0")


    def do_playlist(self, url):
        playlist = Playlist(url)
        playlistName = playlist.title
        for video in playlist.videos:
            video.streams.get_highest_resolution().download('videos/' + playlistName + '/')

    def help_playlist(self):
        print("Downloads full playlist into videos folder")
        print("EX: playlist https://www.youtube.com/watch?v=-C_rvt0SwLE&list=PLaKNAbgyxAh0VD54wrttxVnxC7fYDchf2")

    def do_list(self, path):
        list = os.listdir('videos/' + path)
        for video in list:
            print(video)

    def help_list(self):
        print("lists all videos and or playlists in the videos folder")
        print("EX: list")
        print("EX2: list musicplaylist")

    def do_open(self, video):
       cwd = os.getcwd()
       path = cwd + "/videos/"
       os.startfile(path + "/" + video)

    def help_open(self):
        print("Allows you to play a video from the terminal")
        print("EX: open")
        print("Which allows you to open the videos folder")
        print("EX: open video.mp4")
        print("Which allows you to play specific video from the terminal")



    def do_clear(self, blank):
        os.system('cls')


    def help_clear(self):
        print("Clears all text in the terminal.")


    def do_exit(self, blank):
        exit()

    def help_exit(self):
        print("Closes Youtube Video Downloader.")
    

Terminal().cmdloop()
