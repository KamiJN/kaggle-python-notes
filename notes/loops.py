"""
Kaggle Python Course - Days 8 & 9: Loops and List Comprehensions
Notatki: Julia Nowak | Data: 14-07-2025 & 15-07-2025
"""

# =============================================================================
# 1. Pętle
# =============================================================================
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=', ') 
# output: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, 

for planet in planets:
    print(planet, end="\n") 
# output: 
# Mercury
# Venus
# Earth
# Mars
# Jupiter
# Saturn
# Uranus
# Neptune

multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
print(product) # output: 360

text = "integeR efficitur, sApien eget porttitor interDum, dIAm felis efficitur Nisi, nec Tempus lectus arcu in diam"
for char in text:
    if char.isupper():
        print(char, end='') # output: RADIANT

# RANGE()
for i in range(5):
    print("Learning. i =", i)
# output: 
# Learning. i = 0
# Learning. i = 1
# Learning. i = 2
# Learning. i = 3
# Learning. i = 4

# PĘTLE WHILE
i = 1
while i < 64:
    print(i, end=' ')
    i *= 2 # output: 1 2 4 8 16 32

# =============================================================================
# 2. Wyrażenia list
# =============================================================================
# 1)
"""
squares = []
for n in range(10):
    squares.append(n**2)
print(squares) # output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
"""
squares = [n**2 for n in range(10)]
print(squares) # output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 2)
long_planets = [planet.upper() + "." for planet in planets if len(planet) > 6]
print(long_planets) # output: ['Mercury', 'Jupiter', 'Neptune']
"""
long_planets = [
    planet.upper() + "." 
    for planet in planets 
    if len(planet) > 6]
Zapis podobny do struktury kwerend w SQL (SELECT, FROM, WHERE).
"""

# 3)
'''
def count_negatives(nums):
    """Return the number of negative numbers in the given list.
    
    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative
'''
def count_negatives(nums):
    return len([num for num in nums if num < 0])