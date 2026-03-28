# utils.py
from datetime import datetime, timedelta

def validate_date(date_str: str) -> bool:
    """
    Validates if the input string is in YYYY-MM-DD format.
    Returns True if valid, False otherwise.
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def calculate_next_period(last_period: str, cycle_length: int) -> str:
    """
    Calculates the next expected period date.
    last_period: string in YYYY-MM-DD format
    cycle_length: average cycle length in days
    Returns: next period date as string YYYY-MM-DD
    """
    last_date = datetime.strptime(last_period, "%Y-%m-%d")
    next_date = last_date + timedelta(days=cycle_length)
    return next_date.strftime("%Y-%m-%d")