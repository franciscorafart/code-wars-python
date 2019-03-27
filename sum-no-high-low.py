# Sum all the numbers of the array (in F# and Haskell you get a list) except the highest and the lowest element (the value, not the index!).
# (The highest/lowest element is respectively only one element at each edge, even if there are more than one with the same value!)
#
# Example:
#
# { 6, 2, 1, 8, 10 } => 16
# { 1, 1, 11, 2, 3 } => 6
#
# If array is empty, null or None, or if only 1 Element exists, return 0.
# Note:In C++ instead null an empty vector is used. In C there is no null. ;-)

def sum_array(arr):
    sum = 0
    if not arr or len(arr)==1:
        return sum

    max, min = max_min_arr(arr)

    if max in arr:
        arr.remove(max)
    if min in arr:
        arr.remove(min)

    if arr:
        for f in arr:
            sum+=f

    return sum

def max_min_arr(arr):
    max = float('-inf')
    min = float('inf')
    for x in arr:
        if x>max:
            max = x
        if x<min:
            min = x
    return (max,min)
