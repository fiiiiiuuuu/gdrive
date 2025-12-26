import argparse
from Google import Create_Service
from create_folder import create_folder
from upload_file import upload_file
from get_sharing_link import get_sharing_link
from download_files import download_file


def get_arguments():
    parser = argparse.ArgumentParser(description='Google Drive Manager')
    parser.add_argument(
        '--parent_id',
        type=str,
        default=None,
        help='ID родительской папки'
    )
    parser.add_argument(
        '--folder_name',
        type=str,
        default='Projects',
        help='Имя главной папки'
    )
    parser.add_argument(
        '--subfolder_name',
        type=str,
        default='Python',
        help='Имя подпапки'
    )
    parser.add_argument(
        '--mime_type',
        type=str,
        default='application/octet-stream',
        help='MimeType по умолчанию'
    )
    return parser.parse_args()


def process_file_workflow(service, file_name, mime_type, target_folder_id):
    current_mime_type = mime_type

    if mime_type == 'application/octet-stream':
        if file_name.endswith('.py'):
            current_mime_type = 'text/x-python'
        elif file_name.endswith('.png'):
            current_mime_type = 'image/png'
        elif file_name.endswith('.jpg') or file_name.endswith('.jpeg'):
            current_mime_type = 'image/jpeg'

    uploaded_file_id = upload_file(service, file_name, current_mime_type, target_folder_id)
    web_view_link = get_sharing_link(service, uploaded_file_id)
    print(f'Файл {file_name}: {web_view_link}')
    download_file(service, uploaded_file_id, file_name)


def main():
    args = get_arguments()

    client_secret_file = 'credentials.json'
    api_name = 'drive'
    api_version = 'v3'
    scopes = ['https://www.googleapis.com/auth/drive']

    service = Create_Service(client_secret_file, api_name, api_version, scopes)

    projects_folder_id = create_folder(service, args.folder_name, args.parent_id)
    target_folder_id = create_folder(service, args.subfolder_name, projects_folder_id)

    process_file_workflow(service, 'main.py', args.mime_type, target_folder_id)


if __name__ == '__main__':
    main()
