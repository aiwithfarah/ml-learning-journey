temp = 30
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside & it's sunny!")
elif temp <= 0 and is_sunny:
    print("It is cold outside and it's sunny!")
elif 28 > temp > 0 and is_sunny:
    print("It is Warm Outside!") 
else:
    print("It is not Hot outside!")