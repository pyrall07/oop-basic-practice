
def test_video_creation(sample_video):
    video = sample_video

    assert video.video_id == "asd123"
    assert video.title == "Belajar Dasar OOP Python"
    assert video.duration == 120
    assert video.url.startswith("https://")

def test_video_duration_in_minutes(sample_video):
    video = sample_video
    assert video.duration_minutes() == 2.0
       