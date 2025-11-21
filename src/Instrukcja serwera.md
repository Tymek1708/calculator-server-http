# Rzeczy do zrobienia i przydatne komendy

---

## Komendy do testowania serwera-kalkulatora:

- ### curl -v -X PUT 'http://127.0.0.1:8000/kalkulator/' 
  - ### -H 'Accept: application/json, application/json+problem'
  - ### -H 'Content-Type: application/json'
  - ### -d @input_file.json
  - ### | jq "[nazwa_pola_wyjściowego_jsona[0]]" = ładne wyrysowanie outputowego jsona

---

## Ważne informacje
### Przykładowy output dla poprawnego przetworzenia:
#### Nagłówki:
    HTTP/1.1 200 OK <- z jakiegoś powodu opcjonalny
    Content-Type: application/json
#### JSON:
    {"result":[wynik działania]}
#### Razem:
    HTTP/1.1 200 OK <- z jakiegoś powodu opcjonalny
    Content-Type: application/json
    {"result":[wynik działania]}

---

### Przykładowy output dla błędu:
#### Nagłówki:

    HTTP/1.1 400 Bad Request <- z jakiegoś powodu opcjonalny
    Content-Type: application/problem+json
    Content-Language: en
#### JSON:
    {
     "title": "Validation Error",
     "detail": "num1 is missing",
     "status": 400
    }
#### Razem:
    HTTP/1.1 400 Bad Request <- z jakiegoś powodu opcjonalny
    Content-Type: application/problem+json
    Content-Language: en
    {
     "title": "Validation Error",
     "detail": "num1 is missing",
     "status": 400
    }

---

## Ważny [link](https://fastapi.tiangolo.com/tutorial/handling-errors/?h#install-custom-exception-handlers) z informacjami o traktowaniu błędów

---

## Wyjątki, które mogą się pojawić
- ### Niepoprawny format jsona <- obsługiwany automatycznie przez FastAPI
- ### Niepoprawna wartość w polu (nie float) <- obsługiwany automatycznie przez FastAPI
- ### Niepoprawna operacja (operacja nieobsługiwana przez serwer) <- Handled
- ### Niepoprawna operacja (dzielenie przez zero) <- Handled

---

## Freezowanie i instalowanie zależności:

- ### pip install pipreqs
  - ### pipreqs .
- ### python3 -m pip install -r [nazwa pliku requirements].txt
