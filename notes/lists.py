"""
Kaggle Python Course - Days 6 & 7: Lists
Notatki: Julia Nowak | Data: 04-07-2025 & 05-07-2025
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
# 3. Przykładowe metody list
# ============================================================================= 
# list.append() - dodaje nowy element na koniec listy
print(planets.append('Pluto')) # output: None, nic nie zwraca
print(planets) # output: ['Mercury', 'Venus', 'unknown', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
# list.pop() -  usuwa i zwraca ostatni element listy
print(planets.pop()) # output: Pluto
print(planets) # ['Mercury', 'Venus', 'unknown', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# list.index() - zwraca indeks podanego elementu, jeśli go nie ma, zwraca błąd
print(planets.index('Saturn')) # output: 5
# Aby uniknąć błędu, można skorzystać z operatora "in":
if "Earth" in planets:
    print(planets.index('Earth'))
else:
    print("Goodbye World!")

# =============================================================================
# 4. Krotki (ang. "Tuples")
# ============================================================================= 
# Różnią się od list głównie deklaracją i niemożnością ich późniejszej modyfikacji
t1 = 'a', 'b', 'c'
t2 = ('d', 'e', 'f')
t3 = 11, 13, 17
print(t1) # output: ('a', 'b', 'c')
# t1[0] = 'A' # ERROR!

# Używane są często przy funkcjach, zwracających więcej niż jedną wartość.
# as_integer_ratio() - metoda obiektów typu 'float', która zwraca licznik i mianownik w formie krotki.
x = 0.125
print(x.as_integer_ratio()) # output: (1, 8)
numerator, denominator = x.as_integer_ratio()
print(numerator / denominator) # output: 0.125
