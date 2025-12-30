from .progress import DownloadProgress

progress = DownloadProgress()

SEARCH_OPTIONS = {
    "quiet": True,
    "no_warnings": True,
    "extract_flat": False,
    "force_generic_extractor": True,
    "skip_download": True,
    "format": "bestaudio/best",
}

DOWNLOAD_OPTIONS = {
    "format": "best[ext=mp4]/bestvideo+bestaudio/best",
    "merge_output_format": "mp4",
    "outtmpl": "%(title)s.%(ext)s",

    "noplaylist": True,
    "progress_hooks": [progress.hook],

    # 🔇 Matikan semua noise
    "quiet": True,
    "no_warnings": True,
    "logtostderr": False,
    "noprogress": True,
    "verbose": False,

    # 🧩 Hindari client bermasalah
    "extractor_args": {
        "youtube": {
            "player_client": ["android"]
        }
    },

    # ⚡ Performa
    "concurrent_fragment_downloads": 8,
    "fragment_retries": 50,
    "retries": 10,
}
