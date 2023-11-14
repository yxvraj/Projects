#Yuvraj Deshpande MIS 15 Section 01 Part 2: School

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#I will be using a numbering system. This will make it easier to refer to the instructions and see what part belongs where. 
#For example, #1 means that i did the first of the problem, which was to download the sheet, and so on:

#8
df = pd.read_excel("Generic University Data Updated (1) .xlsx", sheet_name="Schools")

#9
df['Total'] = df.sum(axis=1)

#10
year = range(2008,2018)

#11
scholarship = df.loc['Business and Management', year]
scholarship.plot()
scholarship.ply(kind='line')

#12
plt.title('School of Business Scholarship Amounts')
plt.ylabel('Amount of Money')
plt.xlabel('Years')
plt.show()

#13
All_scholarships = df.loc['Health Sciences', 'Social Sciences' , 'Arts and Humanities' , 'Business and Management' , 'Engineering' , year]
All_scholarships.plot()
All_scholarships.ply(kind='line')

#14
print(df.max(year, 2018))

#End of Part 2
