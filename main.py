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
    indeksy = algorytm_wyszukiwania_indeksy(tekst, wzorzec)

    if len(indeksy) == 0:
        print("Nie znaleziono wzorca w tekście.")
        return

    wzorzecDlugosc = len(wzorzec)
    ostatni = 0
    wynik = ""

    zielony = "\033[42m"
    reset = "\033[0m"

    for i in indeksy:
        if i < ostatni:
            continue

        wynik += tekst[ostatni:i]
        wynik += zielony + tekst[i:i + wzorzecDlugosc] + reset

        ostatni = i + wzorzecDlugosc
        print(wynik)

        while True:
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
                if len(tekst) > 1_000:
                    print("Tekst za długi.")
                    continue
                break

            kolorowanie_wzorcow(tekst, wzorzec)

        elif wybor == "2":
            print("1. Standardowe dane")
            tekst = "ala ma kota i ma psa"
            wzorzec = "ma"
            print("Tekst:", tekst)
            print("Wzorzec:", wzorzec)

            kolorowanie_wzorcow(tekst, wzorzec)

            print("\n2. Najlepszy przypadek")
            tekst = "super przedmiot"
            wzorzec = "super"

            print("Tekst:", tekst)
            print("Wzorzec:", wzorzec)

            kolorowanie_wzorcow(tekst, wzorzec)

            print("\n3. Najgorszy przypadek")
            tekst = "a" * 200 + "b"
            wzorzec = "aaab"

            print("Tekst:", tekst)
            print("Wzorzec:", wzorzec)

            kolorowanie_wzorcow(tekst, wzorzec)

        elif wybor == "3":
            print("Koniec programu")
            break

        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")
