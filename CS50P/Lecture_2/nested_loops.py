# Mario

def main():
    print_square(3)

def print_square(size):
    # for each row in square
    for i in range(size): #rows
        # for each brick in row
        for j in range(size): #columns
            # print brick
            print("*", end="")
        print() #newline after each row
main()