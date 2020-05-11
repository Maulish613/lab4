# -*- coding: utf-8 -*-
"""
Created on Mon May 11 15:30:21 2020

@author: mauli
"""
import string

fin = open('words.txt')
for i in fin:
    words = i.split()
    #print(words)
    for word in words:
        whitespace = string.whitespace
        punctuation = string.whitespace
        both = whitespace+punctuation
        word = word.strip(both)
        word_list = ''
        for each_letter in word:
            word_without_something = string.printable
            if each_letter in word_without_something:
                word_list+= each_letter
        print(word_list)

    