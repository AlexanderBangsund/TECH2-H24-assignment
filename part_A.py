from math import sqrt
import numpy as np





def std_loops(x):
    sum_dataset = 0
    
    mean_of_squares = 0
    
    
    for i in range(len(x)):
        sum_dataset += x[i]
        mean_of_squares += (x[i])**2
        
    mean_dataset = sum_dataset / len(x)

    mean_of_squares = mean_of_squares / len(x)


    variance = mean_of_squares - mean_dataset**2

    standard_deviation = float(sqrt(variance))
        
    
        
    return float(standard_deviation)


x = [1, 2, 3, 4, 5]
std_dev = std_loops(x)   

print(std_dev)




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





dataset = [1, 2, 3, 4, 5]

#Define the list

dataset_array = np.array(dataset)

#convert the dataset into an array



std = np.std(dataset_array)


#Using the built in function to find the standard deviation and assign it to the variable std

print(std)
   
