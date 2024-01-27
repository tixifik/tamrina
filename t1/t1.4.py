# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 13:31:34 2023

@author: pardis
"""
def adad_be_binary(adad):
    return "{0:b}".format(int(adad))
a=int(input())
b=int(input())
a=str(adad_be_binary(a))
b=str(adad_be_binary(b))
a= int(str(10**(100-len(a)))+a)
b= int(str(10**(100-len(b)))+b)
c = 0
i = 0
while i != 61:
    c = c + abs((a//10**i)%2-(b//10**i)%2)
    i = i+1
print(c)