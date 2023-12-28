1.
def underscores(lst):
    unqnumbers = []
    result = []
    
    for num in lst:
        if num not in unqnumbers:
            unqnumbers.append(num)
            result.append(num)
        else:
            result.append('_')
    
    return result

list1 = [1, 4, 25, 8, 42, 25, 8]
list2 = underscores(list1)
print(list2)

2.
def dstring(str1, str2):
    if len(str1) > len(str2):
        return str1[len(str2):]
    else:
        return str2[len(str1):]
    
r1 = dstring("abcde", "abcd")
r2 = dstring("aa", "a")

3.
def element(num):
    result = 0
    for i in num:
        result ^= i
    return result

r = element([2, 2, 1, 4, 5, 4, 5, 8, 7, 7, 8])

5.
def likes(names):
    num_likes = len(names)
    if num_likes == 0:
        return "xich kim yoqtirmedi"
    elif num_likes == 1:
        return f"{names[0]}ga yoqadi"
    elif num_likes == 2:
        return f"{names[0]} va {names[1]}ga yoqadi"
    elif num_likes == 3:
        return f"{names[0]}, {names[1]} va {names[2]}ga yoqadi "
    else:
        return f"{names[0]}, {names[1]} va yana {num_likes - 2} yoqadi"
    



4.
def number(nums):
    n = len(nums)
    a = 0
    for i in range(n + 1):
        a ^= i
    for num in nums:
        a ^= num
    return a