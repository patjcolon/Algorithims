"""learning how to use bubble search alg func
by patjcolon
last updated 7/12/2023"""

def bubble_search(the_list):
    """sorts  through a list ordering list pairs
    sorts through up to (len(list)-1)**2 times
    O(n**2) time"""
    high_idx = len(the_list) - 1
    in_order = False

    print(the_list, "<-- start")

    for i in range(high_idx):
        print("\nCycle:", (i+1))
        in_order = True
        for j in range(high_idx):
            swap_spot = ""

            item = the_list[j]
            next = the_list[j+1]
            if item > next:
                the_list[j] = next
                the_list[j+1] = item
                in_order = False

                swap_spot = "<-- swap"
            print(the_list, i, j, swap_spot)
        
        if in_order == True: 
            remaining_cycles = high_idx - i
            print(f"\nFinished early by {remaining_cycles} cycles.\n" 
                  if remaining_cycles > 0 else "Done.")
            return


unsorted_list = [101, 49, 3, 12, 56]
sorted_list = [3, 12, 49, 56, 101]

bubble_search(unsorted_list)
bubble_search(sorted_list)