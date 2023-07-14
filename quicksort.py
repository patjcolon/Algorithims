"""learning how to use quicksort alg"""


def sort_part(the_list, low_idx, pivot_idx):
    pivot_value = the_list[pivot_idx]

    while pivot_idx != low_idx:
        low_value = the_list[low_idx]

        print(the_list, low_value, pivot_value)
        if low_value > pivot_value:
            the_list[low_idx] = the_list[pivot_idx-1]
            the_list[pivot_idx] = low_value
            the_list[pivot_idx-1] = pivot_value
            pivot_idx -= 1

        else:
            low_idx += 1
    
    return pivot_idx


def quicksort(the_list, low_idx, high_idx):
    if low_idx > high_idx:
        return
    
    pivot_idx = sort_part(the_list, low_idx, high_idx)
    quicksort(the_list, low_idx, pivot_idx -1)
    quicksort(the_list, pivot_idx+1, high_idx)




list1 = [2, 5, 3, 1, 4]

quicksort(list1, 0, len(list1)-1)
print("Sorted list:", list1)