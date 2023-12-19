# 1.masala
# import re

# def sum_(list1, list2):
#     result = []
#     for i in range(min(len(list1), len(list2))):
#         result.append(list1[i] + list2[i])
#     return result

# def e_numbers(s):
#     return [int(num) for num in re.findall(r'\d+', s)]

# list1 = "100 200 300"
# list2 = "100 202 111"
# list1_numbers = e_numbers(list1)
# list2_numbers = e_numbers(list2)
# print(sum_(list1_numbers, list2_numbers))

# list3 = "100 200 300"
# list4 = "10 20"
# list3_numbers = e_numbers(list3)
# list4_numbers = e_numbers(list4)
# print(sum_(list4_numbers, list3_numbers))


# 2.masala
# def r_number(number):
#     number_str = str(number)
#     r_numberstr = number_str[::-1]
#     return number_str == r_numberstr

# print(r_number(212))
# print(r_number(123))

# 3.masala
# import re

# def mr_character(text):
#     d_text = re.findall(r'[^a-zA-Z0-9]', '', text)

#     char_count = {}
#     for char in d_text:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1

#     max_count = 0
#     mostcommon = ''
#     for char, count in char_count.items():
#         if count > max_count:
#             max_count = count
#             mostcommon = char

#     return f'"{mostcommon}" is repeated the most'

# print(mr_character("The number is 111"))
# print(mr_character("What color is your Bugatti?")) 


# 5.masala
# def find_index(text, element):
#     for i in range(len(text)):
#         if text[i:i+len(element)] == element:
#             return f"{element}-ning indexi {i}-chi index"
#     return f"{element} topilmadi text ichida"

# print(find_index("Tomato", "o"))