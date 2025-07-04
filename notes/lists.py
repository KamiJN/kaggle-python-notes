"""
Kaggle Python Course - Days 6: Lists
Notatki: Julia Nowak | Data: 04-07-2025
"""

# =============================================================================
# 1. Indeksowanie & Slicing
# =============================================================================
example_list = [
    ['-', '+', '/'],
    ['1', '1', '2', '3'],
    [5, 'k', "abc"],
]
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
fib_seq = [1, 1, 2, 3, 5, 8]

print(planets[:3]) # output: ['Mercury', 'Venus', 'Earth']
print(planets[1:-1]) # output: ['Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus']
print(planets[-3:]) # output: ['Saturn', 'Uranus', 'Neptune']
print(planets) # output: ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets[2] = 'unknown'
print(planets) # output: ['Mercury', 'Venus', 'unknown', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# =============================================================================
# 2. Funkcje związane z listami
# =============================================================================
# len() - zwraca długość listy.
print(len(planets)) # output: 8
# sorted() - zwraca posortowaną listę.
print(sorted(planets)) # output: ['Jupiter', 'Mars', 'Mercury', 'Neptune', 'Saturn', 'Uranus', 'Venus', 'unknown']
# sum() - zwraca sumę.
print(sum(fib_seq)) # output: 20
# max() & min() - zwraca największą i najmniejszą wartość z listy.
print(max(fib_seq)) # output: 8
print(min(fib_seq)) # output: 1

# =============================================================================
# 3. Wprowadzenie do obiektów
# =============================================================================