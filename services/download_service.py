from models.video import Video
from infrastructure.yt_dlp.client import YTDLPClient
from typing import Optional


class DownloadService:
    # service untuk mendownload video youtube
    def __init__(self, client:YTDLPClient):
        self.client = client

    def download(self, video: Video, path: Optional[str] = None) -> str:
        self.client.download(video.url, path)