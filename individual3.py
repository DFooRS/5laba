import sys
import math

if __name__ == '__main__':
    k = int(input("Enter k: "))

    i = 2
    while i <= math.sqrt(k):
        if k % i == 0:
            print("0")
            break
        i += 1
    else:
        print("1")