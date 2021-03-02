#quickstart.py is the code neccesary to first implement the google drive API.
#Note that all of this code is suggested to be directly copied from google drive API and not altered. This code helps
#to run the initial setup of the google drive API so that requests can be made.
#code can be found here: https://developers.google.com/drive/api/v3/quickstart/python

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.activity.readonly']


# Returns a string representation of the first elements in a list.
def truncated(array, limit=2):
    contents = ', '.join(array[:limit])
    more = '' if len(array) <= limit else ', ...'
    return u'[{0}{1}]'.format(contents, more)


# Returns the name of a set property in an object, or else "unknown".
def getOneOf(obj):
    for key in obj:
        return key
    return 'unknown'


# Returns a time associated with an activity.
def getTimeInfo(activity):
    if 'timestamp' in activity:
        return activity['timestamp']
    if 'timeRange' in activity:
        return activity['timeRange']['endTime']
    return 'unknown'


# Returns the type of action.
def getActionInfo(actionDetail):
    return getOneOf(actionDetail)


# Returns user information, or the type of user if not a known user.
def getUserInfo(user):
    if 'knownUser' in user:
        knownUser = user['knownUser']
        isMe = knownUser.get('isCurrentUser', False)
        return u'people/me' if isMe else knownUser['personName']
    return getOneOf(user)


# Returns actor information, or the type of actor if not a user.
def getActorInfo(actor):
    if 'user' in actor:
        return getUserInfo(actor['user'])
    return getOneOf(actor)


# Returns the type of a target and an associated title.
def getTargetInfo(target):
    if 'driveItem' in target:
        title = target['driveItem'].get('title', 'unknown')
        return 'driveItem:"{0}"'.format(title)
    if 'drive' in target:
        title = target['drive'].get('title', 'unknown')
        return 'drive:"{0}"'.format(title)
    if 'fileComment' in target:
        parent = target['fileComment'].get('parent', {})
        title = parent.get('title', 'unknown')
        return 'fileComment:"{0}"'.format(title)
    return '{0}:unknown'.format(getOneOf(target))

creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
    # time.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service = build('driveactivity', 'v2', credentials=creds)

# Call the Drive Activity API
results = service.activity().query(body={
    'pageSize': 10
}).execute()
activities = results.get('activities', [])

if not activities:
    print('No activity.')
else:
    print('Recent activity:')
    for activity in activities:
        time = getTimeInfo(activity)
        action = getActionInfo(activity['primaryActionDetail'])
        actors = map(getActorInfo, activity['actors'])
        targets = map(getTargetInfo, activity['targets'])
        print(u'{0}: {1}, {2}, {3}'.format(time, truncated(actors), action, truncated(targets)))





