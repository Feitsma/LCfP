#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
quiz programm for python certificate

Hielke Feitsma 
20-11-2019
"""

import pandas as pd
import numpy as np
import sys
import random
import os
import time

def add_question():
    df = pd.read_csv("question_form.csv", sep=';')
    #df = pd.DataFrame(columns=['question', 'right_answer', 'fake_answer_1', 'fake_answer_2', 'fake_answer_3']) #to make a fresh dataFrame
    nr_questions = df.shape[0]
    question = input("Ask me a question: ") 
    right_answer = input("Give me the right answer: ") 
    fake_answer_1 = input("Enter the first fake answer: ")
    fake_answer_2 = input("Enter the second fake answer: ")
    fake_answer_3 = input("Enter a third fake answer: ")
    new_row = {'question':question, 'right_answer':right_answer, 'fake_answer_1':fake_answer_1, 'fake_answer_2':fake_answer_2, 'fake_answer_3':fake_answer_3}
    df= df.append(new_row, ignore_index=True)

    df.to_csv('question_form.csv', index=False, sep=';')
    
def play_game():
    df = pd.read_csv("question_form.csv", sep=';')
    nr_questions = df.shape[0]
    random_question_nr = random.randrange(0, nr_questions)
    print('Here comes the question: ')
    answer_locations = [1,2,3,4]
    np.random.shuffle(answer_locations) #shuffle for random answer sequence
    options = ['[A]','[B]','[C]','[D]']
    print(df.iloc[random_question_nr, 0])
    length_plus_one = len(answer_locations) + 1 
    for i in range(1,length_plus_one):
        print(options[i-1], df.iloc[random_question_nr, answer_locations[i-1]])
    user_input = input('Respond with answer: ') 

    if user_input == 'A':
        given_answer = df.iloc[random_question_nr, answer_locations[0]]
    elif user_input == 'B':
        given_answer = df.iloc[random_question_nr, answer_locations[1]]
    elif user_input == 'C':
        given_answer = df.iloc[random_question_nr, answer_locations[2]]
    elif user_input == 'D':
        given_answer = df.iloc[random_question_nr, answer_locations[3]]
    else:
        print("Not an option")
        time.sleep(2)
        os._exit(1)
    if given_answer == df.loc[random_question_nr, 'right_answer']:
        print("Gratz, right answer!")
        time.sleep(2)
        os._exit(1)
    else:
        print("wrong answer, start again")
        play_game()
        
    
def see_questions():
    df = pd.read_csv("question_form.csv", sep=';')
    print(df)
    

def quiz_master():
    answer = input('What do you want?' '\n' 
                   '[A] = Play a game' '\n' 
                   '[B] = Add a question' '\n' 
                   '[C] = See all questions' '\n'
                   'I want to : ')
    try:
        if answer == 'A':
            play_game()
        elif answer == 'B':
            add_question()
        elif answer == 'C':
            see_questions()
    except:
        print('Ik stop al')
        time.sleep(2)
        os._exit(1)


while True:
    quiz_master()


