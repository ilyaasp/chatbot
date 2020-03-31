# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 01:34:00 2020

@author: Ultimate
"""
#Importing libraries
import numpy as np
import tensorflow as tf
import re 
import time

# PART1: Data Preprocessing #


# Importing the dataset
lines = open('movie_lines.txt', encoding='utf-8', errors='ignore').read().split('\n')
conversations = open('movie_conversations.txt', encoding='utf-8', errors='ignore').read().split('\n')

#Creating python dictionary that maps each lines and its id
id2line = {}
for line in lines:
    _line = line.split(' +++$+++ ')
    if len(_line) == 5:
        id2line[_line[0]] = _line[4]

# Creating a list of all of the conversation
conversations_ids = []
for conversation in conversations[:-1]: #doesnt include the last row, cause its empty
    _conversation = conversation.split(' +++$+++ ')[-1][1:-1].replace("'", "").replace(" ", "")   #get the last column of each row #[1:-1] doesnt include the square bracket as the first and last element of the last column of each row    
    conversations_ids.append(_conversation.split(','))
        
#Getting separately the questions and the answers from the conversations_ids list
questions = []
answers = []
for conversation in conversations_ids:
    for i in range(len(conversation) - 1):
        questions.append(id2line[conversation[i]])
        answers.append(id2line[conversation[i+1]])

