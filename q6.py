import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("student_performance.csv")

#Bar chart: Student names vs final scores.
plt.bar(df["Student"], df["Final_Score"])
plt.xlabel("Student Name")
plt.ylabel("Final Score")
plt.title("Student Performance")
plt.xticks(rotation=90)
plt.show()


#Scatter plot: Hours studied vs final scores.
plt.scatter(df["Hours_Studied"], df["Final_Score"])
plt.xlabel("Hours Studied")
plt.ylabel("Final Score")
plt.title("Student Performance")
plt.show()

#Histogram: Distribution of final scores.
plt.hist(df["Final_Score"])
plt.xlabel("Final score")
plt.ylabel("Frequency")
plt.title("Score Distribution")
plt.show()

#Line plot: Previous scores vs Final scores.
plt.plot(df["Previous_Score"])
plt.plot(df["Final_Score"])
plt.ylabel("Score")
plt.title("Score Variation")
plt.show()