def binary_search(input_array, value):
    r = len(input_array)-1
    l = 0
    mid = int(l+(r-l)/2)
    while(r>=l):
        if  input_array[mid]==value:
            return mid
        elif input_array[mid] > value:
             r = mid - 1
             mid = int(l + (r - l) / 2)
        else:
            l = mid + 1
            mid = int(l + (r - l) / 2)
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))