# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 17:52:37 2017

@author: thinktic
"""

#Ejercicio 1
def sum_lista(l):
    res=0
    for i in l:
        res = res + i
    return res

#Ejercicio 2
def triple_exp(x, y, z):
    return (x**y)**z

#Ejercicio 3
def impares_113(l):
    res = []
    for i in l:
        if i % 2 == 1 and i >= 113:
            res.append(i)
    return res

#Ejercicio 4
def media(l):
    return sum(l)/len(l)

#ejercicio 5
def factorial(num):
    res = 1
    while num>1:
        res=res*num
        num = num-1
    return res

#ejercicio 6
def divisores(num):
    res = []
    for i in range(num):
        if i !=0 and num % i == 0  :
            res.append(i)
    return res  

#ejercicio 7
def primo(num):
    return(len(divisores(num))==1)      
    
        
factorial(5)