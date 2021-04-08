# API z użytkownikami

Uruchomienie serwera:
`python manage.py runserver`

logowanie do django admin (`127.0.0.1:8000/admin/`) jako superuser:
```
   login: gov-user
   password: gov-user-dev
```

Aby uzyskać token do API wysyłamy POST na `http://127.0.0.1:8000/api-token-auth/` i przekazujemy parametry:
```
{
    "username":"gov-user", 
    "password": "gov-user-dev"
}
```
W odpowiedzi otrzymujemy token, aby pobrać dane z API:

`GET http://127.0.0.1:8000/gov-api/person/<pesel>/ "Authorization: Token XXXXX...."`
