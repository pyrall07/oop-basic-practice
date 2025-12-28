from main import main

def test_cli_flow_with_fixtures(mocker, capsys, repo, search_service, download_service):
    """
    Test alur CLI interaktif menggunakan fixture sepenuhnya:
    1. Search video
    2. List repository
    3. Download video
    4. Exit
    """
    # Simulasi input user
    mocker.patch("builtins.input", side_effect=[
        "1",            # menu search
        "Python",       # keyword
        "2",            # max_results
        "2",            # menu list saved videos
        "3",            # menu download
        "1",            # pilih video 1
        "",             # folder default
        "5"             # exit
    ])

    # Mock download agar tidak benar-benar download
    mocker.patch("services.download_service.YoutubeDL.download")

    # Jalankan main() dengan dependency injection
    main(repo=repo, search_service=search_service, download_service=download_service)

    captured = capsys.readouterr()
    # Cek output ada judul video dari dummy_client
    assert "Python Video 1" in captured.out
    assert "Python Video 2" in captured.out
    # Cek ada pesan sukses download
    assert "Video berhasil didownload" in captured.out
    # Cek menu exit
    assert "Keluar. Sampai jumpa!" in captured.out

    # Cek repository telah menyimpan video dari search
    assert len(repo.list_all()) == 2
