import os
import google.generativeai as genai
from date_parser import extract_datetime_range
from calenders_util import is_available, create_appointment

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

class TailorTalkAgent:
    def handle_input(self, user_input: str) -> str:
        print(f"[Agent] User said: {user_input}")

        start, end = extract_datetime_range(user_input)
        if not start or not end:
            return "⚠️ I couldn't understand the date/time. Please try something like 'Book on 20 July at 4 PM'."

        if is_available(start, end):
            create_appointment("Meeting via TailorTalk", start, end)
            return f" You're booked on {start.strftime('%A, %d %B %Y at %I:%M %p')}!"
        else:
            return f" That slot is already taken. {start.strftime('%A ,%d %B %Y at %I:%M %p')}. Try a different time."
agent = TailorTalkAgent()