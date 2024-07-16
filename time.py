import datetime

def print_current_date_time():
    now = datetime.datetime.now()
    print("Current date and time: ", now.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    print_current_date_time()
