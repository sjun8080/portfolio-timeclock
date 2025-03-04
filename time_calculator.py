from datetime import datetime, timedelta
import pytz
from tzlocal import get_localzone
from utils import validate_duration_format, format_time, format_day

class TimeCalculator:
    def __init__(self):
        """Initialize TimeCalculator with system timezone"""
        self.local_tz = get_localzone()
        self.now = datetime.now(self.local_tz)
        
    def calculate_end_time(self, duration: str) -> tuple:
        """
        Calculate end time based on current time and duration
        
        Args:
            duration (str): Duration string in format "HH:MM"
            
        Returns:
            tuple: (start_time, start_day, end_time, end_day, timezone)
            
        Raises:
            ValueError: If duration format is invalid
        """
        if not validate_duration_format(duration):
            raise ValueError("Invalid duration format. Use HH:MM format (e.g., '5:40')")
            
        # Parse duration
        hours, minutes = map(int, duration.split(':'))
        
        # Calculate end time
        end_time = self.now + timedelta(hours=hours, minutes=minutes)
        
        return (
            format_time(self.now),
            format_day(self.now),
            format_time(end_time),
            format_day(end_time),
            str(self.local_tz)
        )
    
    def format_output(self, duration: str) -> str:
        """
        Format the calculation result as a string
        
        Args:
            duration (str): Duration string in format "HH:MM"
            
        Returns:
            str: Formatted output string
        """
        try:
            start_time, start_day, end_time, end_day, tz = self.calculate_end_time(duration)
            
            return (
                f"Start Time: {start_time} on {start_day} ({tz})\n"
                f"Duration: {duration}\n"
                f"End Time: {end_time} on {end_day} ({tz})"
            )
        except ValueError as e:
            return f"Error: {str(e)}"
