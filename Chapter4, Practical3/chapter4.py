# -*- coding: utf-8 -*-
"""
Chapter 4
"""
#%% 4.2-4.3
import pandas as pd #kort de naam af om weet ik veel welke reden

data_in_dict= { "year" : [1950, 1951, 1952,1953, 1954, 1955,1956, 1957, 1958, 1959],"champ" : ["Farina", "Fangio", "Ascari", "Ascari","Fangio", "Fangio", "Fangio", "Fangio","Hawthorne", "Brabham"],"wins" : [3, 3, 6, 5,6, 4, 3, 4, 1, 2],"points" : [30, 31, 36, 34,42, 40, 30, 40, 42, 43]}
data_in_dict["gender"] = ["m", "m", "m","m", "m","m","m", "m", "m", "m"] #add variable
#print("printing first as a python dictionary: \n", data_in_dict) #print lelijke stream of text (dictionary)
#transfor dictionary into dataframe by using pandas (pd)
formula_One = pd.DataFrame(data_in_dict, columns = ["year", "champ", "wins", "points", "gender"]) #
print("Printing as a pandas DataFrame object: \n", formula_One)
print("the size of the table is: (rows * columns)")
print(formula_One.shape)
print("the rows are organized as:")
print(formula_One.columns)
print("the Python type of values on the columns are:")
print(formula_One.dtypes)

formula_One.to_csv('f1_fifties.csv') #save the file as csv in 
print('data frame written to csv file')

#%% 4.4

#import statistics

data_in_dict= { "year" : [1950, 1951, 1952,1953, 1954, 1955,1956, 1957, 1958, 1959],"champ" : ["Farina", "Fangio", "Ascari", "Ascari","Fangio", "Fangio", "Fangio", "Fangio","Hawthorne", "Brabham"],"wins" : [3, 3, 6, 5,6, 4, 3, 4, 1, 2],"points" : [30, 31, 36, 34,42, 40, 30, 40, 42, 43]}
data_in_dict["gender"] = ["m", "m", "m","m", "m","m","m", "m", "m", "m"] #add variable
#transfor dictionary into dataframe by using pandas (pd)
formula_One = pd.DataFrame(data_in_dict, columns = ["year", "champ", "wins", "points", "gender"]) #
team_wins= ["Alfa"] * 2 + ["Ferrari"] * 2 + ["Mercedes"] * 2 + ["Ferrari", "Maserati", "Ferrari", "Cooper"] #define column team wins
formula_One["team"] = team_wins #add column team to dictionary, based on our column created above
del(formula_One["gender"]) #delete column gender

print(formula_One.head()) #print first 5 (standard number) entries (rows) from table
print(formula_One.head(3)) #print first 3 entries from table
print(formula_One["champ"][-4:]) #frint last 4 entries from column champs
print(formula_One[["champ","year"]][2:4]) #print entries 2&3 from column champ and year (let op rare notatie met dubbele blokhaakjes)
print("average schore in fifties:", statistics.mean(formula_One["points"])) #use mean from statistics and use number given in points column

only_Maserati_seasons = formula_One[formula_One.team == 'Maserati'] #make a new object of class DataFrame
print(type(only_Maserati_seasons)) #just to show what type it is
print(only_Maserati_seasons) #print newly created DataFrame

#filter to find seasons won in a Ferrari driven by Juan Manuel Fangio
only_Fangio_seasons = formula_One[formula_One.champ == 'Fangio'] #first filter based on driver
only_Fangio_driving_Ferrari_seasons = only_Fangio_seasons[only_Fangio_seasons.team == 'Ferrari'] #Filter on team
print(only_Fangio_driving_Ferrari_seasons) #print filtered output based on driver and team

#%% 4.5
import pandas as pd

oscars = pd.read_csv("OscarsWinners.csv", error_bad_lines=False)
#random_selection = oscars.sample(24) #random selection
#print(random_selection[["Name", "year_of_award", "Award Name"]]) #print selection
jewish_oscar_winners = oscars[oscars.Faith == 'Jewish'] #select all jewish people
jewish_from_germany = jewish_oscar_winners[jewish_oscar_winners.Birthplace == 'Germany'] #from DataFrame of all Jewish people select the ones borne in Gemany

#pd.set_option('display.max_rows', oscars.shape[0]) #change display setting
#pd.set_option('display.max_columns', oscars.shape[1]) #change display settings
#pd.set_option('display.width', 300) #characters in oneline widthprint(oscars)
#print(oscars)

#%% 4.7
