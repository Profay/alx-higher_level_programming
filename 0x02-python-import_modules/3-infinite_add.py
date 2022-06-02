#!/usr/bin/python3
import sys


def main():
    a = len(sys.argv)
    sum = 0
    for b in range(1, a):
        sum += int(sys.argv[b])
    print("{}".format(sum))


if __name__ == "__main__":
    main()
