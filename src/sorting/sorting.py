# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # loop over both arr while merging values in a increasing order
    a_p = 0
    b_p = 0
    merging_point = 0

    # loop as long as array a point and array b point
    # are less than their length
    while a_p < len(arrA) and b_p < len(arrB) :
        # if list a[point] is less than b[point] assign a[point] at mergin point
        if arrA[a_p] < arrB[b_p]:
            merged_arr[merging_point] = arrA[a_p]
            a_p += 1
        # else assign b[point] at mergin point
        else:
            merged_arr[merging_point] = arrB[b_p]
            b_p += 1

        # move to next point in merged_arr
        merging_point += 1

    # go through array without fallin out of range
    # if list a has still values add them to merged_arr
    while a_p < len(arrA):
        merged_arr[merging_point] = arrA[a_p]
        a_p += 1
        merging_point += 1

    # if list b has still values add them to merged_arr
    while b_p < len(arrB):
        merged_arr[merging_point] = arrB[b_p]
        b_p += 1
        merging_point += 1

    return merged_arr


# print(merge([1,5,6],[3,7,8]))

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

    # for a merge sort to work we have to split the code in half
        # until one value is left in arr
        # base case is only one value
        # need the middle
        # need left
        # need right
    # then we merge those values back up in the same pattern
        # with the merge function
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    left = merge_sort(left)

    right = merge_sort(right)
    
    arr = merge(left,right)

    return arr

# print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    
    pass
def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
