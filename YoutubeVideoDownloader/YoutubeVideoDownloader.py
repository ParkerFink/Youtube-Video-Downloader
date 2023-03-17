from pytube import YouTube

from cmd import Cmd


class Terminal(Cmd):

    def do_download(self, url):
        yt = YouTube(url).streams.get_highestResolution().download('videos/')


Terminal().cmdloop()
