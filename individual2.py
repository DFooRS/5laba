import sys

if __name__ == '__main__':
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    if (a + b > c) and (a + c > b) and (b + c > a):
        if a == b == c:
            print("Triangle is equilateral")
        elif (a == b) or (a == c) or (b == c):
            print("Triangle is isosceles")
        else:
            print("Triangle is scalene")
    else:
        print("Triangle does not exist")