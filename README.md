# Sortowanie adresów e-mail

Prosty program napisany w Pythonie, który wczytuje plik zawierający adresy e-mail i sortuje je według domen, tworząc osobne pliki tekstowe dla każdej domeny.

## Wymagania

Aby uruchomić ten program, wymagane jest zainstalowanie biblioteki `tkinter`. Możesz zainstalować ją, wykonując polecenie:

```bash
$ pip install -r requirements.txt
```

## Jak korzystać

1. Uruchom program komendą `py main.py`.
2. Po uruchomieniu programu wciśnij dowolny przycisk, aby wybrać plik zawierający adresy e-mail do posortowania.
3. Wybierz plik zawierający adresy do posortowania w formacie `email:haslo`
4. Po wybraniu pliku program utworzy osobne pliki dla każdej domeny adresów e-mail i zapisze je w bieżącym katalogu.

## Jak dodać własne domeny

1. Otwórz plik config.json
2. Dodaj na końcu:
```
  	"Nazwa pliku": [
      "@twojadomena.xyz"
      "@twojadomena2.xyz"
    ]
 ```

## TODO

1. ~~Wybór katalogu do eksportu~~
2. Optymalizacja kodu
3. ~~Dodać automatyczne usuwanie capture~~
4. ~~Plik json z możliwością ustawiania własnych domen itp (ogólnie konfiguracyjny)~~
5. Możliwość wczytania kilku plików na raz/folder input


Program napisany z dedykacją dla:
![](https://imgur.com/R5zmVzA.png)