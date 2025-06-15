"""
Kaggle Python Course - Days 2 & 3: Functions
Notatki: Julia Nowak | Data: 14-06-2025 & 15-06-2025
"""

# =============================================================================
# 1. Docstrings - dokumentowanie kodu
# =============================================================================
def biggest_difference(a, b, c):
    """
    Zwraca największą różnicę między dowolnymi dwiema liczbami spośród a, b i c.
    
    Przykład:
    >>> biggest_difference(-5, 4, 9)
    14
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(c - a)
    return max(diff1, diff2, diff3)

# Test funkcji
print(biggest_difference(-5, 4, 9)) # output: 14
print(help(biggest_difference))

# =============================================================================
# 2. Funkcja print() i argument separatora
# =============================================================================
print("Standardowy print:", 1, 1, 2, 3, 5) 
print("Print z separatorem przecinka:", 1, 1, 2, 3, 5, sep=', ') 
print("Print z separatorem nowej linii:", 1, 1, 2, 3, 5, sep='\n') 

# =============================================================================
# 3. Funkcje jako argumenty (funkcje wyższego rzędu)
# =============================================================================
def mult_by_five(x):
    return x * 5

def call(fun, arg):
    """Wywołuje fun na arg."""
    return fun(arg)

def squared_call(fun, arg):
    """Wywołuje fun na wyniku fun(arg)."""
    return fun(fun(arg))

# Test funkcji
print("\nWyniki funkcji wyższego rzędu:")
print(
    " - mult_by_five(5):", mult_by_five(5), '\n',
    "- call(mult_by_five, 5):", call(mult_by_five, 5), '\n',
    "- squared_call(mult_by_five, 5):", squared_call(mult_by_five, 5)
)

# =============================================================================
# 4. Funkcja max() i argument klucza
# =============================================================================
def mod_five(x):
    return x % 5

# Test funkcji
print(
    "Największa liczba z 41, 32 i 23 to ", 
    max(41, 32, 23),
    ", a liczba, której reszta z dzielenia przez pięć jest największa to ", 
    max(41, 32, 23, key=mod_five)
)
# Funkcja max() z argumentem key stosuje do każdego argumentu 
# przypisaną do key funkcję mod_five, a następnie zwraca ostateczny wynik, 
# jakim jest oryginalny element, którego wartość zwrócona przez key 
# jest największa.

# =============================================================================
# 5. Funkcja round() - zaokrąglanie liczb
# =============================================================================
def round_to_two_places(x):
    """
    Zwróć podaną liczbę, zaokrągloną do dwóch miejsc po kropce.
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    return round(x, 2)

# Test funkcji
print(round_to_two_places(5.5786)) # output: 5.58

print(round(234234234, -1)) # output: 234234230
print(round(234234234, -3)) # output: 234234000
print(round(234234234, -5)) # output: 234200000

# =============================================================================
# 6. Funkcja abs() - wartość absolutna
# =============================================================================
x = -10
y = 5
smallest_abs = min(abs(x), abs(y))

print(smallest_abs) # output: 5