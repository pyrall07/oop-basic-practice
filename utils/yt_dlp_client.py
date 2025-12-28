from yt_dlp import YoutubeDL
from typing import List, Dict

class YTDLPClient:
    # wrapper untuk yt-dlp

    def __init__(self):
        self.ydl_opts = {"quiet": True, "skip_download": True}

    def search(self, keyword: str, max_results: int = 5) -> List[Dict]:
        # cari video di youtube, return list of metadata dict
        query = f"ytsearch{max_results}:{keyword}"
        with YoutubeDL(self.ydl_opts) as ydl:
            result = ydl.extract_info(query, download=False)
            return result.get("entries", [])