"""fizzbuzz 3 5 game, trying lambda solution"""

# key notes: 

# *map() * is unpacker. i wonder if it works for dict_keys type objects that can't be subscripted
# dict1 = {1: "a", 2: "b", 3: "c"}
# keys = [*dict1.keys()]
# print(keys)
# print(keys[1])
# it works


#  not 0 or 1+ is interesting. is / is not -> true false?
# print(not 2)
# print(not 0)
# yes





def fizzbuzz(num):
    for i in range(num):
        if not i % 3 and not i % 5:
            print("FizzBuzz")
        elif not i % 5:
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i)

num = 50
fizzbuzz(num)

# *map() * is unpacker (also works for dict_keys type of objs: [*dict1.keys()])
# not 0 is True not 1+ is False; inverted bool
print(*map(lambda i: "Fizz"*(not i % 3) + "Buzz"*(not i % 5) or i, range(1,num)),sep="\n")
# magical, beautiful, elegant. coding poetry