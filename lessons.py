# def bublesort(list2):
#     len_index= len(list2)-1
#     count = 0
#     sorted = False
#     while not sorted:
#         sorted = True
#         for i in range(0,len_index):
#             if list2[i]>list2[i+1]:
#                 count+=1
#                 sorted = False
#                 list2[i],list2[i+1] = list2[i+1],list2[i]
#     return list2,count
# print(bublesort([14,5,3,1,9,78,24,69]))

def bubblesort(list3):
    n=len(list3)
    count = 0
    for i in range(n-1):
        swap = False
        for a in range(0, n-1):
            if list3[a]>list3[a+1]:
                list3[a],list3[a+1] = list3[a+1],list3[a]
                count+=1
                swap = True
            if not swap:
                break
    return list3,count
list3= [1,2,5,9,7,3,6]
print(bubblesort(list3))