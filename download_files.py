import os
import io
from googleapiclient.http import MediaIoBaseDownload


def download_file(service, file_id, filename):
    if not os.path.exists('Download'):
        os.makedirs('Download')
        
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(os.path.join('Download', filename), 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    
    done = False
    while done is False:
        status, done = downloader.next_chunk()
