# Tasks
Prosty projekt do zarządzania zadaniami

## O projekcie

> Projekt ma na celu zademonstrowanie sposobu zbudowania prostej aplikacji
> zawierającej formularz logowania, autoryzację z użyciem tokenu JWT i umożliwiającej
> zarządzanie zadaniami do wykonania.
>
> Projekt powstał przy użyciu języka programowania [Python] w wersji 3,
> wykorzystującego framework [FastAPI] do zbudowania serwera zdolnego przyjmować
> zapytania HTTP. Frontend został zbudowany przy pomocy języka programowania
> [Typescript] i frameworku [Nuxt] w wersji 3, z wykorzystaniem dedykowanej
> temu narzędziu biblioteki komponentów [NuxtUI], korzystającej z frameworku
> [TailwindCSS].
>
> Projekt korzysta z narzędzi [tox] i [Github Actions] w celu przeprowadzenia testów
> jednostkowych z użyciem kilku środowisk i wersji języka Python
>
> Struktura projektu została przemyślana zgodnie z zasadami architektury heksagonalnej.
>
> Szablon projektu został wygenerowany przy użyciu narzędzia [PyScaffold].
>
> W celu ułatwienia wdrożenia projektu wykorzystano narzędzie [Docker]

## Uruchomienie projektu

> Do uruchomienia projektu wymagany jest Docker z funkcją docker compose.
>
> Aby uruchomić projekt należy stworzyć plik `.env` w katalogu backend. Plik zawiera zmienną
> środowiskową `SECRET_KEY`, potrzebną do uruchomienia serwera. Zmienna zawiera klucz haszujący
> tokeny. Przykładowy plik znajduje się we wspomnianym katalogu pod nazwą `.env.example`.
> Plik można skopiować i nadać mu odpowiednią nazwę. Następnie należy zmienić wartość zmiennej
> `SECRET_KEY`. Następnie można uruchomić projekt wykorzystując poniższą instrukcję:

```
docker compose up
```

> Po jej wywołaniu i uruchomieniu kontenera dockerowego projekt dostępny jest pod adresem
> `http://localhost`. Przekierowania obsługuje [nginx].

## Odpowiedź na pytanie

> Hydration error powstaje w przypadku kiedy jest różnica pomiędzy stroną wygenerowaną po
> stronie serwera a stroną utworzoną po stronie klienckiej. Jeśli występują różnice, w konsoli
> przeglądarki pokazuje się ów błąd. We wskazanym przypadku przyczyną błędu są inicjacje
> zmiennych `currentTime` i `onlineTime`. Błąd mogłaby również spowodować również funkcja
> komponowalna (composable) `useTasks()`. Możliwością rozwiązania tego problemu jest
> umieszczenie dwóch powyższych zmiennych w `onMounted`. W przypadku `useTasks` można użyć
> `useAsyncData`. Opcjonalnie można użyć komponentu nuxt `<ClientOnly>` (to że jest to kod
> nuxt można rozpoznać po tym, że funkcje ref nie są explicite importowane), albo w skrajnych
> przypadkach zrezygnować z renderowania strony po stronie serwera (SSR).


[Python]: https://www.python.org
[FastAPI]: https://fastapi.tiangolo.com
[Typescript]: https://www.typescriptlang.org
[Nuxt]: https://nuxt.com
[NuxtUI]: https://ui.nuxt.com
[TailwindCSS]: https://ui.nuxt.com
[tox]: https://tox.wiki/en/latest/config.html
[Github Actions]: https://github.com/features/actions
[TailwindCSS]: https://ui.nuxt.com
[PyScaffold]: https://pyscaffold.org/
[Docker]: https://www.docker.com
[nginx]: https://nginx.org/en/
