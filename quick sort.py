def quick_sort(list1):
    length = len(list1)
    if len(list1) <=1:
        return list1
    else:
        pivot = list1.pop()

    items_s = []
    items_l = []

    for i in list1:
        if i > pivot:
            items_l.append(i)
        else:
            items_s.append(i)

    return quick_sort(items_s) + [pivot] + quick_sort(items_l)


quick_sort([17,5,2,4,19,8])