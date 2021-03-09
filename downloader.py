from pytube import YouTube
import os


# Youtube video downloader
class YtDownloader:
    def initialize(self, link):
        self.yt_video = YouTube(link)

    def title(self):
        return self.yt_video.title

    def video_id(self):
        return self.yt_video.video_id

    def download(self):
        """download file
           get byte data
           delete file"""

        self.download_video = self.yt_video.streams.first().download(filename='downloadedVideo')
        path = os.path.normpath(self.download_video)

        try:
            with open(path, 'rb') as f:
                # get byte data of a file
                byteData = f.read()
                print(type(byteData))
                print(len(byteData))
                f.close()
                os.remove(path)
                return byteData

        except Exception as e:
            return "Error"

    def filename(self):
        return self.yt_video.title


def preview_image(id):
    return 'https://img.youtube.com/vi/{0}/0.jpg'.format(str(id))

