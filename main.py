import time


def algorytm_wyszukiwania(tekst,wzorzec):
    start1 = time.perf_counter()
    tekstDlugosc=len(tekst)
    wzorzecDlugosc=len(wzorzec)

    ostatni = 0
    wynik = ""

    zielony = "\033[92m"
    bialy = "\033[0m"

    znaleziono = 0

    i = 0

    while  i <= tekstDlugosc - wzorzecDlugosc:
        j = 0
        while j < wzorzecDlugosc and tekst[i + j] == wzorzec[j]:
            j += 1

        if j == wzorzecDlugosc:
            wynik += tekst[ostatni:i] + zielony + tekst[i:i+wzorzecDlugosc] + bialy
            znaleziono += 1
            ostatni = i + wzorzecDlugosc
            i += wzorzecDlugosc
            print(wynik)
            while(True):

                koniec1 = time.perf_counter()
                print("Czas wykonania algorytmu:", koniec1 - start1, "sekundy")
                print("Czy chcesz kontynuować wyszukiwanie? (tak/nie)")
                odpowiedz = input().strip().lower()
                if odpowiedz == "tak":
                    ostatni = i + wzorzecDlugosc
                    break
                elif odpowiedz == "nie":
                    print("Koniec wyszukiwania. Twój wynik to: " + wynik)
                    return
                else:
                    print("Nieprawidłowy wybór, spróbuj ponownie.")
        else:
            i += 1

    if(znaleziono == 0):
        print("Nie znaleziono wzorca w tekście.")
        return
    print("Koniec wyszukiwania. Twój wynik to: " + wynik + tekst[ :tekstDlugosc])


def algorytm_wyszukiwania_indeksy(tekst,wzorzec):
    tekstDlugosc = len(tekst)
    wzorzecDlugosc = len(wzorzec)
    indeksy = []

    if wzorzecDlugosc > tekstDlugosc or wzorzecDlugosc == 0:
        return indeksy

    for i in range(tekstDlugosc-wzorzecDlugosc+1):
        for j in range(wzorzecDlugosc):
            if tekst[i+j] != wzorzec[j]:
                break
        else:
            indeksy.append(i)

    return indeksy

def kolorowanie_wzorcow(tekst, wzorzec):
    start2 = time.perf_counter()

    indeksy = algorytm_wyszukiwania_indeksy(tekst, wzorzec)

    koniec2 = time.perf_counter()
    czas_wykonania = koniec2 - start2

    if len(indeksy) == 0:
        print("Nie znaleziono wzorca w tekście.")
        return

    wzorzecDlugosc = len(wzorzec)
    ostatni = 0
    wynik = ""

    zielony = "\033[92m"
    reset = "\033[0m"

    for i in indeksy:
        if i < ostatni:
            continue

        wynik += tekst[ostatni:i]
        wynik += zielony + tekst[i:i + wzorzecDlugosc] + reset

        ostatni = i + wzorzecDlugosc
        print(wynik)

        while True:
            koniec2 = time.perf_counter()
            print("Czas wykonania algorytmu:", czas_wykonania, "sekundy")
            print("Czy chcesz kontynuować wyszukiwanie? (tak/nie)")
            odpowiedz = input().strip().lower()
            if odpowiedz == "tak":
                break
            elif odpowiedz == "nie":
                print("Koniec wyszukiwania. Twój wynik to:")
                print(wynik + tekst[ostatni:])
                return
            else:
                print("Nieprawidłowy wybór, spróbuj ponownie.")

    wynik += tekst[ostatni:]
    print("Koniec wyszukiwania. Twój wynik to:")
    print(wynik)






while True:
        print("\n=== MENU ===")
        print("Wpisz '1', aby wyszukać wzorzec w tekście")
        print("Wpisz '2', aby zobaczyć przykładowe działanie algorytmu")
        print("Wpisz '3', aby zakończyć program")

        if ('a' == 'A'):
            print ("Test to samo")
        else:
            print ("Test różne")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            while True:
                tekst = input("Wprowadź tekst: ")
                wzorzec = input("Wprowadź wzorzec do wyszukania: ")

                if tekst == "":
                    print("Tekst nie może być pusty. Spróbuj ponownie.")
                    continue
                if wzorzec == "":
                    print("Wzorzec nie może być pusty. Spróbuj ponownie.")
                    continue
                if len(wzorzec) > len(tekst):
                    print("Wzorzec nie może być dłuższy niż tekst. Spróbuj ponownie.")
                    continue
                if len(tekst) > 50_000:
                    print("Tekst za długi.")
                    continue
                break

          #  algorytm_wyszukiwania(tekst, wzorzec)
           # print()
            kolorowanie_wzorcow(tekst, wzorzec)

        elif wybor == "2":
            print("1. Standardowe dane")
            tekst = "ala ma kota i ma psa"
            wzorzec = "ma"
            print("Tekst:", tekst)
            print("Wzorzec:", wzorzec)

#            algorytm_wyszukiwania(tekst, wzorzec)
            #print()
            kolorowanie_wzorcow(tekst, wzorzec)

            print("\n2. Najlepszy przypadek")
            tekst = "super przedmiot"
            wzorzec = "super"

            print("Tekst:", tekst)
            print("Wzorzec:", wzorzec)

    #        algorytm_wyszukiwania(tekst, wzorzec)
          #  print()
            kolorowanie_wzorcow(tekst, wzorzec)

            print("\n3. Najgorszy przypadek")
            tekst = "a" * 200 + "b"
            wzorzec = "aaab"

            print("Tekst:", tekst)
            print("Wzorzec:", wzorzec)

       #     algorytm_wyszukiwania(tekst, wzorzec)
         #   print()
            kolorowanie_wzorcow(tekst, wzorzec)

        elif wybor == "3":
            print("Koniec programu")
            break

        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")
