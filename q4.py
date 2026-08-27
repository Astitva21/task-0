import numpy as np

# Hours studied
hours_studied = np.array([2, 5, 1, 7, 3, 6, 4, 8, 2, 9])

# Attendance
attendance = np.array([94, 65, 86, 96, 73, 50, 53, 86, 63, 96])

# Previous scores
previous_scores = np.array([88, 66, 52, 96, 57, 74, 85, 93, 79, 87])

# Final scores
final_scores = np.array([60, 82, 68, 91, 65, 85, 74, 96, 55, 98])

#print shape of each array
print("Shape:")
print("Hours Studied   -> ", hours_studied.shape)
print("Attendance      -> ", attendance.shape)
print("Previous Scores -> ", previous_scores.shape)
print("Final Scores    -> ", final_scores.shape)

#print data type of each array
print("Dtype:")
print("Hours Studied   -> ", hours_studied.dtype)
print("Attendance      -> ", attendance.dtype)
print("Previous Scores -> ", previous_scores.dtype)
print("Final Scores    -> ", final_scores.dtype)

#print mean of final scores
print("Mean of Final Scores -> ", np.mean(final_scores))

#print maximum and minimum of final scores
print("Maximum of Final Scores -> ", np.max(final_scores))
print("Minimum of Final Scores -> ", np.min(final_scores))

#print standard deviation of final scores
print("Standard Deviation of Final Scores -> ", np.std(final_scores))

#final scores + 5
print("Final Scores + 5 -> ", final_scores + 5)

#boolean array showing which students scored at least 75.
print("Students who scored at least 75 -> ", final_scores >= 75)

#print the final scores of students who scored at least 75.
print("Final Scores of students who scored at least 75 -> ", final_scores[final_scores >= 75])