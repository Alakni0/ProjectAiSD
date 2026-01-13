def algorytm_wyszukiwania(tekst,wzorzec):

    tekstDlugosc=len(tekst)
    wzorzecDlugosc=len(wzorzec)
    ostatni = 0
    wynik = ""
    zielony = "\033[92m"
    bialy = "\033[0m"

    if wzorzecDlugosc>tekstDlugosc or wzorzecDlugosc==0:
        print("Brak mozliwosci wyszukiwania")
        return

    for i in range(tekstDlugosc):
        if i + wzorzecDlugosc > tekstDlugosc:
            break
        j = 0
        while j < wzorzecDlugosc and tekst[i + j] == wzorzec[j]:
            j += 1

        if j == wzorzecDlugosc:
            wynik += tekst[ostatni:i] + zielony + tekst[i:i+wzorzecDlugosc] + bialy
            print(wynik)



            while(True):
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

    print("Koniec wyszukiwania. Twój wynik to: " + wynik + tekst[ostatni:tekstDlugosc])


def algorytm_wyszukiwania_indeksy(tekst,wzorzec):
    tekstDlugosc = len(tekst)
    wzorzecDlugosc = len(wzorzec)
    indeksy = []

    if wzorzecDlugosc > tekstDlugosc or wzorzecDlugosc == 0:
        print("Brak mozliwosci wyszukiwania")
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
    wzorzecDlugosc = len(wzorzec)
    ostatni = 0
    wynik = ""

    zielony = "\033[92m"
    reset = "\033[0m"

    for i in indeksy:
        wynik += tekst[ostatni:i]
        wynik += zielony + tekst[i:i + wzorzecDlugosc] + reset

        print(wynik)

        while True:
            print("Czy chcesz kontynuować wyszukiwanie? (tak/nie)")
            odpowiedz = input().strip().lower()
            if odpowiedz == "tak":
                ostatni = i + wzorzecDlugosc
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



#metody ktore sprawdzaja wydajnosc algorytmu dodac tutaj



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
                break

            algorytm_wyszukiwania(tekst, wzorzec)
            print()
            kolorowanie_wzorcow(tekst, wzorzec)

        elif wybor == "2":
            tekst = "ala ma kota i ma psa"
            wzorzec = "ma"

            algorytm_wyszukiwania(tekst, wzorzec)
            print()
            indeksy = algorytm_wyszukiwania_indeksy(tekst, wzorzec)
            print("Znalezione indeksy:", indeksy)
            kolorowanie_wzorcow(tekst, wzorzec)

        elif wybor == "3":
            print("Koniec programu")
            break

        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")
