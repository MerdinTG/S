# Zadanie 1: Sprawdzenie liczby parzystej lub nieparzystej
# Ten program sprawdza, czy wprowadzona liczba jest parzysta czy nieparzysta.
liczba = int(input('Podaj liczbę całkowitą: '))

if liczba % 2 == 0:
    print('Liczba jest parzysta.')
else:
    print('Liczba jest nieparzysta.')


# Zadanie 2: Ocena na podstawie wyniku
# Program przyjmuje wynik studenta i ocenia go w skali: 0-60: niedostateczny, 61-70: dostateczny, 71-80: dobry, 81-90: bardzo dobry, 91-100: celujący.
wynik = int(input('Podaj wynik (0-100): '))

if wynik < 0 or wynik > 100:
    print('Nieprawidłowy wynik.')
elif wynik <= 60:
    print('Ocena: niedostateczny')
elif wynik <= 70:
    print('Ocena: dostateczny')
elif wynik <= 80:
    print('Ocena: dobry')
elif wynik <= 90:
    print('Ocena: bardzo dobry')
else:
    print('Ocena: celujący')


# Zadanie 3: Sprawdzenie wieku
# Program sprawdza, czy użytkownik jest pełnoletni (18 lat i więcej).
wiek = int(input('Podaj swój wiek: '))

if wiek >= 18:
    print('Jesteś pełnoletni.')
else:
    print('Nie jesteś pełnoletni.')


# Zadanie 4: Trzy liczby - największa
# Program znajduje największą z trzech wprowadzonych liczb.
a = float(input('Podaj pierwszą liczbę: '))
b = float(input('Podaj drugą liczbę: '))
c = float(input('Podaj trzecią liczbę: '))

if a >= b and a >= c:
    print('Największa liczba to:', a)
elif b >= a and b >= c:
    print('Największa liczba to:', b)
else:
    print('Największa liczba to:', c)


# Zadanie 5: Miesiąc na podstawie liczby
# Program przyjmuje numer miesiąca i wyświetla jego nazwę.
numer_miesiaca = int(input('Podaj numer miesiąca (1-12): '))

if numer_miesiaca == 1:
    print('Styczeń')
elif numer_miesiaca == 2:
    print('Luty')
elif numer_miesiaca == 3:
    print('Marzec')
elif numer_miesiaca == 4:
    print('Kwiecień')
elif numer_miesiaca == 5:
    print('Maj')
elif numer_miesiaca == 6:
    print('Czerwiec')
elif numer_miesiaca == 7:
    print('Lipiec')
elif numer_miesiaca == 8:
    print('Sierpień')
elif numer_miesiaca == 9:
    print('Wrzesień')
elif numer_miesiaca == 10:
    print('Październik')
elif numer_miesiaca == 11:
    print('Listopad')
elif numer_miesiaca == 12:
    print('Grudzień')
else:
    print('Nieprawidłowy numer miesiąca.')


# Zadanie 6: Kalkulator - dodawanie, odejmowanie
# Program działa jako prosty kalkulator, wykonując dodawanie lub odejmowanie w zależności od wyboru.
opcja = input('Wybierz opcję (+ lub -): ')
liczba1 = float(input('Podaj pierwszą liczbę: '))
liczba2 = float(input('Podaj drugą liczbę: '))

if opcja == '+':
    print('Wynik:', liczba1 + liczba2)
elif opcja == '-':
    print('Wynik:', liczba1 - liczba2)
else:
    print('Nieprawidłowa opcja.')


# Zadanie 7: Sprawdzanie roku przestępnego
# Program sprawdza, czy dany rok jest rokiem przestępnym.
rok = int(input('Podaj rok: '))

if (rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0):
    print('Rok jest przestępny.')
else:
    print('Rok nie jest przestępny.')