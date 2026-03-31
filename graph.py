import matplotlib.pyplot as plt
import csv
def plot_graph():
    time_data = []
    score_data = []
    try:
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) < 4:
                    continue
                time_data.append(float(row[2]))
                score_data.append(float(row[3]))
    except FileNotFoundError:
        print("No data found yet")
        return
    if len(time_data) == 0:
        print("No data to plot.")
        return
    plt.plot(time_data, score_data)
    plt.xlabel("Time Spent")
    plt.ylabel("Score")
    plt.title("Time vs Score")
    plt.show()
if __name__ == "main":
    print("Running plot_graph")
    plot_graph()
    print("Done")