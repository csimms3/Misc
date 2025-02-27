import time

def slowfib(n):
    if n <= 1:
        return n
    else:
        return slowfib(n-1) + slowfib(n-2)

# ~ 190000 in 1sec
def fib(n):
    arr=[0,1]
    for i in range(2,n):
        arr.append(arr[i-1]+arr[i-2])
    return arr[n-1]

# ~ 255000 in 1sec
def constspacefib(n):
    if n <= 1:
        return n

    a = 0
    b = 1
    for i in range(n//2):
        a = b + a
        b = b + a

    if n % 2 == 1:
        return b + a
    else:
        return b

# ~ 255000 in 1sec
def generatorfib(n):
    def fib():
        a, b = 0, 1
        while True:  # First iteration:
            yield a  # yield 0 to start with and then
            a, b = b, a + b

    fib_gen = fib()
    for _ in range(n):
        next(fib_gen)
    return next(fib_gen)

def main():
    s = time.time()
    generatorfib(255000)
    e = time.time()
    print(f"time elapsed: {e - s}")




main()