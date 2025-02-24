import math


def is_prime(num: int) -> bool:
    for i in range(2, round(math.ceil(num))):
        if num % i == 0:
            return False
    return True


for i in range(20):
    print(f"{i}: {is_prime(i)}")