import time

my_time = int(input("Enter time in seconds: "))

for num in reversed(range(1,my_time+1)):
    seconds = num % 60
    minutes = int(num / 60) % 60
    hours = int(num / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Happy New Year!")