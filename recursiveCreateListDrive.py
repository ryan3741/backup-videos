# recursiveCreateListDrive.py is the code to go through the entire google drive final video folder to find all of the
# files and then output them to the finalVideoNamesDrive.txt file. This does not make assumptions that the google drive
# final video folder is structured in any way and goes through recursively.

import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']


def get_gdrive_service():
    """ Grants access to the google drive by asking user to log in or using credentials from previous run.

    parameters:
    -none

    Output:
    -google drive api service
    """
    creds = None
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    # return Google Drive API service
    return build('drive', 'v2', credentials=creds)

def recursiveList(ID, service, f):
    """ Recursively goes through the file tree printing out all files but not printing out folders.

    parameters:
    -string: idthe id for the current file/folder
    - f, file stream that we are writing to
    -google drive api service

    Output:
    -none but function does print out the current id if it relates to a file and not to a folder
    """

    currFile = service.files().get(fileId=ID).execute()

    # check if our current ID refers to a file or folder
    if currFile['mimeType'] != 'application/vnd.google-apps.folder':
        # if it refers to a file, then we output it to our file stream
        f.write(currFile["title"])
        f.write("\n")
        print(currFile["title"])

    # loop through all of the children of our current ID so we can recursively check them
    #note that 1000 is the maximum number of children that this function can handle on google drive side
    children = service.children().list(folderId=ID, maxResults=1000).execute()
    for child in children.get('items', []):
        # make the recursive call on the child
        recursiveList(child['id'], service, f)
    return

def print_files_in_folder(service, folderID, fileOutput):
    """ This function outputs  all of the files within the inputted folder to a txt file.

    parameters:
    -string: the id for the current file/folder
    -google drive api service
    -string: name of file to output to

    Output:
    -doesn't return anything but does write the names of all of the files within this directory
    """
    f = open(fileOutput, 'w')
    recursiveList(folderID, service, f)
    f.close()


#calls function that logs individual in and then outputs names of files to txt file
service = get_gdrive_service()

# update this to be the drive folder that will be traversed to output files
driveFolder = ""

#this is the name for the file that will be outputted
fileOutput = "recursiveVideoNamesDrive.txt"

#runs the main function
print_files_in_folder(service, driveFolder, fileOutput)



