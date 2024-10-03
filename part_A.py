from math import sqrt
import numpy as np





def std_loops(x):   #Define the finction for parameter x
    sum_dataset = 0
    
    mean_of_squares = 0   #Add local values within the function
    
    
    for i in range(len(x)):
        sum_dataset += x[i]   
          #Loops through the parameter and add together each index to the variable sum_dataset
          
        mean_of_squares += (x[i])**2   
        
        #Loops through the parameter and raise every index to the power of 2
        
    mean_dataset = sum_dataset / len(x)     
    
    #computes the mean of the dataset

    mean_of_squares = mean_of_squares / len(x)
#Compute the mean of squares

    variance = mean_of_squares - mean_dataset**2

#Use the previous assigned variables to assign the variancee

    standard_deviation = float(sqrt(variance))
        
    #Compute the standard deviation
    
        
    return float(standard_deviation)

#return standard deviation


x = [1, 2, 3, 4, 5]

#Assign the values to the dataset


std_dev = std_loops(x)   



#call the function

print(std_dev)






#Apply the given dataset

def std_builtin(dataset):
    #Define the function for parameter dataset
    
    mean_dataset = sum(dataset) / len(dataset)
    
    #Use the built in functions to find the mean dataset


    sum_dataset = sum(dataset)
    
    #Use the built in function to sum the dataset

    sum_value_sub_mean_squared = sum((value - mean_dataset)**2 for value in dataset)

#List comprehension through subtract the mean dataset for every value, and then raise it to the power of 2

    variance = sum_value_sub_mean_squared / len(dataset)
    
    #Compute the variance

    standard_deviation = float(sqrt(variance))
    
    #Use the variance to find the standard deviation
    
    return standard_deviation

dataset = [1, 2, 3, 4, 5]    


std_dev = std_builtin(dataset)

#Calling the function 
print(std_dev)





dataset = [1, 2, 3, 4, 5]

#Define the list

dataset_array = np.array(dataset)

#convert the dataset into an array



std = np.std(dataset_array)


#Using the built in function to find the standard deviation and assign it to the variable std

print(std)
   
