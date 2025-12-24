from googleapiclient.http import MediaFileUpload


def upload_file(service, file_name, mime_type, parent_folder_id):
    media_content = MediaFileUpload(file_name, mimetype=mime_type)

    query = f"name = '{file_name}' and '{parent_folder_id}' in parents and trashed = false"
    response = service.files().list(q=query, fields="files(id)").execute()
    found_files = response.get('files')

    if found_files:
        existing_file_id = found_files[0]['id']
        service.files().update(fileId=existing_file_id, media_body=media_content).execute()
        return existing_file_id
    else:
        file_metadata = {'name': file_name, 'parents': [parent_folder_id]}
        new_file = service.files().create(
            body=file_metadata,
            media_body=media_content,
            fields='id'
        ).execute()
        return new_file.get('id')
