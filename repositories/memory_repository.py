from models.video import Video
from typing import List

class MemoryVideoRepository:
    # Simpan video di memory sementara
    def __init__(self):
        self._videos: List[Video] = []

    def save(self, video: Video):
        # simpan video baru
        self._videos.append(video)

    def list_all(self) -> List[Video]:
        # ambil semua video yang tersimpan
        return self._videos
    
    def clear(self):
        # Hapus semua video
        self._videos.clear()