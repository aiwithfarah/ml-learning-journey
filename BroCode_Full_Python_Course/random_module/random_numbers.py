import random 

low = 1
high = 100

random_int= random.randint(low, high)

print(random_int)

random_float = random.random()
print(random_float)

options = ("heads", "tails", "none")
print(random.choice(options))

cards = ['a', 'b', 'c', 'd', 1, 2, 3, 4]
random.shuffle(cards)
print(cards) #[3, 2, 'c', 'b', 1, 'd', 4, 'a']