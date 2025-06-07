from datetime import datetime, timedelta


def display_current_datetime():
    global current_date
    current_date =  datetime.now()
    

def calculate_future_date():
    days_entry = int(input("Enter number of days: "))
    future_date  = current_date + timedelta(days = days_entry)
    print(f"The date in future will be {future_date}") 
display_current_datetime()
calculate_future_date()