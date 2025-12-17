def create_folder(service, name, parent_id=None):
    query = f"name = '{name}' and mimeType = 'application/vnd.google-apps.folder'"
    if parent_id:
        query += f" and '{parent_id}' in parents"
    
    response = service.files().list(q=query, fields="files(id)").execute()
    found_files = response.get('files')
    
    if found_files:
        return found_files[0]['id']
    
    metadata = {'name': name, 'mimeType': 'application/vnd.google-apps.folder'}
    if parent_id:
        metadata['parents'] = [parent_id]
        
    created_file = service.files().create(body=metadata, fields='id').execute()
    return created_file.get('id')
