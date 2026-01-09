def algorytm_wyszukiwania(tekst,wzorzec):

    tekstDlugosc=len(tekst)
    wzorzecDlugosc=len(wzorzec)

    #if wzorzecDlugosc>tekstDlugosc or wzorzecDlugosc==0:
     #   return wynik

    for i in range(tekstDlugosc):
        if i + wzorzecDlugosc > tekstDlugosc:
            break
        j = 0
        while j < wzorzecDlugosc and tekst[i + j] == wzorzec[j]:
            j += 1
        if j == wzorzecDlugosc:
            wynik = tekst[0:i] + "[" + tekst[i:i+wzorzecDlugosc] + "]"
            print(wynik)



while True:
        print("=== MENU ===")
        print("Wpisz '1', aby wyszukać wzorzec w tekście")
        print("Wpisz '2', aby zakończyć program")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            print("1 dziala")
            algorytm_wyszukiwania("ala ma kota","ma")


        elif wybor == "2":
            print("Koniec programu")
            break

        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")




