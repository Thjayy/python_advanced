def insertion_sort(list1):
    indexlen = range(1, len(list1))

    for i in indexlen:
        value = list1[i]

        while list1[i-1] > value and i>0:
            list1[i], list1[i-1] = list1[i-1], list1[i]
            i = i-1
        
    return list1

print(insertion_sort([6,5,8,11,12]))