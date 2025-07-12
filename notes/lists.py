"""
Kaggle Python Course - Days 6 & 7: Lists
Notatki: Julia Nowak | Data: 11-07-2025 & 12-07-2025
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

# =============================================================================
# 5. Zadania - rozwiązania
# ============================================================================= 
# 1)
def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if len(L) < 2:
        return None
    return L[1]

# 2)
def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    return teams[-1][1] # / return teams[len(teams) - 1][1]

# 3)
def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    racers[0], racers[-1] = racers[-1], racers[0] 

# 4)
a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]

# Put your predictions in the list below. Lengths should contain 4 numbers, the
# first being the length of a, the second being the length of b and so on.
lengths = [3, 2, 0, 2]

# 5)
# party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
# A guest is considered 'fashionably late' if they arrived after at least half of the party's guests. However, they must not be the very last guest (that's taking it too far). In the above example, Mona and Gilbert are the only guests who were fashionably late.
# Complete the function below which takes a list of party attendees as well as a person, and tells us whether that person is fashionably late.
def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1
