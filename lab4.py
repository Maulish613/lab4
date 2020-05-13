# -*- coding: utf-8 -*-
"""
Created on Mon May 11 15:30:21 2020

@author: mauli
"""
import string

fin = open('pg2542.txt')

for i in fin:
    words = i.split()
    for word in words:
        white_space = string.whitespace
        punctuation = string.punctuation
        word = word.strip(white_space + punctuation)
        new_word = ''
        for j in word:
            printing_word = string.printable
            if j in printing_word:
                new_word+= j
        print(new_word)
                