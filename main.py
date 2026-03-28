# main.py
# Entry point for the Period Tracker project

from utils import calculate_next_period, validate_date
from tips import get_random_tip

def main():
    print("🌸 Welcome to the Simple Period Tracker 🌸")
    
    # Input handling
    last_period = input("Enter last period date (YYYY-MM-DD): ")
    cycle_length = input("Enter average cycle length in days: ")

    # Validate inputs
    if not validate_date(last_period):
        print("❌ Invalid date format. Please use YYYY-MM-DD.")
        return
    
    try:
        cycle_length = int(cycle_length)
    except ValueError:
        print("❌ Cycle length must be a number.")
        return

    # Date calculation logic
    next_period = calculate_next_period(last_period, cycle_length)

    # Output formatting
    print("\n📅 Your next expected period is around:", next_period)
    print("💡 Tip for you:", get_random_tip())

if __name__ == "__main__":
    main()