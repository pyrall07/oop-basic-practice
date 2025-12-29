import pytest

def test_download_service_mocked(download_service, sample_video, mock_client):
    download_service.download(sample_video, path="downloads")
    
    mock_client.download.assert_called_once_with(
        sample_video.url,
        "downloads"
    )
    

def test_download_service_default_path(download_service, sample_video, mock_client):
    download_service.download(sample_video)
    
    mock_client.download.assert_called_once_with(
        sample_video.url,
        None
    )
