# 1.masala
# def reverse(s):
#     vowels = "aeiouAEIOU"
#     v_list = [i for i in s if i in vowels]
#     r_vowels = v_list[::-1]
#     result = ""
#     v = 0
#     for i in s:
#         if i in vowels:
#             result += r_vowels[v]
#             v += 1
#         else:
#             result += i
#     return result

# print(reverse("sAlom"))


# 2.masala
# def reverse(s):
#     v = []
#     result = ""
#     for i in s:
#         if i.isalpha():
#             v.append(i)
#     for i in s:
#         if i.isalpha():
#             result += v.pop()
#         else:
#             result += i
#     return result


# print(reverse("he-11/o, Wo?rl.d")) 


# 3
# from datetime import datetime

# def day_(date):
#     year, month, day = map(int, date.split('-'))

#     date_obj = datetime(year, month, day)

#     day_number = date_obj.timetuple().tm_yday
#     return day_number


# 4.masala
# def letter(a, b):
#     result = 0

#     for i in a:
#         result ^= ord(i)

#     for i in b:
#         result ^= ord(i)

#     return chr(result)
# print(letter("t","te"))


# 5.masala
# def repeate(words):
#     result = []
#     for w in words:
#         s = set()
#         r = [i for i in w if i in s or s.add(i)]
#         result.extend(r)
#     return result

# words1 = ["bella", "label", "roller"]
# words2 = ["cool", "lock","cook"]
# print(repeate(words1))