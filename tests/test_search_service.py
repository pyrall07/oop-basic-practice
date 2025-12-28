import pytest
from services.search_service import SearchService
from repositories.memory_repository import MemoryVideoRepository
    
def test_search_service_with_dummy_client(dummy_client):
    # test search normal dengan dummy client
    repo = MemoryVideoRepository()
    service = SearchService(repo, dummy_client)

    results = service.search("Python", max_results=3)

    assert len(results) == 3
    assert len(repo.list_all()) == 3

    for i, video in enumerate(results, start= 1):
        assert video.title == f"Python Video {i}"
        assert video.url.startswith("https://")    


def test_repository_gets_saved_videos(dummy_client):
    repo = MemoryVideoRepository()
    service = SearchService(repo, dummy_client)

    service.search("Python", max_results=2)

    all_videos = repo.list_all()
    assert len(all_videos) == 2
    # cek judul video
    assert all_videos[0].title == "Python Video 1"
    assert all_videos[1].title == "Python Video 2"

def test_video_attributes_from_search_service(dummy_client):
    # pastikan hasil search bisa diakses sebagai object video
    repo = MemoryVideoRepository()
    service = SearchService(repo, dummy_client)

    videos = service.search("Python", max_results=1)
    video = videos[0]

    assert video.video_id == "1"
    assert video.title == "Python Video 1"
    assert video.duration == 130
    assert video.url == "https://youtube.com/watch?v=1"


    
