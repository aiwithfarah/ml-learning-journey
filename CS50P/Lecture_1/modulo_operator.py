def main():
    num = int(input("Enter a number: "))
    x = is_even(num)
    print(x)

def is_even(n):
    if n%2 == 0:
        return "Even"
    else:
        return "Odd"
    
main()