#create a dict of countaries and capitals

capitals = {
    'India' : 'New Delhi',
    'Australia' : 'Canbera ',
    'Canada' : 'Ottawa',
    'France' : 'Paris',
    'Russia' : 'Moscow',
}

# Get values from a dictionary by accessing the key
print(capitals['Russia']) #Moscow

# Or use .get method
print(capitals.get('Russia'))

# .get() returns Noneif the key does not exist
print(capitals.get('Japan')) #None

# Create new key:value pair using .update()
capitals.update({"Germany" : "Berlin"})
print(capitals)
# {'India': 'New Delhi', 'Australia': 'Canbera ', 'Canada': 'Ottawa', 'France': 'Paris', 'Russia': 'Moscow', 'Germany': 'Berlin'}

# Update existing key:value pair using .update()
capitals.update({'Canada' : 'Toronto'})

print(capitals)
#{'India': 'New Delhi', 'Australia': 'Canbera ', 'Canada': 'Toronto', 'France': 'Paris', 'Russia': 'Moscow', 'Germany': 'Berlin'}

capitals.pop('India')
print(capitals)
# {'Australia': 'Canbera ', 'Canada': 'Toronto', 'France': 'Paris', 'Russia': 'Moscow', 'Germany': 'Berlin'}

# removes lates key:value pair We don't need to pass a key
capitals.popitem()
print(capitals)
# {'Australia': 'Canbera ', 'Canada': 'Toronto', 'France': 'Paris', 'Russia': 'Moscow'}

print(capitals.keys())
# dict_keys(['Australia', 'Canada', 'France', 'Russia'])

for key in capitals.keys():
    print(key)

# Australia
# Canada
# France
# Russia    

print(capitals.values()) #dict_values(['Canbera ', 'Toronto', 'Paris', 'Moscow'])   

for value in capitals.values():
    print(value)

# Canbera 
# Toronto
# Paris
# Moscow

print(capitals.items())
#dict_items([('Australia', 'Canbera '), ('Canada', 'Toronto'), ('France', 'Paris'), ('Russia', 'Moscow')])

for key,value in capitals.items():
    print(f"{key} : {value}")

# Australia : Canbera
# Canada : Toronto
# France : Paris
# Russia : Moscow
