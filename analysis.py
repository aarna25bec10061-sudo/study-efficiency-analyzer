def analyze_performance(time_spent, score , efficiency):
    print("Personal Analysis")
    if time_spent < 10 and efficiency >= 0.8:
        print(" your study sessions are short but highly focused")
    elif time_spent >= 30 and efficiency >= 0.5:
        print("your study sessions are consistent and productive")
    elif efficiency >= 1:
        print("your study session gets great results in a short time")
    elif time_spent >= 20 and efficiency < 0.5:
        print("your study sessions are long but not very effective. try changing study methods.")
    else:
        print(" keep experimenting with different study methods to find what works best for you")
    if efficiency < 0.5:
        print("Try changing your study method or reducing distractions")
    elif efficiency >= 1:
        print("Your method is working well")
import csv
def subject_analysis():
    subject_scores = {}
    subject_time = {}
    try:
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) < 5:
                    continue
                subject = row[1]
                time_spent = float(row[2])
                score = float(row[3])
                subject_scores[subject] = subject_scores.get(subject, 0) + score
                subject_time[subject] = subject_time.get(subject, 0) + time_spent
    except FileNotFoundError:
        print("No data available.")
        return
    print(" Analysis for subjects:")
    for subject in subject_scores:
        avg_eff = subject_scores[subject] / subject_time[subject]
        print(f"{subject}: Efficiency = {avg_eff:.2f}")
    weakest = min(subject_scores, key=lambda s: subject_scores[s] / subject_time[s])
    strongest = max(subject_scores, key=lambda s: subject_scores[s] / subject_time[s])
    print("Strongest subject: {strongest}")
    print("Need more focus: {weakest}")
import csv
def experiment_mode():
    print(" Experiment Mode")
    sessions = []
    try:
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) < 5:
                    continue
                time_spent = float(row[2])
                score = float(row[3])
                sessions.append((time_spent, score))
    except FileNotFoundError:
        print("No data available")
        return
    if len(sessions) < 2:
        print("Not enough data to analyze")
        return
    short_sessions = [s for s in sessions if s[0] < 20]
    long_sessions = [s for s in sessions if s[0] >= 20]
    if short_sessions:
        avg_short = sum(s[1] for s in short_sessions) / len(short_sessions)
    else:
        avg_short = 0
    if long_sessions:
        avg_long = sum(s[1] for s in long_sessions) / len(long_sessions)
    else:
        avg_long = 0
    print(f"Avg score (short sessions): {avg_short:.2f}")
    print(f"Avg score (long session): {avg_long:.2f}")
    if avg_short > avg_long:
        print("you perform better in short session ")
    else:
        print("you perform better in longer sesssion ")