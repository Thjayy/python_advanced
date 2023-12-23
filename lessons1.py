# a = 25
# name = "Boburjon"

# def func():
#     name = "Javoxir"
#     def inner_function():
#         prefix = "Google"
#         nonlocal name
#         print(prefix, name)
#         name = "Azizbek"
#     inner_function()

# func()
# print(name)


# def myfunc():
#     age = 26
#     name = "Murodjon"

#     def inner(email):
#         print(email,name)
#     return inner
# execute = myfunc()
# print(execute)
# execute("m@gmail.com")


# def counter(start):
#     def increment(step=1):
#         nonlocal start
#         start = start + step
#         print(start)
#     return increment
# my_func = counter(5)

# my_func()
# my_func()


# import re
# text = "There out her child sir his lived 77 789 456 12. Design at uneasy me season of branch on praise esteem."
# output = re.findall("\\d\\d",text)
# print(output)

# text = "Banana"
# my_char = iter(text)
# print(next(my_char))  



# def binary_search(list1, value):
#     start_index = 0
#     end_index = len(list1)-1
#     count = 0    
#     while start_index <= end_index:
#         mid_point = start_index + (end_index - start_index)//2
#         mid_point_value = list1[mid_point]
#         count+=1
#         if mid_point_value == value:
#             return (mid_point, mid_point_value)
#         elif value<mid_point_value:
#             end_index = mid_point-1
#         else:
#             start_index = mid_point+1
#     return None
# print(binary_search([1,5,6,8,17,24,45,98], 24))


class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        count = self.start

        self.start+=1
        return count
    
nums = MyRange(1,10)
for i in nums:
    print(i)