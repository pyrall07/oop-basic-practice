import pytest

def test_download_service_mocked(download_service, sample_video, mocker):
    # test download service tanpa koneksi internet menggunakan pytest-mock

    # mock YoutubeDL.download
    mock_download = mocker.patch("services.download_service.YoutubeDL.download")

    file_path = download_service.download(sample_video, path="downloads")

    # Pastikan path return sesuai format
    assert file_path == "downloads/Belajar Dasar OOP Python.mp4"

    # Pastikan YoutubeDL.download dipanggil sekali
    mock_download.assert_called_once_with([sample_video.url])
    

def test_download_service_default_path(download_service, sample_video, mocker):
    # test download tanpa path (default current folder)
    mock_download = mocker.patch("services.download_service.YoutubeDL.download")

    file_path = download_service.download(sample_video)

    assert file_path == "Belajar Dasar OOP Python.mp4"
    mock_download.assert_called_once_with([sample_video.url])
