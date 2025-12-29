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
    "verbose": True,
    "quiet": True,
    "no_warnings": True,
    "extractor_args": {
        "youtube": {
            "player_client": "web_safari"
        }
    },
}
