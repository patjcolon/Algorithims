"""For learning the basics of algs. Fib style
by patjcolon
last updated 7/10/2023"""

# fib alg O(n)

def fib_seeded(sequence_position:int = 0):
    """Finds value of given position in the fibonacci sequence
    O(n) time O(1) space; Iterative Approach"""
    seed_zero = 0
    seed_one = 1

    if type(sequence_position) is not int or sequence_position < 0:
        return print(f"Fib sequence '{sequence_position}' cannot be obtained.")
    elif sequence_position == 0:
        return seed_zero
    elif sequence_position == 1:
        return seed_one
    else:
        while sequence_position > 1:
            next_sequence = seed_one + seed_zero
            seed_zero = seed_one
            seed_one = next_sequence
            sequence_position -= 1
    return print(next_sequence)


def fib_recursive(sequence_position):
    """Finds value of a given position in the fibonacci sequence
    O(2**n) time O(n) space; Recursive Approach"""
    if sequence_position < 2:
        return sequence_position
    back_one = sequence_position - 1
    back_two = sequence_position - 2

    this_position = fib_recursive(back_one) + fib_recursive(back_two)
    return this_position

print(fib_recursive(6))
print(fib_recursive(7))