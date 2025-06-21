"""
Kaggle Python Course - Days 4 & 5: Booleans & Conditionals
Notatki: Julia Nowak | Data: 21-06-2025 & 22-06-2025
"""

# =============================================================================
# 1. Porównania
# Przykład z funkcją sprawdzającą, czy dana liczba jest nieparzysta.
# =============================================================================
def is_odd(n):
    return n % 2 == 1

# Test funkcji
print("Is -760 odd?", is_odd(-760)) # output: False
print("Is 5 odd?", is_odd(5)) # output: True

