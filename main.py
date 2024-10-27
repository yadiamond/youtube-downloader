from pytube import YouTube
url  = input('enter url')
video_url = url
yt = YouTube(video_url)
stream = yt.streams.get_highest_resolution()
output_path = "path/to/output/directory/"
stream.download(output_path)