# # Write a function that takes in a non-empty array of distinct integers
#  and an integer representing a target sum. If any two numbers 
# in the input array sum up to the target sum,
#  the function should return them in an array, in any order. 
# If no two numbers sum up to the target sum,
#  the function should return an empty array.

# input: 
# array = [3,5,-4,8,11,1,-1,6]
# targetSum = 10
# output:
# [-1,11]


def twoNumberSum(array, targetSum):
    final_list=[]
    for i in range(len(array)):
        difference = targetSum-array[i]
        if difference == array[i]:
            continue
        if  difference in array:
            final_list.append(array[i])
            final_list.append(difference)
            break
    return final_list


 

if __name__=="__main__":
    array = [3,5,-4,8,11,1,-1,6]
    targetSum = 10
    print(twoNumberSum(array,targetSum))
 