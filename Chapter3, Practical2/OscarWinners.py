#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 22:03:23 2019

@author: hielke
"""
import csv


with open("OscarsWinners.csv") as handler_csv_file:
    raw_content_file = csv.reader(handler_csv_file) #collection of characters
    table = list(raw_content_file) #table is a list of lists
#%%  
print(table)    
print("data records=", len(table))
print("table header=", table[0])
print("last record in table=", table[-1])
print("name in last record in table=", table[-1][3])
print("data points in a record=", len(table[0]))
index_in_excel = 1
for record in table:
    index_in_excel += 1
    print("index in excel:", index_in_excel, len(record))
for record in table[1:]: #skip the header
    category = record[0]
    year_of_win = record[2]
    name_winner = record[3]
    print(year_of_win, name_winner, "won the", category, "award")

expected_record_length = len(table[0])
consistent = True
word_counter = 0
index_in_excel = 1
for record in table[1:]:
    consistent = (len(record) == expected_record_length)
    if not consistent:
        index_in_excel +=1
        print("Alert, Alert, Alert")
        print("entry", index_in_excel, "in excel, has", len(record), "data points")
        word_counter += 1
        continue
    else:
        index_in_excel +=1
        continue
print("the total number of faulty columns =", word_counter)




#%%
# for removing entries from list

expected_record_length = len(table[0])
consistent = True
word_counter = 0
table_index = 1
for record in table[1:]:
    consistent = (len(record) == expected_record_length)
    if not consistent:
        table_index +=1
        print("Alert, Alert, Alert")
        print("entry", table_index, "in excel, has", len(record), "data points")
        #table.remove(record) #remove entries in list that are too long. 
        word_counter += 1
        continue
    else:
        table_index +=1
        continue


#%% 
categoriseren = [] #an empty list, to be filled with found solutions
for row in table[1:]:
    categ = row[0]
    year = int(row[2]) #forcing year to be integer
    faith = row[8]
    #print(row)
    if categ == 'Best Director' and 1940 <= year <= 1949 and faith == 'Jewish':
        to_append = (str(row[0]), str(row[2:5]), str(row[8])) #make a string which can be added to list
        print(row[0], row[2:5], row[8], row[10])
        categoriseren.append(to_append) #add a solution to the list
print("the number of solutions is:", len(categoriseren)) #display total of number of solutions that are in list

#%% 3.6

#adding entries to file
to_append = []
index_in_list = 0
for column in table[0]: #loop door alle columns van table row 1 (of 0, indexing....)
    variable_name = str(column) #read column name
    if variable_name == 'Award Number':
        last_entry = table[-1]
        previous_award_nr = int(last_entry[1])
        variable_name = previous_award_nr + 1
        print("ik heb zelf award number berekend, nml: ", variable_name)
        continue #gaat nog niet helemaal goed MOI 
    user_input = input("{}: ".format(variable_name)) #only 1 line of code and askst every column variable
    to_append.insert(index_in_list, user_input) #add value to list
    index_in_list +=1 #makes sure next value is added behind previous
table.append(to_append)
print(table[-1])

with open("OscarPlus.csv", mode="w") as handler: #make new file
    file_writer = csv.writer(handler) #geen idee
    for row in table: #loop alle rows af in table
        file_writer.writerow(row) #schrijf elke row naar file

#%% 3.7

def average_age_of_directors(table): #define function
    age_at_winning = [] #make empty list
    for row in table[1:]: #loop through all rows in table
        if row[0] == 'Best Director': #check if row contains best director
            birthday = row[6] #get birthday of director
            birthday = int(birthday[-4:]) #get last 4 digits (year of birth)
            year_of_win = int(row[2]) #get year of win from column 3 (remember index 0 = column 1)
            age_at_win = int(year_of_win-birthday) #maak een sommetje
            age_at_winning.append(age_at_win) #voeg toe aan lijst
            continue
        else:
            continue
    average_age_at_winning = round(sum(age_at_winning)/len(age_at_winning) , 1) #som alle ages en deel door aantal invoeren en rond het af op 1 decimaal
    return average_age_at_winning #geef average age at winning terug aan mij
            


average_age_at_winnen = average_age_of_directors(table) #roep functie op






        