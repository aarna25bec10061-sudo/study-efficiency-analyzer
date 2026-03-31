import time
def start_timer():
    print("Timer started.")
    input("press enter to start the timer")
    start_time = time.time()
    print("timer started")
    input("press enter to stop the timer")
    end_time = time.time()
    time_spent = end_time - start_time
    print(f"Time spent: {time_spent:.2f} seconds")
    return time_spent
    