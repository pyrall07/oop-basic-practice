from repositories.memory_repository import MemoryVideoRepository

def test_save_and_list_videos(sample_video):
    repo = MemoryVideoRepository()
    repo.save(sample_video)

    videos = repo.list_all()
    assert len(videos) == 1
    assert videos[0].video_id == "asd123"
    assert videos[0].title == "Belajar Dasar OOP Python"

def test_clear_videos(sample_video):
    repo = MemoryVideoRepository()
    repo.save(sample_video)
    repo.clear()

    assert len(repo.list_all()) == 0
