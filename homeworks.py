1.
def rbubblesort(lst):
    count = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0 and lst[i] >= 10:
            lst[i] = int(str(lst[i])[::-1])
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            count+=1
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst, count

3.
def bubble_sort(arr):
    s = len(arr)
    for i in range(s):
        for j in range(0, s-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

4.
def words(file1):
    with open(file1, 'r') as file:
        text = file.read()
        text = text.replace('|', ' ')
        words = text.split()
        return len(words)
    
5.
def guess_number():
    low = 1
    high = 50
    a = 0

    while low <= high:
        mid = (low + high) // 2
        a += 1

        print(f"shu raqammi? {mid}? (urinish {a})")
        r = input("Enter 'baland', 'past', or 'togri': ")

        if r == "baland":
            high = mid - 1
        elif r == "past":
            low = mid + 1
        elif r == "togri":
            print(f"{mid} {a}-ta urinishta topildi")
            break
        else:
            print("Notogri kiritilgan")