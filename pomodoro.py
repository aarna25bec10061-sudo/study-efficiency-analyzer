import time
def pomodoro_session():
    print("Starting Pomodoro session ")
    focus_time = 25  
    break_time = 5  
    print("Focus time started")
    time.sleep(focus_time)
    print("Break Time ")
    time.sleep(break_time)
    print(" Pomodoro session completed ")
    return focus_time