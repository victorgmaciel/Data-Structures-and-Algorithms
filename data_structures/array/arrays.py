""" 
1. Two-Sum Problem
A. one approach is iterating through every single pair of integers
this is costly and results in a O(n2) because of the nested loops.

 """
from unittest import result


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


# print(find_target(target, nums_list))
# target = 20
# print(find_target(target, nums_list))

""" 
B. A better approach would be O(n)
hash table perhaps 
 """

def two_sum_hash_table(target_num, arr):
    result_dict = dict() #create an empty dictionary 
    for i in range(len(arr)):
        if arr[i] in result_dict:
            print(result_dict[arr[i]], arr[i])
            return True
        else:
            result_dict[target_num - arr[i]] = arr[i]
    return False

A = [-2, 1,2,4,7,11]

target = 13

print(two_sum_hash_table(target, A))


