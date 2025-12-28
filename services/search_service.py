from models.video import Video
from repositories.memory_repository import MemoryVideoRepository
from utils.yt_dlp_client import YTDLPClient
from typing import List

class SearchService:
    # service untuk mencari video dan menyimpannya di repository

    def __init__(self, repository: MemoryVideoRepository, client: YTDLPClient = None):
        self.repository = repository
        self.client = client or YTDLPClient()

    def search(self, keyword: str, max_results: int = 5) -> List[Video]:
        # cari video via yt-dlp dan simpan di repository
        raw_results = self.client.search(keyword, max_results= max_results)
        videos = []

        for entry in raw_results:
            video = Video(
                video_id=entry.get("id"),
                title=entry.get("title",),
                duration=entry.get("duration", 0),
                url=entry.get("webpage_url")
            )
            self.repository.save(video)
            videos.append(video)
        

        return videos