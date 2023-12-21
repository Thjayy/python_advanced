def binary_search(list1, value):
    start_index = 0
    end_index = len(list1)-1
    count = 0    
    while start_index <= end_index:
        mid_point = start_index + (end_index - start_index)//2
        mid_point_value = list1[mid_point]
        count+=1
        if mid_point_value == value:
            return (mid_point, mid_point_value)
        elif value<mid_point_value:
            end_index = mid_point-1
        else:
            start_index = mid_point+1
    return None
print(binary_search([1,5,6,8,17,24,45,98], 24))