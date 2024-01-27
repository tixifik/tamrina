

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 13:56:17 2023

@author: pardis
"""

def adad_be_binary(adad):
    return "{:032b}".format(int(adad))

a = int(input())
b = int(input())
c = int(input())

list1 = []



a = str(adad_be_binary(a))
b = str(adad_be_binary(b))

binary = b+a

for i in range(c):
    vorodi = int(input())
    if binary[-vorodi-1]=='1':
        list1.append('yes')
    elif binary[-vorodi-1]=='0':
        list1.append('no')
        

for x in range(len(list1)):
    print(list1[x])