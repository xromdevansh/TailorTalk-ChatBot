from dateparser.search import search_dates
from datetime import timedelta

DEFAULT_DURATION_MINUTES = 30

def extract_datetime_range(text):
    print(f"[DEBUG] Parsing input: {text}")
    results = search_dates(
        text,
        settings={
            'PREFER_DATES_FROM': 'future',
            'TIMEZONE': 'Asia/Kolkata',
            'RETURN_AS_TIMEZONE_AWARE': False,
            'DATE_ORDER': 'DMY'
        }
    )

    if not results:
        return None, None

    # Use the first matched date in the sentence
    parsed = results[0][1]
    print(f"[DEBUG] Detected datetime: {parsed}")
    start_time = parsed
    end_time = parsed + timedelta(minutes=DEFAULT_DURATION_MINUTES)

    return start_time, end_time
