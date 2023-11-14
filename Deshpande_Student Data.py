#Yuvraj Deshpande MIS 15 Section 01 Part 1: Student Data

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#I will be using a numbering system. This will make it easier to refer to the instructions and see what part belongs where. 
#For example, #1 means that i did the first of the problem, which was to download the sheet, and so on:

#2
#Reading the file and looking for a specifc sheet inside the file
df = pd.read_excel(io = "/Users/yuvraj/Downloads.xls" , sheet_name = "Generic University Data Updated.xlsx")

#3 
print(df.shape)

#4
print(df.head())
print(df.tail())

#5
#
df=df.drop(["Aid Type","ID","Pell Grant Amount","Postal Code","City"])

#6
print(df.head(5))

#7
#7 Part 1:
filter1=df.loc[df["State"]=="California"]
#7 Part 2:
filter2=df.loc[df["Gender"]=="Female"]

#End of Part 1

