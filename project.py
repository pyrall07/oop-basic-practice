from repositories.memory_repository import MemoryVideoRepository
from services.search_service import SearchService
from services.download_service import DownloadService
from infrastructure.yt_dlp.client import YTDLPClient
from utils.cli_helper import clear_screen, pause

from tqdm import tqdm
import time
import threading

# ================= PROGRESS BAR =================

def staged_progress(label: str, stop_event: threading.Event):
    """Progress bar 3 tahap:
    - cepat ke 80%
    - tahan di 80% sampai proses selesai
    - lanjut ke 100%
    """
    with tqdm(total=100, desc=label, ncols=80) as pbar:
        while pbar.n < 80:
            pbar.update(1)
            time.sleep(0.02)

        while not stop_event.is_set():
            time.sleep(0.1)

        while pbar.n < 100:
            pbar.update(1)
            time.sleep(0.01)

# ================= UTIL =================

def print_videos(videos):
    for idx, video in enumerate(videos, start=1):
        print(f"{idx}. {video.title} ({video.duration}s)")

# ====== FUNGSI WAJIB CS50P (TOP LEVEL) ======

def search_videos(search_service, keyword: str, max_results: int = 5):
    return search_service.search(keyword, max_results=max_results)

def list_videos(repo):
    return repo.list_all()

def download_single_video(download_service, video, path=None):
    download_service.download(video, path)
    return video.title

# ==============================================

def _search_worker(container, search_service, keyword, max_results, stop_event):
    """Thread worker untuk search"""
    container["results"] = search_videos(
        search_service, keyword, max_results
    )
    stop_event.set()

def main(repo=None, search_service=None, download_service=None, interactive=True):
    # ===== Dependency Injection =====
    if repo is None:
        repo = MemoryVideoRepository()

    if search_service is None or download_service is None:
        client = YTDLPClient()
        search_service = search_service or SearchService(repo, client)
        download_service = download_service or DownloadService(client)
    # ===============================

    while True:
        clear_screen()
        print("\n=== YouTube Mini OOP CLI ===")
        print("1. Search video")
        print("2. List saved videos")
        print("3. Download video")
        print("4. Clear repository")
        print("5. Exit")

        choice = input("Pilih menu (1-5): ").strip()

        # ========== SEARCH ==========
        if choice == "1":
            keyword = input("Masukkan keyword: ").strip()
            if not keyword:
                continue

            max_results = input("Max result (default 5): ").strip()
            max_results = int(max_results) if max_results.isdigit() else 5

            stop_event = threading.Event()
            result_container = {}

            search_thread = threading.Thread(
                target=_search_worker,
                args=(result_container, search_service, keyword, max_results, stop_event)
            )

            progress_thread = threading.Thread(
                target=staged_progress,
                args=("Searching", stop_event)
            )

            search_thread.start()
            progress_thread.start()

            search_thread.join()
            progress_thread.join()

            results = result_container.get("results", [])
            print()
            print_videos(results)
            pause(interactive)

        # ========== LIST ==========
        elif choice == "2":
            videos = list_videos(repo)
            if not videos:
                print("Repository kosong.")
            else:
                print("\nVideo tersimpan:")
                print_videos(videos)
            pause(interactive)

        # ========== DOWNLOAD ==========
        elif choice == "3":
            videos = list_videos(repo)
            if not videos:
                print("Tidak ada video untuk didownload.")
                pause(interactive)
                continue

            print("\nVideo Tersedia:")
            print_videos(videos)
            print("0. Kembali ke menu")

            raw = input("Masukkan nomor video (pisahkan koma): ").strip()
            if raw == "0" or not raw:
                continue

            indices = [int(i) for i in raw.split(",") if i.strip().isdigit()]
            path = input("Folder tujuan (default current): ").strip() or None

            for i in indices:
                if 1 <= i <= len(videos):
                    print(f"\nDownloading: {videos[i-1].title}")
                    stop_event = threading.Event()

                    progress_thread = threading.Thread(
                        target=staged_progress,
                        args=("Downloading", stop_event)
                    )

                    progress_thread.start()
                    title = download_single_video(download_service, videos[i-1], path)
                    stop_event.set()
                    progress_thread.join()

                    print(f"Video berhasil didownload: {title}")

            pause(interactive)

        # ========== CLEAR ==========
        elif choice == "4":
            if input("Yakin? (y/n): ").lower() == "y":
                repo.clear()
                print("Repository berhasil dikosongkan.")
                pause(interactive)

        # ========== EXIT ==========
        elif choice == "5":
            print("Keluar. Sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid.")
            pause(interactive)

if __name__ == "__main__":
    main()
