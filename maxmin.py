#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 09:52:11 2020

@author: cheeku
"""

list = []
num = int(input("How many numbers:"))

for n in range(num):
    numbers = int(input('Enter numbers:'))
    list.append(numbers)

print('Maximum element:', max(list), '\nMinimum element:', min(list))