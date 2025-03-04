from datetime import datetime
import re

def validate_duration_format(duration: str) -> bool:
    """Validates if the duration string matches the format HH:MM"""
    pattern = r'^\d{1,2}:\d{2}$'
    if not re.match(pattern, duration):
        return False
    
    hours, minutes = map(int, duration.split(':'))
    return 0 <= hours <= 99 and 0 <= minutes <= 59

def format_time(dt: datetime) -> str:
    """Formats datetime object to 12-hour time string"""
    return dt.strftime("%I:%M %p").lstrip('0')

def format_day(dt: datetime) -> str:
    """Formats datetime object to day name"""
    return dt.strftime("%A")
