# # 1-masala
# def number(nums):
    # n = len(nums)
    # t = (n + 1) * (n + 2) // 2
    # a = sum(nums)
    # if t == a:
    #     return n + 1
    # else:
    #     return t - a


# # 2-masala
# def dsort(nums):
    # unq = set()
    # dup = []

    # for num in nums:
    #     if num in unq:
    #         dup.append("_")
    #     else:
    #         unq.add(num)

    # result = sorted(list(unq)) + dup
    # return result


# # 3-masala
# def find_first_occurrence(haystack, needle):
#     return haystack.find(needle)

# haystack = "sadbutsad"
# needle = "sad"


# # 4-masala
# def search(num, target):
#     l, r = 0, len(num) - 1
#     while l <= r:
#         mid = (l + r) // 2
#         if num[mid] == target:
#             return mid
#         elif num[mid] < target:
#             l = mid + 1
#         else:
#             r = mid - 1
#     return l


# nums = [1, 3, 5, 6]
# target = 5