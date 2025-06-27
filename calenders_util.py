from __future__ import print_function
import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'tailor-talk-agent-448fcde5f672.json'
CALENDAR_ID = 'primary'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('calendar', 'v3', credentials=credentials)

def is_available(start_time, end_time):
    events = service.events().list(
        calendarId=CALENDAR_ID,
        timeMin=start_time.isoformat() + 'Z',
        timeMax=end_time.isoformat() + 'Z',
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    busy = events.get('items', [])
    print(f"[DEBUG] Found {len(busy)} conflicting events")
    return len(busy) == 0

def create_appointment(summary, start_time, end_time):
    event = {
        'summary': summary,
        'start': {
            'dateTime': start_time.isoformat(),
            'timeZone': 'Asia/Kolkata'
        },
        'end': {
            'dateTime': end_time.isoformat(),
            'timeZone': 'Asia/Kolkata'
        },
    }
    event_result = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
    print(f"[DEBUG] Event created: {event_result.get('htmlLink')}")
    return event_result
