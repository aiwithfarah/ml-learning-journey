# Skip number 13 in the counter

for num in range(1, 21):
    if num == 13:
        continue
    print(num)

name = "haraf"

for letter in name:
    if letter == "r":
        break
    print(letter)