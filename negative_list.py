def count_neg(array):
    count = 0
    i = 0 # row
    j = len(array) -1 # col
    # since we are starting from right side

    while j >= 0 and i < len(array):
        if array[i][j] < 0: 
            count += (j + 1)
            i += 1
        else:
            j -= 1
    return count
print(count_neg([[-4,-3,-1,1],[-2,-2,1,2],[-1,1,2,3],[1,2,4,5]]))
