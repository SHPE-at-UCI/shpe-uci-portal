from __future__ import print_function # google api must be on first line
import os

# google imports
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient.http import MediaFileUpload
from app.extensions import db
from flask import g


SCOPES = ['https://www.googleapis.com/auth/drive']

# credentials go in same folder as this file
# file name should be whatever creds is on line 28/29
def google_drive_auth(userfile):
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('drive', 'v3', credentials=creds)
    return get_file_in_google_drive(service, userfile)

def get_file_in_google_drive(google_api_call, file_to_upload):
    # puts a file in google drive only not specific folder
    user_data = db.child("users").child(g.user['localId']).get().val()
    use_as_filename = user_data['last_name'] + '_' + user_data['first_name']
    file_metadata = {
    'name': use_as_filename, #this name appears on google drive
    #'parents': [''] #put google folder ID inside of quotes to get file in that folder
    }
    media = MediaFileUpload(file_to_upload)
    file_to_google_drive = google_api_call.files().create(body=file_metadata,
                                        media_body=media,
                                        fields="id").execute()



# def update_file(service, userfile, id): #works
#         file_id = id
#         file_metadata = { #if name is not specified when updating the file it will keep the same name
#             'parents': '1mC7JhJA4WLp8pT7pb98NNgtSZPzqkGAn' #parent must match parent of folder
#         }
#         media = MediaFileUpload("path of file")
#         service.files().update(body=file_metadata,
#                                         media_body=media,
#                                         fileId=file_id).execute()