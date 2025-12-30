import sys

class DownloadProgress:
    def __init__(self):
        self.last_msg = ""

    def hook(self, d):
        if d["status"] == "downloading":
            downloaded = d.get("downloaded_bytes", 0) / 1024 / 1024
            speed = d.get("speed")
            speed = f"{speed/1024/1024:.2f} MB/s" if speed else "..."

            msg = f"\r⬇ Downloading: {downloaded:.2f} MB | {speed}"
            if msg != self.last_msg:
                sys.stdout.write(msg)
                sys.stdout.flush()
                self.last_msg = msg

        elif d["status"] == "finished":
            sys.stdout.write("\n✅ Download selesai\n")
