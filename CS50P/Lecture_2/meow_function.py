def main():
    num = get_number()
    meow(num)


def get_number():

    while True:
        n = int(input("Enter a number: "))
        if n > 1:
            return n

def meow(n):
    for _ in range(n):
        print("meow")


main()