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
    indeksy = [] #indeksy na ktorych znaleziono wzorzec

    if wzorzecDlugosc > tekstDlugosc or wzorzecDlugosc == 0:
        print("Brak mozliwosci wyszukiwania")
        return indeksy

    for i in range(tekstDlugosc-wzorzecDlugosc+1):  #ostatnia pozycja do sprawdzania to tekstDlugosc-wzorzecDlugosc
                                                    #range konczy na jednym miejscu przed koncem dlatego +1
        for j in range(wzorzecDlugosc):
            if tekst[i+j] != wzorzec[j]:
                break
        else:
            indeksy.append(i)

    return indeksy

def kolorowanie_wzorcow(tekst, wzorzec):
    indeksy = algorytm_wyszukiwania_indeksy(tekst, wzorzec)
    wzorzecDlugosc = len(wzorzec)
    koniec = 0 #slaba nazwa
    wynik = ""

    ZIELONE_TLO = "\033[42m"
    RESET = "\033[0m"

    for indeks in indeksy:
        wynik += tekst[koniec:indeks]
        wynik += ZIELONE_TLO + tekst[indeks:indeks + wzorzecDlugosc] + RESET
        koniec = indeks + wzorzecDlugosc

    wynik += tekst[koniec:]
    print(wynik)






while True:
        print("\n=== MENU ===")
        print("Wpisz '1', aby wyszukać wzorzec w tekście")
        print("Wpisz '2', aby zakończyć program")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            algorytm_wyszukiwania("ala ma kota i ma psa","ma")
            print(algorytm_wyszukiwania_indeksy("ala ma kota i ma psa","ma"))
            kolorowanie_wzorcow("ala ma kota i ma psa","ma")


        elif wybor == "2":
            print("Koniec programu")
            break

        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")




