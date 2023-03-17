from pytube import YouTube



url = str(input("video url: "))

yt = YouTube(url).streams.get_highestResolution().donwload()
