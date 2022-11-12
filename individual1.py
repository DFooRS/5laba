import sys

if __name__ == '__main__':
    print("Seasons:\n"
          "1 - winter\n"
          "2 - spring\n"
          "3 - summer\n"
          "4 - autumn\n")
    n = int(input("Enter season: "))

    if n == 1:
        print("December, January, February")
    elif n == 2:
        print("March, April, May")
    elif n == 3:
        print("June, July, August")
    elif n == 4:
        print("September, October, November")
    else:
        print("Error!", file=sys.stderr)
        exit(1)

