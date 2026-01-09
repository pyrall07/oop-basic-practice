from project import main

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

    mocker.patch.object(
        download_service.client,
        "download",
        return_value=None
    )

    # Jalankan main() dengan dependency injection
    main(
    repo=repo,
    search_service=search_service,
    download_service=download_service,
    interactive=False
)

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

def test_cli_clear_repository(mocker, capsys, repo, search_service, download_service):
    mocker.patch(
        "builtins.input", side_effect=[
            "1", "Python", "2", # search
            "4", "y",           # clear repository
            "2",                # list
            "5"                 # exit
        ]
    )
    
    main(
    repo=repo,
    search_service=search_service,
    download_service=download_service,
    interactive=False
)
    
    captured = capsys.readouterr()
    
    assert "Repository berhasil dikosongkan." in captured.out
    assert "Repository kosong." in captured.out
    assert len(repo.list_all()) == 0
    

def test_cli_invalid_menu_input(mocker, capsys, repo, search_service, download_service):
    mocker.patch(
        "builtins.input", side_effect=[
            "9", # invalid menu
            "5"
        ]
    )
    main(
    repo=repo,
    search_service=search_service,
    download_service=download_service,
    interactive=False
)
    
    captured = capsys.readouterr()
    assert "Pilihan tidak valid" in captured.out
    
def test_cli_multiple_download(mocker, capsys, repo, search_service, download_service):
    mocker.patch("builtins.input", side_effect=[
        "1", "Python", "3",   # search
        "3",                  # download
        "1,3",                # multiple selection
        "",                   # default path
        "5"                   # exit
    ])

    mock_download = mocker.patch.object(
        download_service.client,
        "download",
        return_value=None
    )

    main(
    repo=repo,
    search_service=search_service,
    download_service=download_service,
    interactive=False
)

    captured = capsys.readouterr()

    assert "Video berhasil didownload:" in captured.out
    assert "Python Video 1" in captured.out
    assert "Python Video 3" in captured.out
    
    assert mock_download.call_count == 2
