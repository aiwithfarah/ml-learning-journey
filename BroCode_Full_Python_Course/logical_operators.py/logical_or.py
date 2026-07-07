temp = 15
is_raining = False

# if temp is too hot, too cold, or it's raining - event will be cancelled
if 35 < temp or temp < 16 or is_raining:
    print("Outdoor event is cancelled")
else:
    print("Outdoor event is not cancelled")

