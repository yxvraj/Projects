#Yuvraj Deshpande MIS 15 Section 01 Part 3: Program

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#I will be using a numbering system. This will make it easier to refer to the instructions and see what part belongs where. 
#For example, #1 means that i did the first of the problem, which was to download the sheet, and so on:

#15
df = pd.read_excel("Generic University Data Updated (1).xlsx", sheet_name="Programs")

#16
df['Total'] = df.sum(axis=1)

#17
df_top=df.head(5)
print(df_top)

#18
df_top.plot(kind='area', stacked=True,  figsize=(10,6))
df_top.plot(kind='area', stacked=False,  figsize=(10,6))
plt.title('Top 5 Programs with the highest amount of scholarships')
plt.ylabel('Years')
plt.xlabel('Programs')
plt.show()

#19
print(df['Computer Science' , 'Information Management' , 'Business Administration'].head())

#19 Part 2: 
df.loc[['Computer Science', 'Information Management', 'Business Administration'], year]
df_top = df.loc[['Computer Science', 'Information Management', 'Business Administration'], year].transpose()
df_top.plot(kind='hist', figsize=(10, 6))
plt.title('Scholarship Amount Distribution between threee different programs')
plt.ylabel('Amount of money')
plt.xlabel('Program')
plt.show()

