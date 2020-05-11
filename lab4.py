# -*- coding: utf-8 -*-
"""
Created on Mon May 11 15:30:21 2020

@author: mauli
"""
import string

fin = open('words.txt')
for i in fin:
    words = i.split()
    print(words)

    