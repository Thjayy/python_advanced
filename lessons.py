# def counter(start):
#     def increment(step=1):
#         nonlocal start
#         start = start + step
#         print(start)
#     return increment
# my_func = counter(5)

# my_func()
# my_func()

# from collections import namedtuple
# Color = namedtuple('Color', ['red', 'green', 'blue'])
# rgb_colors = {"red":235, "green":64, "blue":52}
# rgb_rang = Color(235,64,52)
# print(rgb_rang)

from collections import namedtuple
User = namedtuple('User', ['name', 'age', 'location'])
def get_user():
    return [
        User('Boburjon', 25, 'Ferghana'),
        User('Murodjon', 26, 'Namangan'),
        User('Javokhir', 19, 'Mars')
    ]
for i in get_user():
    print(f"{i.name} is {i.age} years old from {i.location}")