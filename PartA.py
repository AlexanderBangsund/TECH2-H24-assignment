

from math import sqrt

dataset = [1, 2, 3, 4, 5]




def std_loops(dataset):
    sum_dataset = 0
    
    mean_of_squares = 0
    
    
    for i in range(len(dataset)):
        sum_dataset += dataset[i]
        mean_of_squares += (dataset[i])**2
        
    mean_dataset = sum_dataset / len(dataset)

    mean_of_squares = mean_of_squares / len(dataset)


    variance = mean_of_squares - mean_dataset**2

    standard_deviation = sqrt(variance)
        
    
        
    return float(standard_deviation)
std_dev = std_loops(dataset)   

print(std_dev)