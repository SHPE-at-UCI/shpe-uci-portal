from __future__ import print_function # google api must be on first line
import os

# google imports
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient.http import MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/drive']

def google_drive_auth(file):
    creds = None
    if os.path.exists('token.pickle'): # allows quicker access to api from a token
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'path to credentials', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    # print("Auth finished") for testing
    service = build('drive', 'v3', credentials=creds)
    return get_file_in_google_drive(service, file)

def get_file_in_google_drive(google_api_call, file_to_upload):

    # puts a file in google drive only not specific folder
    file_metadata = {
    'name': 'This is name of file that appears on google drive', #this name appears on google drive
    #'mimeType': "application/vnd.google-apps.file" # allows one to specify type of file to save
    }
    media = MediaFileUpload(file_to_upload,
                            resumable=True)
    file = google_api_call.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    #print("upload complete") for testing