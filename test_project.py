import pytest
from project import search_videos, list_videos, download_single_video
from models.video import Video
from repositories.memory_repository import MemoryVideoRepository
from services.search_service import SearchService
from services.download_service import DownloadService

# ===== FIXTURE MINIMAL KHUSUS test_project.py =====

@pytest.fixture
def repo():
    return MemoryVideoRepository()

@pytest.fixture
def sample_video():
    return Video(
        video_id="123",
        title="Test Video",
        duration=120,
        url="http://example.com"
    )

class DummyClient:
    def search(self, keyword, max_results=5):
        return [
            {
                "id": "1",
                "title": "Dummy Video",
                "duration": 100,
                "webpage_url": "http://example.com"
            }
        ]

    def download(self, url, path=None):
        pass

@pytest.fixture
def search_service(repo):
    return SearchService(repo, DummyClient())

@pytest.fixture
def download_service():
    return DownloadService(DummyClient())

# ===== TEST WAJIB CS50P =====

def test_list_videos_empty(repo):
    assert list_videos(repo) == []

def test_search_videos(search_service):
    results = search_videos(search_service, "python", 1)
    assert len(results) == 1
    assert results[0].title == "Dummy Video"

def test_download_single_video(download_service, sample_video):
    title = download_single_video(download_service, sample_video)
    assert title == "Test Video"
