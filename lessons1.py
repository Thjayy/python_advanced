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


sequence_type = [1,2,3,4,5,6,7,8,9]
print(sequence_type.index(5))