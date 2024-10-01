#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt

dataset = [1, 2, 3, 4, 5]

def std_builtin(dataset):
    mean_dataset = sum(dataset) / len(dataset)


    sum_dataset = sum(dataset)

    sum_value_sub_mean_squared = sum((value - mean_dataset)**2 for value in dataset)

    variance = sum_value_sub_mean_squared / len(dataset)

    standard_deviation = float(sqrt(variance))
    
    return standard_deviation
std_dev = std_builtin(dataset)
print(std_dev)
   

    
    
    
    
    


