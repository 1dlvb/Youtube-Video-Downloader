from pytube import YouTube


# Youtube video downloader
class YtDownloader:
    def initialisation(self, link):
        self.yt_video = YouTube(link)

    def title(self):
        return self.yt_video.title

    def video_id(self):
        return self.yt_video.video_id

    def download(self):
        return self.yt_video.streams.first().download()


def preview_image(id):
    return 'https://img.youtube.com/vi/{0}/0.jpg'.format(str(id))


# link = input()
#
# yt = YtDownloader()
# yt.initialisation(link)
#
# video_id = yt.video_id()
# yt.title()
# print(video_id)
# print(video_image(video_id))
