#!/usr/bin/env python3


def happy_new_year():
    for i in range(10, 0, -1):
        print(i)
    print("Happy New Year!")


def square_integers(int_list):
    return [x**2 for x in int_list]


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def print_numbers_with_for():
    for i in range(1, 6):
        print(i)


def print_numbers_with_while():
    i = 1
    while i <= 5:
        print(i)
        i += 1


def square_numbers_with_comprehension():
    return [x**2 for x in range(1, 6)]


def square_numbers_with_generator():
    return (x**2 for x in range(1, 6))

