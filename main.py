
import tasks
import timer
import data
import analysis
import graph
import pomodoro
while True:
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. plot the Graph")
    print("4. subject analysis")
    print("5. Experiment Mode")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
       tasks.add_task()
    elif choice == "2":
        tasks.showtasks()
        if len(tasks.task_list) == 0:
            continue
        try:
            index= int(input("Enter the task number to start the timer: ")) - 1
            if index < 0 or index >= len(tasks.task_list):
                print("Invalid task number.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        task_name = tasks.task_list[index]
        subject = input("Enter the subjectd for this task: ")
        print("Starting timer for task: {task_name}")
        print("Choose your study method:")
        print("1.traditional Study")
        print("2. Pomodoro Technique ")
        study_method = input("Enter your choice: ")
        if study_method == "1":
           time_spent = timer.start_timer()
        elif study_method == "2":
           time_spent = pomodoro.pomodoro_session()
        else:
            print("Invalid choice.using normal timer by default.") 
            time_spent = timer.start_timer()
        score = float(input("Enter your score for this task : "))
        if time_spent == 0:
            efficiency = 0
        else:
            efficiency = score / time_spent
        print(f"Efficiency for task '{task_name}': {efficiency:.2f}")
        analysis.analyze_performance(time_spent, score, efficiency)
        data.save_data(task_name,  subject,time_spent, score,efficiency)
        print("Data saved successfully.")
    elif choice == "3":
        print("Plotting the graph")
        graph.plot_graph()
    elif choice == "4":
        analysis.subject_analysis()
    elif choice == "5":
        analysis.experiment_mode()
    elif choice == "6":
        print("Exiting the program")
        break
    else:
        print(" choice is invalid. Please try again.")