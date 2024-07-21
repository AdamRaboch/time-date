import datetime
# comment 3
def print_current_date_time():
    now = datetime.datetime.now()
    day_of_week = now.strftime("%A")
    formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ", formatted_date_time)
    print("Day of the week: ", day_of_week)

if __name__ == "__main__":
    print_current_date_time()
