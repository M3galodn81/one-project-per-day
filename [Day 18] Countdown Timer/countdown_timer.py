import time

t_hour, t_minute, t_second = 0,0,0

def user_input(time_mode):
    # time_mode = which unit of time
    global t_hour, t_minute, t_second
    t_hour_set, t_minute_set, t_second_set = False,False,False

    while True:
        try:
                if time_mode ==  "hour" and not t_hour_set:
                    t_hour = int(input("Enter the amount of hours you want the enter (The maximum is 23 hours): "))
                    if t_hour > 23: 
                        print("The timer can only go on for a day")
                        continue
                    
                    t_hour_set = True
                    break

                if time_mode == "minute" and not t_minute_set:
                    t_minute = int(input("Enter the amount of minutes you want the enter (The maximum is 59 minutes): "))
                    if t_minute > 59: 
                        print("The timer can only go up to 59 minutes")
                        continue

                    t_minute_set = True
                    break

                if time_mode ==  "second" and not t_second_set:
                    t_second = int(input("Enter the amount of seconds you want the enter (The maximum is 59 seconds): "))
                    if t_second > 59: 
                        print("The timer can only go up to 59 second")
                        continue

                    t_second_set = True
                    break

        except ValueError:
            print("Please enter a whole number")

def countdown():
    global t_hour, t_minute, t_second
    total_time_in_seconds = (t_hour*60*60) + (t_minute*60) + t_second
    while total_time_in_seconds:
        hour = total_time_in_seconds // 3600
        minute = (total_time_in_seconds % 3600) // 60
        second = total_time_in_seconds % 60

        print(f"{hour:02d}:{minute:02d}:{second:02d} <-----------------------")
        time.sleep(1)
        total_time_in_seconds -= 1
    print("Times out")


print("Welcome to the Countdown Timer")
print("The program will ask you to input how many hours, minutes or seconds for your countdown timer.")

while True:
    user_input("hour")
    user_input("minute")
    user_input("second")
    print(f"The timer is {t_hour:02d}:{t_minute:02d}:{t_second:02d}")
    countdown()

    is_reset = input("Do you want to use the app again [yes/no (any other input will be converted into no)]")
    if is_reset in ['y','yes']:
        continue
    else: break