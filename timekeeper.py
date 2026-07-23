import time
print("Welcome to TimeKeeper!")
print("1. General Timer")
print("2. Focus Timer")
while True:
    try:
        choice = int(input("Enter your choice (1 or 2): "))
        if choice in [1, 2]:
            break
        else:
            print("Enter either 1 or 2")
            continue
    except ValueError:
        print("Invalid Input")

def general_timer():
    while True:
        time_in_minutes = int(input("Enter the Time (in minutes): "))
        if time_in_minutes <= 0:
            print("Enter a Time Greater than Zero")
            continue
        else:
            break
    total_time_in_seconds = time_in_minutes * 60
    for i in range (total_time_in_seconds, -1, -1):
        hours = i // 3600
        remainder1 = i % 3600
        minutes = remainder1 // 60
        seconds = remainder1 % 60
        print(f"\r{hours}:{minutes:02}:{seconds:02}", end="")
        time.sleep(1)
    print("Time's Up!")
def focus_timer():
    while True:
        focus_minutes = int(input("Enter the Time You Want to Focus for (in minutes): "))
        focus_interval = int(input("Enter the Interval you Want Between Study Sessions (in minutes): "))
        if focus_minutes <= 0 or focus_interval <= 0:
            print("Enter a Time Greater than Zero")
            continue
        else:
            break
    total_focus_seconds = focus_minutes * 60
    interval_seconds = focus_interval * 60
    for i in range(total_focus_seconds, -1, -1):
        hours = i // 3600
        remainder1 = i % 3600
        minutes = remainder1 // 60
        seconds = remainder1 % 60
        print(f"\r{hours}:{minutes:02}:{seconds:02}", end="")
        time.sleep(1)
        elapsed = total_focus_seconds - i
        if elapsed != 0 and elapsed % interval_seconds == 0 and i != 0:
            print("\nTime for a Break!")
    print("\nFocus Session COmplete!")
                  

if choice == 1:
    general_timer()

else:
    focus_timer()
#NOTE - EVERY PROGRAM HAS LATENCY AND OVER LONGER INTERVALS THERE WILL BE DIFFERENCE BETWEEN ACTUAL TIME AND TIME DISPLAYED IN TERMINAL
