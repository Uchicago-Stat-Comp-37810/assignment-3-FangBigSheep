# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 09:28:10 2018
@title: assignment 3
@author: Zhengyang Fang
"""

## Prob 1. Write a function is_divisible(m, n) 

def is_divisible (m, n):
    if (n == 0):
        raise(ZeroDivisionError('n cannot be 0.'))
    if (not isinstance(m, int) or not isinstance(n, int)):
        raise(ValueError('m and n must be integers.'))
        
    try:
        return (m % n == 0)
    except:        
        return False;
    
## test cases
print(is_divisible (4, 2))
print(is_divisible (4, -2))
print(is_divisible (4, 8))

## these test cases will result in exceptions and stop the program
## uncomment them if you want to test them after all
# print(is_divisible (5, 2.5))
# print(is_divisible (4, 0))
# print(is_divisible ('hello', 8))


# Prob 2. Write a method not equal and gives the same result as the != operator.

def not_equal (x, y):
    # Even the types of x and y are different
    # == operator can handle it
    # if for cases that == operator cannot handle
    # then != operator won't work either
    # so I am not working on other strange types of input
    
    return (not (x == y))


# test cases
print(not_equal(1, 1))
print(not_equal(1, 1.0))
print(not_equal(0.5, 0.5000000))
print(not_equal([2,4,5,6], [1,2]))
print(not_equal('123', [1,2]))
print(not_equal(1, 2))
print(not_equal('c', 2))
print(not_equal('p', 'hello'))

# Prob 3. play with functions in the math module. 

import math

# Example: 
radians = (90.0 / 360.0) * 2 * math.pi 
print (math.sin(radians))

def multi_add (a, b, c):
    return (a * b + c)

# angle test = sin(π/4)+cos(π/4)/2
print ('sin(pi/4) + cos(pi/4)/2 is:')
print (multi_add(math.cos(math.pi / 4), 1 / 2, math.sin(math.pi / 4)))  

# ceiling test = ceil(276/19) + 2log7(12)
print ('ceiling(276/19) + 2 log_7(12) is:')
print (multi_add(2 * math.log(12), 1 / math.log(7), math.ceil(276 / 19)))


# 4. Write a method rand_divis_3 that takes no parameters, generates and prints 
# a random number, and finally returns True if the randomly generated number is 
# divisible by 3, and False otherwise.

import random

def rand_divis_3():
    x = random.randint(0, 100)
    print (x)
    return (x % 3 == 0)
 
# test function
for i in range(5):
    print(rand_divis_3())