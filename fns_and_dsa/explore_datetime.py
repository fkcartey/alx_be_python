from datetime import datetime, timedelta

def display_current_datetime():
    # Obtain the current date and time
    current_date = datetime.now()
    # Format the date and time string
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date):
    # Prompt the user for the number of days
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        # Calculate the future date
        future_date = current_date + timedelta(days=days_to_add)
        # Format and print the future date
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
        return future_date
    except ValueError:
        print("Please enter a valid integer for the number of days.")

def main():
    current_date = display_current_datetime()
    calculate_future_date(current_date)

if __name__ == "__main__":
    main()
