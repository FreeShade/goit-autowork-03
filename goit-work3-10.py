def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k):
    numerator = factorial(n)
    denominator = factorial(n - k) * factorial(k)
    return numerator // denominator
