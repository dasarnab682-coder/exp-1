import numpy as np 
import pandas as pd 
marks = np.array([72,85,91,68,77])
print ("marks:",marks)
print ("mean :", np. mean (marks))
print ("Maximum:",np.max(marks))
print ("minimum:", np.min(marks))

data= {
    "Name":["ankit","ram","sam","somnath","ramu"],
    "Attendance":[88,92,76,95,81],
    "Marks": [72,85,68,91,77]
}
df = pd.DataFrame (data)

print("\n---First Five Records---")
print(df.head())

print("\n--- Data Information---")
print(df.info())

print("\n--- Statistical Summary---")
print(df.describe())

print("\n--- Data Information---")
print(df.info())

print ("nAverage Marks:", df["Marks"].mean())


