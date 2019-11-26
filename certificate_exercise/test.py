#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 19:28:45 2019

@author: hielke
"""

import pandas as pd


df = pd.read_csv("question_form.csv", sep=';')
#df = pd.DataFrame(columns=['question', 'right_answer', 'fake_answer_1', 'fake_answer_2', 'fake_answer_3'])
nr_questions = df.shape[0]
question = input("Ask me a question: ") 
right_answer = input("Give me the right answer: ") 
fake_answer_1 = input("Enter the first fake answer: ")
fake_answer_2 = input("Enter the second fake answer: ")
fake_answer_3 = input("Enter a third fake answer: ")
new_row = {'question':question, 'right_answer':right_answer, 'fake_answer_1':fake_answer_1, 'fake_answer_2':fake_answer_2, 'fake_answer_3':fake_answer_3}
df= df.append(new_row, ignore_index=True)

df.to_csv('question_form.csv', index=False, sep=';')