

def linear_serach(list, target):
    """searches a list for target value
    searches each item in a list, returning the index value of a target or -1 if target not found
    in cases where list contains multiple indexes with target value, only the first instance will be returned"""
    for x in range(len(list)):
        if list[x] == target:
            print("Target found at index", x)
            return x
    print("Target not in list.")
    return -1


list1 = [0, 9, 42, 5, 3, 5]

linear_serach(list1, 5)
linear_serach(list1, 9)
linear_serach(list1, 10)