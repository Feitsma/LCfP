# -*- coding: utf-8 -*-
"""
Chapter5, Practical4
"""
#%%
import pandas as pd
import numpy as np

class_of_2019 = pd.read_csv("classOf2019.csv", sep = ';', encoding= "ISO-8859-1") #sep = separator (is a semicolon in this case in stead of standard comma), also add encoding because of weird é in someones name
#print("Printing as a pandas DataFrame object: \n", class_of_2019)
#print("the size of the table is: (rows * columns)")
#print(class_of_2019.shape) #to determin lenght of row and columns
#print("the rows are organized as:")
#print(class_of_2019.columns)
#print("the Python type of values on the columns are:")
#print(class_of_2019.dtypes)

number_of_rows = class_of_2019.shape[0] #determines number of entries. [1] is for columns
zeros = [0] * number_of_rows #create empty list of 0's
class_of_2019['nrGoodAnswers'] = zeros
class_of_2019['nrBadAnswers'] = zeros
print(class_of_2019)
for newCol in ['nrGoodAnswers','nrBadAnswers']:
    class_of_2019[newCol] = np.nan #np is alias for numpy library which can use NaN
print(class_of_2019)  

class_names_alphabetical = class_of_2019.sort_values(by = ['Surname', 'FirstName']) #sort names based on alphabat, priority to surname
class_names_alphabetical.to_csv('classOf2019_sorted.csv', index=False,  encoding='ISO-8859-1') #save the file as csv without index and é in the name of Leon
print(class_names_alphabetical)

#%%
import pandas as pd
import numpy as np

class_names_alphabetical = pd.read_csv("classOf2019_sorted.csv", sep = ',', encoding= "ISO-8859-1") #sep = separator (is a semicolon in this case in stead of standard comma), also add encoding because of weird é in someones name
print(class_names_alphabetical)

