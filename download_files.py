import os
import io
from googleapiclient.http import MediaIoBaseDownload


def download_file(service, file_id, file_name):
    if not os.path.exists('Download'):
        os.makedirs('Download')

    request = service.files().get_media(fileId=file_id)
    file_path = os.path.join('Download', file_name)
    file_handler = io.FileIO(file_path, 'wb')
    downloader = MediaIoBaseDownload(file_handler, request)

    done = False
    while done is False:
        status, done = downloader.next_chunk()
