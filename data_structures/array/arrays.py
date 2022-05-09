""" 
1. Two-Sum Problem
one approach is iterating through every single pair of integers
this is costly and results in a O(n2) because of the nested loops.

 """
nums_list = [-2,1,2,4,7,11]
target = 13;


def find_target(tar_num, arr):
    for i in range(len(arr)-1): # this outer loop will iterate over all elements in the arr
        for j in range(i + 1, len(arr)): # innet loop iterates from the next index of i to the last index of arr
            if arr[i] + arr[j] == tar_num:
                print(arr[i],arr[j])
                print(i,j)
                return True
    return False


print(find_target(target, nums_list))
target = 20
print(find_target(target, nums_list))




