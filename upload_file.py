from googleapiclient.http import MediaFileUpload


def upload_file(service, filename, mimetype, parent_id):
    media = MediaFileUpload(filename, mimetype=mimetype)
    
    query = f"name = '{filename}' and '{parent_id}' in parents and trashed = false"
    response = service.files().list(q=query, fields="files(id)").execute()
    found_files = response.get('files')
    
    if found_files:
        file_id = found_files[0]['id']
        service.files().update(fileId=file_id, media_body=media).execute()
        return file_id
    else:
        metadata = {'name': filename, 'parents': [parent_id]}
        file = service.files().create(body=metadata, media_body=media, fields='id').execute()
        return file.get('id')
