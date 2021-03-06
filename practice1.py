

'''_ real _ '''
# Make a interpolate function for pricing.
# Constraints :
# 2 <= n <= 2000
# 1 <= m <= 100
# |instances| = |price| = m
# instances[i] < instances[j] , where 0 <= i < j < m

def interpolate(n, instances, price):
    
    # 1st, Check whether there is 0 or Negative values in price array or not.
    
    for elem in price:
        if elem <= 0:
            temp = price.index(elem)
            del instances[temp]
            print(instances)
            del price[temp]
            print(price)
            continue
        else:
            price = price
            continue
    
    print(instances)
    print(price)
    
    # Now, we are free of price 0 or negative.
    # 2nd, Check whether there is a value in instance maching "n".

    if (n in instances):
        print("n is in the instances")
        unit_p = price[instances.index(n)]
        print('\n',unit_p)
        
    # if there isn't a value in instance maching "n"
    # Check each cases where n < min(instances), 
    # min(instances) < n < max(instances), and
    # n > max(instances)
    
    elif (n > min(instances)) and (n < max(instances)):
        print("n is not in the instances")
        ind1 = _
        for i in range(len(instances)-1):
            if n > instances[i] and n < instances[i+1] :
                ind1 = i
                break
            else:
                continue

        slope_in = (price[ind1+1] - price[ind1]) / (instances[ind1+1] - instances[ind1])
        a_in = price[ind1] - slope_in * instances[ind1] 
        unit_p = slope_in*n + a_in 
    
    elif n > max(instances):
        m = len(instances)
        print("n is larger than max value in the instances")
        slope_max = float(price[m-1] - price[m-2]) / (instances[m-1] - instances[m-2])
        a_max = float(price[m-1]) - slope_max * instances[m-1]
        unit_p = slope_max*n + a_max

    elif n < min(instances):
        m = len(instances)
        print("n is smaller than min value in the instances")
        slope_min = float(price[1] - price[0]) / (instances[1] - instances[0])
        a_min = float(price[0]) - slope_min * instances[0]
        unit_p = slope_min*n + a_min
    
    # print('unit_p as original form:', unit_p)
    # Because in Python, round() works wierdly...
    
    if (unit_p*1000 % 5 == 0) and (unit_p*1000 % 10 != 0): 
        unit_p = round(unit_p, 2) + 0.01
    else:
        unit_p = round(unit_p, 2) 
    
    print("{:.2f}".format(unit_p))
    pass

'''Task Trial 3'''
def interpolate(n, instances, price):
    m = len(instances)
    unit_p = _
    if n >= min(instances) and n <= max(instances):
        if n in instances:
            for i in range(len(instances)):
                if instances[i] == n and price[i] > 0:
                    unit_p = price[i]
                else:
                    unit_p = unit_p

        else: 
            for i in range(len(instances)):       
                for elem in price:
                    if elem == 0:
                        temp = price.index(elem)
                        del instances[temp]
                        #print(instances)
                        del price[temp]
                        #print(price)
                    else:
                        continue
            ind1 = _
            for i in range(len(instances)):
                if n >= instances[i] and n <= instances[i+1] :
                    ind1 = i
                    
                else:
                    ind1 = ind1
    
            slope1 = (price[ind1+1] - price[ind1]) / (instances[ind1+1] - instances[ind1])
            a_1 = price[ind1] - slope1 * instances[ind1] 
            unit_p = slope1*n + a_1    

    elif n > max(instances):
        slope_max = float(price[m-1] - price[m-2]) / (instances[m-1] - instances[m-2])
        a_max = float(price[m-1]) - slope_max * instances[m-1]
        unit_p = slope_max*n + a_max

    elif n < min(instances):
        slope_min = float(price[1] - price[0]) / (instances[1] - instances[0])
        a_min = float(price[0]) - slope_min * instances[0]
        unit_p = slope_min*n + a_min
    
    print('unit_p as original form:', unit_p)
    # Because in Python, round() works wierdly...
    if (unit_p*1000 % 5 == 0) and (unit_p*1000 % 10 != 0): 
        unit_p = round(unit_p, 2) + 0.01
    else:
        unit_p = round(unit_p, 2) 
    
    print(unit_p)
    pass

''' # Task Trial 2 '''
def interpolate(n, instances, price):
    m = len(instances)
    if n >= min(instances) and n <= max(instances):
        if n in instances:
            for i in range(len(instances)):
                if instances[i] == n and price[i] > 0:
                    unit_p = price[i]
                    break
                
        else: 
            for i in range(len(instances)):
                #temp_ls = [round(0.1 * a, 1) for a in list(range(1,11))]
       
                for elem in price:
                    if elem == 0:
                        temp = price.index(elem)
                        del instances[temp]
                        print(instances)
                        del price[temp]
                        print(price)
                    elif elem != 0:
                        continue
                    break
                    
                
            print(instances)
            print(price)
            temp_lst = []
            
            for i in range(len(instances)):
                a = abs(n - instances[i])
                temp_lst.append(a)
                print(temp_lst)
            print(temp_lst.index(min(temp_lst)))
            ind1 = instances.index(min(temp_lst))
            slope1 = price[ind1+1] - price[ind1]/(instances[ind1+1] - instances[ind1])
            a_1 = price[ind1] - price[ind1]*slope1
            unit_p = slope1*n + a_1    

    elif n > max(instances):
        
        slope_max = float(price[m-1] - price[m-2])/(instances[m-1] - instances[m-2])
        a_max = float(price[m-1]) - slope_max * instances[m-1]
        unit_p = slope_max*n + a_max

    elif n < min(instances):
        slope_min = float(price[1] - price[0])/(instances[1] - instances[0])
        a_min = float(price[0]) - slope_min * instances[0]
        unit_p = slope_min*n + a_min
    #unit_p = round(unit_p,2)
    print(round(unit_p*100/100,2))
    #print('{:.2f}'.format(unit_p))
    pass
''' # Task trial 1 '''
if n >= min(instances) and n <= max(instances):
    if n in instances:
        for i in range(len(instances)):
            if instances[i] == n and price[i] > 0:
                unit_p = prices[i]
        break

    else: 
        temp_lst = []
        for i in range(len(instances)):
            a = abs(n - instances[i])
            temp_lst.append(a)
        ind1 = instances.index(min(temp_lst))
        slope1 = (prices[ind1+1] - prices[ind1])/(instances[ind1+1] - instances[ind1])
        a_1 = prices[ind1] - prices[ind1]*slope1
        unit_p = slope1*n + a_1    
            
elif n > max(instances):
    slope_max = (prices[m-1] - prices[m-2])/(instances[m-1] - instances[m-2])
    a_max = prices[m-1] - slope_max * instances[m-1]
    unit_p = slope*n + a_max
    
elif n < min(instances):
    slope_min = (price[1] - prices[0])/(instances[1] - instances[0])
    a_min = prices[0] - slope_min * instances[0]
    unit_p = slope*n + a_min
''' Task end'''

def is_leap(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
print(is_leap(int(input()))

def is_leap(year):
    leap = False
    if year % 400 == 0 and year % 100 != 0:
        leap = True
    elif year % 4 == 0:
        leap = True
    # Write your logic here
    return leap

year = int(input())
print(is_leap(year))

def is_leap(year):
    leap = False
    if year % 400 == 0:
        leap = True
    else:
        if year % 100 == 0:
            leap = leap
        elif year % 4 == 0:
            leap = True
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))



'''
Task
Given an integer, , perform the following conditional actions:

If  n is odd, print Weird
If  n is even and in the inclusive range of 2 to 5, print Not Weird
If  n is even and in the inclusive range of 6 to 20, print Weird
If  n is even and greater than 20, print Not Weird

Input Format
A single line containing a positive integer, n.

Constraints
1<= n <=100

Output Format
Print Weird if the number is weird; otherwise, print Not Weird.

'''

# My Solution

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    if n%2 != 0:
        print('Weird')
    elif n > 20:
        print('Not Weird')
    elif n >=6 :
        print('Weird')
    else:
        print('Not Weird')

        
'''
Task
Read two integers from STDIN and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.

Input Format
The first line contains the first integer, a. The second line contains the second integer, b.

Constraints
1<= a <= 10**10
1<= b <= 10**10

Output Format
Print the three lines as explained above.
'''

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a+b)
    print(a-b)
    print(a*b)
    
    
'''
Task
Read two integers and print two lines. The first line should contain integer division, a//b. 
The second line should contain float division, a/b.

You don't need to perform any rounding or formatting operations.

Input Format
The first line contains the first integer, . The second line contains the second integer, .

Output Format
Print the two lines as described above.
'''

a = int(input())
b = int(input())
print(a//b)
print(a/b)
