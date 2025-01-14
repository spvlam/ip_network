from firebase_admin import credentials, initialize_app, storage
from fastapi import  UploadFile,HTTPException

cred_path = "configs/gen-lang-client-0171787428-firebase-adminsdk-k51fh-283522ca15.json"
cred = credentials.Certificate(cred_path)
initialize_app(cred, {"storageBucket": "gen-lang-client-0171787428.appspot.com"})
bucket = storage.bucket()


class FirebaseSto():
    def upload_image(self, file: UploadFile):
        try:
            file_content =  file.file.read()
            file_name = file.filename
            file_name = "/home/lamnv/Pictures/" + file_name
            print(file_name)
            blob = bucket.blob(file_name)
            blob.upload_from_string(file_content, content_type=file.content_type)
            blob.make_public()
            public_url = blob.public_url
            return public_url
        except Exception as e:
            print(f"Error: {e}")
            raise HTTPException(status_code=500, detail="An error occurred while uploading the image.")
    