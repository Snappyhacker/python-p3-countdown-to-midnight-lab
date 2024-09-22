# your code goes here!
# countdown.py

def countdown(start):
    while start > 0:
        print(f"{start} SECOND(S)!")
        start -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(start):
    import time
    while start > 0:
        print(f"{start} SECOND(S)!")
        time.sleep(1)  # Sleep for 1 second between prints
        start -= 1
    print("HAPPY NEW YEAR!")
