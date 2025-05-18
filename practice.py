# ## Fibonacci Sequence
#
# def fib(number):
#     # Starting the sequence
#     n1, n2 = 0, 1
#     # for loop to move the numbers along
#     for _ in range(number):
#         # yield the current value of n1
#         yield n1
#         # give n1 and n2 new values
#         n1, n2 = n2, n1 + n2
#
# # Print all the numbers in the sequence up to the given parameter
# print(fib(21))

def fib_list(number):
    result = []
    n1, n2 = 0, 1
    for _ in range(number):
        result.append(n1)
        n1, n2 = n2, n1 + n2
    return result

print(fib_list(21))