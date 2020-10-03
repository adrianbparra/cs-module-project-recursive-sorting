# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    middle = (start+ end) // 2 
    # start at the middle
    # check if target is bigger than or less than
    if arr == []:
        return -1

    if target == arr[middle]:
        return middle
        # if greater set new end
    elif target > arr[middle]:
        # print("greater")
        return binary_search(arr,target,middle,end)
        # if less set new start
    else:
        # print("less")
        return binary_search(arr,target,start,middle)

# arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]

# print(binary_search(arr1, 2, 0, len(arr1)-1))


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively

def agnostic_binary_search(arr, target):
    # Your code here
    pass

