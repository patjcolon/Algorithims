"""For learning the basics of algs. Recursive factorial style
by patjcolon
last updated 7/10/2023"""

def recursive_factorial(n):
    if n == 1:
        return n
    else:
        return n * recursive_factorial(n-1)
    
print(recursive_factorial(10))