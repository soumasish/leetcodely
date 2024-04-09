"""
Intuition:
This is bottom up dynamic programming, which builds the memo all the way from bottom to up.
Most of these problems can be solved without using the entire array and just two variables,
however I find it more intuitive to understand the code using the array.
"""


def fibonacci(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    memo = [0] * n
    memo[1] = 1
    for i in range(2, n):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n - 1]


print(fibonacci(23))
