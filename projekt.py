import funkcje as fnk
import csv

# przygotowanie słownika na dane

worekJson = {}

# liczba generowanych jsonów do podania przez użytkownika

ileRazy = int(input("Podaj proszę ile generować jsonów: "))

# zapisanie do słownika wygenerowanych jsonów

for i in range(0, ileRazy):
    worekJson.update({i: fnk.generuj_jsona()})

# print(worekJson)

fnk.menu()
dokonajWyboru = int(input("Wybierz polecenie z listy: "))

if dokonajWyboru == 1:

    # zapis do pliku ustalonych na sztywno informacji z json
    # - - - - - - - - - - - ENDPOINT - 1 - - - - - - - - - -

    with open('json_endpointOne.csv', 'w', encoding='utf-8') as endpointOneCsv:
        doZapisu = csv.writer(endpointOneCsv)
        doZapisu.writerow(['_type', '_id', 'name', 'type', 'latitude', 'longitude'])  # tytuły dla danych

        for i in range(0, ileRazy):
            doZapisu.writerow([worekJson[i]['_type'], worekJson[i]['_id'], worekJson[i]['name'], worekJson[i]['type'], worekJson[i]['geo_position']['latitude'], worekJson[i]['geo_position']['longitude']])

    # zapis do pliku informacji ustalonych przez uzytkownika
    # - - - - - - - - - - - ENDPOINT - 2 - - - - - - - - - -

elif dokonajWyboru == 2:

    coWybrac = input("Wskaż, które dane zapisać: ")

    # rozdzielenie wyrazów po przecinku

    listaDanych = coWybrac.split(', ')

    # zapis do pliku informacji wybranych przez użytkownika

    with open('json_endpointTwo.csv', 'w', encoding='utf-8') as endpointTwoCsv:
        doZapisu = csv.writer(endpointTwoCsv)
        doZapisu.writerow(listaDanych)  # tytuły dla danych

        tabs = []  # przygotwanie listy na tymczasowe dane

        for i in range(0, ileRazy):
            for j in range(0, len(listaDanych)):
                try:
                    if listaDanych[j] != 'latitude' and listaDanych[j] != 'longitude':
                        tabs.append(worekJson[i][listaDanych[j]])
                    else:
                        tabs.append(worekJson[i]['geo_position'][listaDanych[j]])
                except(KeyError):
                    print("Nie ma takiej informacji w json")
                    break
            doZapisu.writerow(tabs)
            tabs.clear()

else:
    print("Zły wybór")
