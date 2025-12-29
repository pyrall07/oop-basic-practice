from yt_dlp import YoutubeDL
from .options import SEARCH_OPTIONS, DOWNLOAD_OPTIONS

class YTDLPClient:

    def search(self, keyword: str, max_results: int = 5):
        with YoutubeDL(SEARCH_OPTIONS) as ydl:
            query = f"ytsearch{max_results}:{keyword}"
            info = ydl.extract_info(query, download=False)
            return info.get("entries", [])
        
    def download(self, url: str, path: str = None) -> None:
        options = DOWNLOAD_OPTIONS.copy()
        if path:
            options["outtmpl"] = f"{path}/%(title)s.%(ext)s"
            
        with YoutubeDL(options) as ydl:
            ydl.download([url])