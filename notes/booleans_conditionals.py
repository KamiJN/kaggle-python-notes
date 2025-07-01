"""
Kaggle Python Course - Days 4 & 5: Booleans & Conditionals
Notatki: Julia Nowak | Data: 21-06-2025 & 28-06-2025
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

# =============================================================================
# 2. Warunki 
# =============================================================================
def inspect(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else:
        print(x, "is unlike anything I've ever seen...")

inspect(10) # output: 10 is positive
inspect(0) # output: 0 is zero
inspect(-14) # output: -14 is negative

# =============================================================================
# 3. Łączenie warunków i wartości zmiennych bool - za pomocą "and", "or" i "not" 
# =============================================================================
def can_run_for_president(age, is_citizen):
    return is_citizen and (age >= 35)

print(can_run_for_president(19, True)) # output: False
print(can_run_for_president(55, False)) # output: False
print(can_run_for_president(55, True)) # output: True

# =============================================================================
# 4. Funkcja bool() i konwersja 
# =============================================================================
if 0:
    print(0)
elif "spam":
    print("spam")
# output: spam

# Wszystkie wartości liczbowe traktowane są jako prawda, z wyjątkiem zera.
print(bool(1)) # output: True 
print(bool(0)) # output: False
# Wszystkie ciągi znaków traktowane są jako prawda, z wyjątkiem pustych ciągów znaków.
print(bool("xyz")) # output: True 
print(bool("")) # output: False
# Ogólnie rzecz biorąc, puste ciągi znaków, listy, itd. są traktowane jako fałsz, a reszta jako prawda.

# =============================================================================
# 5. Funkcja sprawdzająca przygotowanie na opady deszczu.
# =============================================================================
def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    #return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday # output: False (przy poniższym założeniu)
    return have_umbrella or rain_level < 5 and have_hood or not (rain_level > 0 and is_workday)

have_umbrella = False
rain_level = 5
have_hood = False
is_workday = False

actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual) # output: True

# =============================================================================
# 6. Instrukcja pass - zastępuje przyszły kod, po jej wywołaniu nic się nie dzieje - nie doprowadza ona do błędu.
# Przydaje się, gdy zostanie zostawiona pusta pętla, warunek, itd. 
# =============================================================================

# =============================================================================
# 7. Funkcje zwracające "True", według podanego opisu warunku.
# =============================================================================
def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return ketchup and mustard and onion

def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not (ketchup or mustard or onion) # / return not ketchup and not mustard and not onion

def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return (ketchup or mustard) and not (ketchup and mustard) # / return (ketchup and not mustard) or (mustard and not ketchup)
