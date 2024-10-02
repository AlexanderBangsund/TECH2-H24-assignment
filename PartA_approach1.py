

from math import sqrt






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






