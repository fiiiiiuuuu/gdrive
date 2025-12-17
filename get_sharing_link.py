def get_sharing_link(service, file_id):
    fields = "webViewLink"
    response = service.files().get(fileId=file_id, fields=fields).execute()
    return response.get('webViewLink')
