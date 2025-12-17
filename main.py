import argparse
from Google import Create_Service
from create_folder import create_folder
from upload_file import upload_file
from get_sharing_link import get_sharing_link
from download_files import download_file

def get_args():
    parser = argparse.ArgumentParser(description='Google Drive Manager')
    parser.add_argument('--parent_id', type=str, default=None, help='ID родительской папки')
    parser.add_argument('--folder_name', type=str, default='Projects', help='Имя главной папки')
    parser.add_argument('--subfolder_name', type=str, default='Python', help='Имя подпапки')
    parser.add_argument('--mime_type', type=str, default='image/png', help='MimeType для основного файла')
    return parser.parse_args()

def main():
    args = get_args()
    
    CLIENT_SECRET = 'credentials.json'
    API_NAME = 'drive'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/drive']

    service = Create_Service(CLIENT_SECRET, API_NAME, API_VERSION, SCOPES)

    projects_folder_id = create_folder(service, args.folder_name, args.parent_id)
    new_project_folder_id = create_folder(service, args.subfolder_name, projects_folder_id)

    utka_id = upload_file(service, 'utka.png', args.mime_type, new_project_folder_id)
    utka_link = get_sharing_link(service, utka_id)
    print(f'Файл utka.png: {utka_link}')
    download_file(service, utka_id, 'utka.png')

    script_id = upload_file(service, 'main.py', 'text/x-python', new_project_folder_id)
    script_link = get_sharing_link(service, script_id)
    print(f'Файл main.py: {script_link}')
    download_file(service, script_id, 'main.py')
    
    print(f"Обработано файлов: {args.files_count}")

if __name__ == '__main__':
    main()
