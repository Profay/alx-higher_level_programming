#!/usr/bin/python3


def safe_print_division(a, b):
    def div (num1, num2):
        return (num1 / num2)
    try:
        a = div(a, b)
        return a
    except ZeroDivisionError:
        a = None
        return None
    finally:
        print("Inside result: {}".format(a))
