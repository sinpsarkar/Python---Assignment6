# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 20:30:52 2019

@author: psarka
"""
import numpy as np

def Vandermode(series,increasing):
    
    #read comma separated numbers
    a = [int(x) for x in series.split(',')]
    i = 0

    n = len(a)

    #define shape 
    if n == 0 :
        arr = np.array(a * n,dtype=int)                
        matrix_structure = arr.reshape(n,n)
    else:
        arr = np.array(a * n,dtype=int)                
        matrix_structure = arr.reshape(n,len(a))

    #create the final matrix according to the inputs provided
    while(i < n):
            if increasing == 'True' or increasing == "":
            # if increasing is true
                matrix_structure[i] = matrix_structure[i] ** i
            else:
            # if increasing is false
                matrix_structure[i] = matrix_structure[i] ** (n - (i + 1))
            i += 1        

    return matrix_structure.transpose()


series=input("Input numbers separated by comma: ")
print(Vandermode(series,'False'))
print(Vandermode(series,'True'))
