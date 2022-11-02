# Write a function that takes in a non-empty array of integers
#  that are sorted in ascending order and
#  returns a new array of the same length with the squares 
# of the original integers also sorted in ascending order. 
# array = [1,  2,  3,  5,  6,  8,  9] 
# Returns: [1,  4,  9,  25,  36,  64,  81]

def sortedSquareArray(array):
    squared_array =[]
    for j in array:
        product_j =j**2
        squared_array.append(product_j)
    return squared_array

if __name__=="__main__":
    array = [1,  2,  3,  5,  6,  8,  9] 
    print(sortedSquareArray(array))