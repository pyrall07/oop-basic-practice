from repositories.memory_repository import MemoryVideoRepository
from services.search_service import SearchService
from services.download_service import DownloadService
from utils.yt_dlp_client import YTDLPClient

def print_videos(videos):
    for idx, video in enumerate(videos, start=1):
        print(f"{idx}. {video.title} ({video.duration}s)")

def main(repo=None, search_service=None, download_service=None):
    """
    CLI interaktif.
    Bisa inject dependency (untuk testing)
    """
    repo = repo or MemoryVideoRepository()
    search_service = search_service or SearchService(repo, YTDLPClient())
    download_service = download_service or DownloadService()

    while True:
        print("\n=== YouTube Mini OOP CLI ===")
        print("1. Search video")
        print("2. List saved videos")
        print("3. Download video")
        print("4. Clear repository")
        print("5. Exit")

        choice = input("Pilih menu (1-5): ").strip()

        if choice == "1":
            keyword = input("Masukkan keyword untuk search video: ")
            max_results = input("Jumlah maksimal video yang dicari (default 5): ").strip()
            max_results = int(max_results) if max_results.isdigit() else 5

            results = search_service.search(keyword, max_results=max_results)
            print("\nHasil pencarian:")
            print_videos(results)

        elif choice == "2":
            videos = repo.list_all()
            if not videos:
                print("Repository kosong.")
            else:
                print("\nVideo di repository:")
                print_videos(videos)

        elif choice == "3":
            videos = repo.list_all()
            if not videos:
                print("Tidak ada video untuk didownload. Lakukan search terlebih dahulu.")
                continue

            print("\nPilih video yang ingin didownload:")
            print_videos(videos)
            selected_idx = input("Masukkan nomor video: ").strip()
            if not selected_idx.isdigit() or int(selected_idx) < 1 or int(selected_idx) > len(videos):
                print("Pilihan tidak valid.")
                continue

            selected_video = videos[int(selected_idx)-1]
            download_path = input("Masukkan folder tujuan (default current folder): ").strip()
            download_path = download_path or None

            saved_file = download_service.download(selected_video, download_path)
            print(f"Video berhasil didownload: {saved_file}")

        elif choice == "4":
            confirm = input("Apakah yakin ingin menghapus semua video di repository? (y/n): ").lower()
            if confirm == "y":
                repo.clear()
                print("Repository berhasil dikosongkan.")

        elif choice == "5":
            print("Keluar. Sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih menu 1-5.")

if __name__ == "__main__":
    main()
