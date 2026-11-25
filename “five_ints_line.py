#!/usr/bin/env python3
# Created By: Maeva Tchuenga
# Date: 11, 24 2026
# This program is to enter numbers from 1000 t0 2000


def main():
    # process the numbers in a loop.
    for counter in range(1000, 2001):
        print(counter, end=" ")
        if counter % 5 == 0:
            print(counter)


if __name__ == "__main__":
    main()
