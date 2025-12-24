def create_folder(service, folder_name, parent_folder_id=None):
    query = f"name = '{folder_name}' and mimeType = 'application/vnd.google-apps.folder'"
    if parent_folder_id:
        query += f" and '{parent_folder_id}' in parents"

    response = service.files().list(q=query, fields="files(id)").execute()
    found_folders = response.get('files')

    if found_folders:
        return found_folders[0]['id']

    folder_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }

    if parent_folder_id:
        folder_metadata['parents'] = [parent_folder_id]

    created_folder = service.files().create(body=folder_metadata, fields='id').execute()
    return created_folder.get('id')
