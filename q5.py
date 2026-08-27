import pandas as pd

# Load the CSV
df = pd.read_csv("student_performance.csv")

#print the first five rows 
print(df.head())

#print the number of rows and columns
print("Number of rows and columns:", df.shape)

#display the column names
print("Columns:", df.columns.tolist())

#whether there are any missing values in the dataset
print("Missing values in each column:\n", df.isnull().sum())

#avg of final score
print("Average of final scores:", df['Final_Score'].mean())

#maximum of final score
print("Maximum of final scores:", df['Final_Score'].max())

#new column
df["Improvement"] = df["Final_Score"] - df["Previous_Score"]
#print(df)

#students with attendance >= 80
print(df[df["Attendance"] >= 80])

#
processed_student_performance = df.sort_values(by = "Final_Score", ascending = False)
processed_student_performance.to_csv("processed_student_performance.csv", index = False)