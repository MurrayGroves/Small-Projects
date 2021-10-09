# Raise error if arguments aren't positive
def force_positive(*args):
    for arg in args:
        if arg < 0:
            raise ValueError("all inputs must be positive")


def is_prime(my_int: int) -> bool:
    force_positive(my_int)

    for i in range(2, (my_int//2)+1):
        if my_int % i == 0:
            return False

    return True


# Return all primes within range
def prime_range(start: int, end: int) -> list:
    force_positive(start, end)

    primes = []
    for i in range(start, end):
        if is_prime(i):
            primes.append(i)

    return primes


# Return prime factors of an integer
def prime_factors(my_int: int) -> list:
    force_positive(my_int)
    factors = []
    while my_int != 1:
        for i in prime_range(2, int(my_int//2)+2):
            if my_int % i == 0:
                my_int /= i
                factors.append(i)
                continue
            if i > my_int:
                break
    return sorted(factors)


# Find the highest common factor of two integers
def hcf(first: int, second: int) -> int:
    force_positive(first, second)

    first_factors = prime_factors(first)
    second_factors = prime_factors(second)

    factors = first_factors if len(first_factors) < len(second_factors) else second_factors
    factors2 = first_factors if factors == second_factors else second_factors

    highest = 1
    for i in factors:
        if i in factors2:
            highest *= i

    return highest


# Find the lowest common multiple of two integers
def lcm(first: int, second: int) -> int:
    force_positive(first, second)

    first_factors = prime_factors(first)
    second_factors = prime_factors(second)

    factors = []
    for i in first_factors:
        print(i)
        if i in second_factors:
            second_factors.pop(second_factors.index(i))

        factors.append(i)

    for i in second_factors:
        print(i)
        factors.append(i)

    multiple = 1
    for i in factors:
        print(i)
        multiple *= i

    return multiple


# Check if two integers are coprime
def is_coprime(first: int, second: int) -> bool:
    force_positive(first, second)

    if hcf(first, second) == 1:
        return True

    return False


# Provide solutions to ax+b = c mod n
def solve(a: int, b: int, c: int, n: int) -> list:
    c -= b

    solutions = []
    for i in range(a):
        if (c + i*n) % a == 0:
            solutions.append(int((c + i*n) / a))

    return solutions
