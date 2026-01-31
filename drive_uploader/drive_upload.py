from googleapiclient.http import MediaFileUpload

def upload_file(service, file_path, filename, folder_id):
    file_metadata = {
        "name": filename,
        "parents": [folder_id]
    }

    media = MediaFileUpload(file_path, resumable=True)

    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields="id"
    ).execute()

    return file.get("id")
