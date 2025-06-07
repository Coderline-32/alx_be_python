from datetime import datetime, timedelta

def display_current_datetime():
    global current_date
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")

def calculate_future_date():
    days_entry = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=days_entry)
    formatted_future = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"The date in future will be {formatted_future}")

display_current_datetime()
calculate_future_date()
