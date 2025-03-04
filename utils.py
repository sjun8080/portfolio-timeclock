from datetime import datetime
import re

def validate_duration_format(duration: str) -> bool:
    """
    Validates if the duration string matches the format HH:MM
    
    Args:
        duration (str): Duration string in format "HH:MM"
        
    Returns:
        bool: True if valid format, False otherwise
    """
    pattern = r'^\d{1,2}:\d{2}$'
    if not re.match(pattern, duration):
        return False
    
    hours, minutes = map(int, duration.split(':'))
    return 0 <= hours <= 99 and 0 <= minutes <= 59

def format_time(dt: datetime) -> str:
    """
    Formats datetime object to 12-hour time string
    
    Args:
        dt (datetime): Datetime object to format
        
    Returns:
        str: Formatted time string (e.g., "11:30 AM")
    """
    return dt.strftime("%I:%M %p").lstrip('0')

def format_day(dt: datetime) -> str:
    """
    Formats datetime object to day name
    
    Args:
        dt (datetime): Datetime object to format
        
    Returns:
        str: Day name (e.g., "Monday")
    """
    return dt.strftime("%A")
