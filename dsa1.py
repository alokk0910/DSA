#  Your Goal Today:
# Learn how to:

# Access elements using index

# Loop through a list

# Solve a simple sum problem

# num=[10,20,50,60]

# Task 1: Sum of All Elements in a List

def sum_of_elements(arry):
    total=0
    for num in arry:
        total += num
    return total

print(sum_of_elements([1,2,3,4,50]))

#  Task 2: Find Maximum Element in a List

def max_num(arr):
    if len(arr) ==0:
        return none
    
    max_num=arr[0]
    for num in arr:
        if num > max_num:
            max_num=num
    return max_num
    
print(max_num([1,5,8,22,25]))

    

    




        
