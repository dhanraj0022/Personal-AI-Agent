import streamlit as st
import requests
import os
from datetime import datetime

from drive_auth import get_drive_service
from drive_upload import upload_file
from drive_folders import list_folders


st.set_page_config(page_title="Google Drive File Uploader")

st.title("📤 Google Drive Upload Tool")

# -----------------------------
# Cache Google Drive connection
# -----------------------------
@st.cache_resource
def init_drive():
    return get_drive_service()

service = init_drive()

# -----------------------------
# UI Inputs
# -----------------------------
url = st.text_input("Source file URL")

folders = list_folders(service)

if not folders:
    st.error("No folders found in Google Drive.")
    st.stop()

folder_map = {f["name"]: f["id"] for f in folders}

folder_names = list(folder_map.keys())

selected_folder = st.selectbox(
    "Select destination folder",
    options=folder_names
)

folder_id = folder_map.get(selected_folder)

if not folder_id:
    st.error("Invalid folder selected.")
    st.stop()
# -----------------------------
# Upload logic
# -----------------------------
if st.button("Upload"):
    if not url:
        st.error("Please provide a file URL.")
    else:
        try:
            filename = url.split("/")[-1]
            temp_path = f"temp_{filename}"

            st.info("Downloading file...")
            r = requests.get(url)
            r.raise_for_status()

            with open(temp_path, "wb") as f:
                f.write(r.content)

            st.info("Uploading to Google Drive...")
            file_id = upload_file(service, temp_path, filename, folder_id)

            os.remove(temp_path)

            # -----------------------------
            # Upload history logging
            # -----------------------------
            os.makedirs("upload_logs", exist_ok=True)

            log_file = f"upload_logs/{datetime.now().date()}.md"

            with open(log_file, "a", encoding="utf-8") as f:
                f.write(
                    f"""## File Upload

- **Filename:** {filename}
- **Source URL:** {url}
- **Destination Folder:** {selected_folder}
- **Drive File ID:** {file_id}
- **Timestamp:** {datetime.now().strftime("%H:%M:%S")}

---

"""
                )

            st.success("✅ File uploaded successfully!")
            st.code(file_id)

        except Exception as e:
            st.error(f"Upload failed: {str(e)}")
