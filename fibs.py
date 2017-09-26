#!/usr/bin/bash env python3

def fibonacci(n):
    fib_list = []
    a=0
    b=1
    while n > 0:
        fib_list.append(b)
        a, b = b, a+b
        n = n-1
        return (fib_list)


def fibs_generator():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b


if __name__ == "__main__":
    n = input("n value: ")
    print(fibonacci(n))
    g = fibs_generator()
    fibs_list = [next(g) for _ in range(5)]
    print(fibslist)


