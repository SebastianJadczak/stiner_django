**Stiner** - Z nami zwiedzisz cały świat.

**Autor:** Sebastian Jadczak

**Nazwa systemu:** Stiner

**Prototym systemu:** [https://stiner-dev.herokuapp.com/](https://stiner-dev.herokuapp.com/)

**Grupa docelowa:** Brak grupy docelowej systemu, system jest nastawiony dla wszystkich ludzi chcących aktywnie spędzić czas wakacji, ferii, weekendu.

**Cel systemu:** Celem systemu jest danie możliwości wszystkich ludziom zapoznanie się z:

- Zabytkami
- Stadionami
- Parkami
- Miejscami aktywnego wypoczynku

na terenie całego kraju (Polska). W miarę rozwoju systemu planowana jest ekspansja na Europę jak i cały świat aby poszerzyć bazę dostępnych atrakcji.

**Opis systemu:**

System zawiera 5 głównych zakładek odpowiadającym innej potrzebie klienta:

1. **Mapa** - Na stronie głównej dostępna jest mapa Polski (domyślnie zoom na Warszawę) a na niej zaznaczone miejsca warte zobaczenia.

- Punkty przedstawione w formie graficznej w lokalizacji danego miejsca, po kliknięciu w dany punkt rozwijany jest dymek z skróconym opisem danego miejsca i możliwością przejścia do opisu konkretnego punktu.
- Na głównej stronie istnieje wyszukiwarka która filtruje elementy wg kategorii obiektu np:
  - Zamki
  - Parki
  - Kościoły
  - Muzea
  - Kina/Teatry
  - Hotele/Aqua parki

Użytkownik ma możliwość odfiltrowania tylko te elementy które chce zobaczyć

1. **Trasy zwiedzania -** Zakładka ta podzielona jest na 4 podstrony a każda podstrona ma inne funkcjonalności.
  1. **Ciekawe miejsca:** W tej podzakładce istnieje cała baza danych wszystkich dostępnych punktów na mapie.

Istnieje możliwość ich filtrowania, **po nazwie** , **typie, lokalizacji** czy ocenie użytkowników.

Po kliknięciu w dany punkt rozwija się podstrona danego punktu a w nim:

- **galeria zdjęć danego punktu**
- **opis danego miejsca**
- **krótki zarys historyczny**
- **ocena i opinie o danym miejscu**
- **Dla zalogowanych użytkowników:**  **Możliwość oceniania i komentowania danego punktu**

  1. **Trasy zwiedzania:** W tej zakładce istnieje możliwość Zobaczenia gotowych tras zwiedzania, filtrowania ich wg potrzeb użytkownika np po: lokalizacji, ocenie, nazwie, popularności.

Na głównej stronie podzakładki dostępne trzy widoki tras:

- wszystkie
- najwyżej oceniane
- najpopularniejsze

Po kliknięciu w daną trasę użytkownik będzie miał możliwość:

- zapoznania się z reprezantacją graficzna danej trasy w postacji mapy.
- Przeczytanie informacji o wszystkich punktach
- **Dla zalogowanych użytkowników:**
  - **Skomentowanie i ocenie trasy**
  - **Odsłuchanie trasy w formie audio** (i po opłaceniu abonamentu)

  1. **Twoje trasy -** zakładka ta będzie przechowywać wszystkie trasy zwiedzania stworzone przez użytkownika **(funkcjonalność dostępna tylko dla zalogowanych użytkowników)**. Użytkownik będzie miał możliwość filtrowania swoich tras np. po: nazwie, odległości, mieście.

  1. **Stwórz trasę -** **(funkcjonalność dostępna tylko dla zalogowanych użytkowników)**. Użytkownik na podstawie listy Wszystkich punktów dostępnych w systemie będzie mieć możliwość stworzenie swojej własnej autorskiej trasy zwiedzania z możliwością odtworzenia jej i edycji w zakładce **Twoje trasy.**

Dodatkowo użytkownik będzie miał możliwość Filtrowania tras.

1. **Blog -** Wszyscy użytkownicy będą mogli w tym miejscu poczytać wpisy na tematy podróżnicze.
2. **Sklep -** W tym miejscu użytkownicy będą mogli zakupić wycieczki dostępne w &#39;realu&#39; przez przewodników zaprzyjaźnionych z systemem. Potrzebny sprzęt podróżniczy, czy dostęp do nagrań audio dostępnych tras.
3. **Kontakt -** Podstrona będzie zawierała informacje do kontaktu z pracownikami systemu oraz formularz wysyłania zapytań.

**Role i uprawnienia:**

System przewiduje następujące role:

1. Niezalogowany użytkownik:
  1. będzie mieć możliwość przeglądania tras zwiedzania i punktów
  2. korzystać z pomocy technicznej
  3. korzystać z mapy i filtracji punktów na mapie (strona główna)
2. Zalogowany użytkownik:

1. Wszystko to co Niezalogowany użytkownik
2. Możliwość dokonania zakupów w sklepie internetowym
3. Zmiana swoich danych
4. generowanie tras zwiedzania
5. Ocenianie i pisanie opinii tras i punktów
