import pytest
from models.video import Video
from services.download_service import DownloadService
from services.search_service import SearchService
from repositories.memory_repository import MemoryVideoRepository

class DummyClient:
    """Client dummy untuk SearchService"""
    def search(self, keyword: str, max_results: int = 5):
        """Generate list dummy video sesuai max_results"""
        return [
            {
                "id": f"{i}",
                "title": f"{keyword} Video {i}",
                "duration": 120 + i * 10,
                "webpage_url": f"https://youtube.com/watch?v={i}"
            }
            for i in range(1, max_results + 1)
        ]

@pytest.fixture
def dummy_client():
    return DummyClient()

@pytest.fixture
def download_service():
    return DownloadService()

@pytest.fixture
def repo():
    return MemoryVideoRepository()

@pytest.fixture
def search_service(repo, dummy_client):
    return SearchService(repo, dummy_client)

@pytest.fixture
def sample_video():
    # Return satu object Video yang bisa dipakai di banyak test
    return Video(
        video_id="asd123",
        title="Belajar Dasar OOP Python",
        duration=120,
        url="https://youtube.com/watch?v=asd123"
    )