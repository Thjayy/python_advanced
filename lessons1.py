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


# class MyRange:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.start >= self.end:
#             raise StopIteration
#         count = self.start

#         self.start+=1
#         return count
    
# nums = MyRange(1,10)
# for i in nums:
#     print(i)


# import time
# class Logger:
#     def __init__(self) -> None:
#         self.prefix = time.strftime ('%Y-%m-%d %H:%M:%S', time.localtime())
    
#     def log(self, message):
#         print(f"{self.prefix} ---> {message}")


# class Customlogger(Logger):
#     def __init__(self):
#         super().__init__()
#         self.prefix = time.strftime ('%Y-%m-%d %H:%M:%S', time.localtime())

# logger = Logger()
# logger.log("Hello")


# class FileManager:
#     def __init__(self, filename):
#         self.path = Path(filename)

#     def read(self, encoding="utf-8"):
#         return self.path.read_text(encoding)

#     def write(self, data, encoding="utf-8"):
#         self.path.write_text(data, encoding)

# class ZipFileManager:
#     def __init__(self, filename):
#         self.path = Path(filename)

#     def compress(self):
#         with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
#             archive.write(self.path)

#     def decompress(self):
#         with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
#             archive.extractall()

# def square_number(nums):
#     for i in nums:
#         yield i*i

# mylist = square_number([2,4,5,7,9])
# print (next(mylist))

# mylist = [x*x for x in [2,4,6,7,8,9]]
# print(mylist)

# import random
# import time

# names = ['Murodjon','Boburjon','Ikromjon','Abdulbosit','Javohir']
# majors = ['Math','IT','History','Geography','English','Russian']

# def person_list(person_num):
#     result = []
#     for i in range(person_num):
#         person = {
#             'id':i,
#             'name':random.choice(names),
#             'major':random.choice(majors)
#         }
#         result.append(person)

#     return result


# time1 = time.time()
# people_list = person_list(1000000)
# print(time1)
# time2 = time.time()

# print("speed of function {}".format(time2-time1))

