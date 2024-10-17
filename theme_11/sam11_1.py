def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    n = 200
    fibonacci_numbers = list(fib(n))
    print(f"200-е число Фибоначчи: {fibonacci_numbers[-1]}")
