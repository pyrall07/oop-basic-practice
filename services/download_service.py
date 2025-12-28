from models.video import Video
from yt_dlp import YoutubeDL
from typing import Optional


class DownloadService:
    # service untuk mendownload video youtube

    def __init__(self, ydl_opts:Optional[dict] = None):
        self.ydl_opts = ydl_opts or {"formats":"best", "quiet": False}


    def download(self, video: Video, path: Optional[str] = None) -> str:
        opts = self.ydl_opts.copy()
        if path:
            opts["outtmpl"] = f"{path}/%(title)s.%(ext)s"

        
        with YoutubeDL(opts) as ydl:
            ydl.download([video.url])
            
        return f"{path}/{video.title}.mp4" if path else f"{video.title}.mp4"