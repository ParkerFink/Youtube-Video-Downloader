from pytube import YouTube

from cmd import Cmd


import os



class Terminal(Cmd):

    def do_download(self, url):
        yt = YouTube(url).streams.get_highest_resolution().download('videos/')


    def help_download(self):
        print("It is used to download a single video at a time.")
        print("EX: download https://www.youtube.com/watch?v=DYcLFHgVCn0")



    def do_clear(self, blank):
        os.system('cls')


    def help_clear(self):
        print("Clears all text in the terminal.")


    def do_exit(self, blank):
        exit()

    def help_exit(self):
        print("Closes Youtube Video Downloader.")
    

Terminal().cmdloop()
