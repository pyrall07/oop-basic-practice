class Video:
    def __init__(self, video_id, title, duration, url):
        self.video_id = video_id
        self.title = title
        self.duration = duration
        self.url = url

    def __repr__(self):
        return f"<Video {self.title} ({self.duration})>"
    
    def duration_minutes(self):
        # Mengembalikan durasi video dalam menit
        return round(self.duration / 60, 2)
    