import random

# dane do losowań

iata = ["GDN", "KTW", "KRK", "RZE", "WAW", "WRO", "BRE", "DRS", "HAM", "CGN", "STR"]
miasto = ["Gdynia", "Katowice", "Kraków", "Rzeszów", "Warszawa", "Wrocław", "Brema", "Drezno", "Hamburg", "Kolonia", "Stuttgart"]
kraj = ["Polska", "Niemcy"]
kodKraju = ["PL", "DE"]

wielkoscTabelki = (len(iata) - 1)  # ustalenie wartosci do losowania na podstawie wielkosci tabelki


# funkcja wyświetlająca menu

def menu():
    print("Wybierz jedną z poniższych opcji: ")
    print("1. Zapisz dane: '_type, _id, name, type, latitude, longitude' do pliku csv")
    print("""2. Wybierz dane z listy wymieniając je po przecinku, aby następnie zapisać je do pliku csv:
         _type, _id, name, fullName, iata_airport_code, type, country, geo_position,
         latitude, longitude, location_id, inEurope, countryCode.""")


# losowanie liczby do tabel

def generuj_liczbe_losowa(tabelka):
    return random.randint(0, tabelka)


# ustalenie kraju dla wylosowanej liczby

def jaki_kraj(wylosowanaLiczba):
    if wylosowanaLiczba < 6:  # 6 dlatego, że w tabelce iata zmienia się kraj
        return 0
    else:
        return 1


# funkcja generująca wartości float zaokrąglone do 7 miejsc po przecinku, dla współrzędnych

def generuj_wspolrzedne():
    liczbaFloat = random.random()
    return round(liczbaFloat * 100, 7)


# funkcja generująca 8 cyfrową liczbę do ID

def generuj_ID():
    return random.randint(22334455, 99999999)


# funkcja generująca 6 cyfrową liczbę do location_ID

def generuj_locationID():
    return random.randint(223344, 999999)


# funkcja generująca chociaż część danych json przy wykorzystaniu powyższych funkcji

def generuj_jsona():

    liczbaLosowa = generuj_liczbe_losowa(wielkoscTabelki)

    ustalKraj = jaki_kraj(liczbaLosowa)

    przykladJson = {"_type": "Position", "_id": generuj_ID(), "key": None, "name": miasto[liczbaLosowa], "fullName": miasto[liczbaLosowa] + ", " + kraj[ustalKraj], "iata_airport_code": iata[liczbaLosowa], "type": "location", "country": kraj[ustalKraj], "geo_position": {"latitude": generuj_wspolrzedne(), "longitude": generuj_wspolrzedne()}, "location_id": generuj_locationID(), "inEurope": True, "countryCode": kodKraju[ustalKraj], "coreCountry": True, "distance": None}
    return przykladJson
