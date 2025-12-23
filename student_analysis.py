import pandas as pd
import numpy as np
#load data
df=pd.read_csv("students.csv")
#convert marks into numpy array
marks_array=df[["Maths","science","English"]].to_numpy()
#total and average marks
df["Total_marks"]=np.sum(marks_array,axis=1)
df["Average_marks"]=np.mean(marks_array,axis=1)
#performance calculations
df["Performance"]="Poor"
df.loc[df["Average_marks"]>50,"Performance"]="Average"
df.loc[df["Average_marks"]>=75,"Performance"]= "Excellent"
#attendance analysis
attendance_array=df["Attendance"].to_numpy()
df["Attendance_status"]=np.where(attendance_array>=75,"Good""Low")
#save final report
df.to_csv("final_report.csv",index=False)
print("Student Analysis Performance done successfully")
print("Top Performer")
print(df.loc[df["Average_marks"].idmax(),["Name","Average_marks"]])
print("\nStudents Needing Improvement:")
print(df[df["Performance"] == "Poor"][["Name", "Average_Marks"]])
