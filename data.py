import csv 
def save_data(task,subject,time_spent, score, efficiency):
    with open('data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([task, subject,time_spent, score,efficiency])