


""" had to research what log n meant. my simplified version that allows me to understand it practically in regards to coding and big O:
log_x (log of base x) N can be understood as returning the ceiling for digits required to represent N in base x.
example: log_10 100 requires 2 digits to represent 100. using log_2 and n = 1024 the answer and the ceiling of the answer are the same; 10
because 2**10 = 1024. 10 digits of base 2 can represent 1024 values (ex: 0-1023). what is the minimum amount of binary digits
 required to represent 31? 2**4 = 16 which is too low, 2**6 = 64 which includes it, but 2**5 = 32 which is the min required num of digits"""

def binary_search(list, target):
    """takes a sorted list and returns index of target
    is a binary search. if target is not in list returns -1
    O(log n) time"""
    lower_bound = 0
    upper_bound = len(list) - 1

    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = list[pivot]
        if pivot_value == target:
            print("Target found at index", pivot)
            return pivot
        if pivot_value < target:
            lower_bound = pivot + 1
        elif pivot_value > target:
            upper_bound = pivot - 1
    print("Target not found in list.")
    return -1


list1 = [i for i in range (10)]

binary_search(list1, 2)
binary_search(list1, 9)
binary_search(list1, 11)

x = 0.69897000433 + 0.47712125472
print(x)
print(10 ** x)