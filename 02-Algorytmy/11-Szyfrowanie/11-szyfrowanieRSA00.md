# Szyfr RSA

## Czym jest szyfr RSA?

W wypadku szyfrowania asymetrycznego korzysta się z dwóch kluczy: 
**publicznego do
szyfrowania wiadomości oraz prywatnego – do odszyfrowania.
Nazwa szyfru RSA to skrót od nazwisk trzech profesorów z Massachusetts Institute of
Technology w USA, którzy w 1977 r. opublikowali ten algorytm. Byli to Ronald L. Rivest, Adi
Shamir i Leonard Adleman.
Szyfr RSA to asymetryczny algorytm kryptograficzny. Posiada parę kluczy – publiczny
(e, n) oraz prywatny (d, n).
Postępowanie z użyciem asymetrycznego szyfrowania można sprowadzić do następujących
kroków:
Każda osoba, która chce otrzymać zaszyfrowaną wiadomość, „wystawia” na publiczny
widok swój klucz publiczny.
Osoba chcąca wysłać wiadomość szyfruje ją wykorzystując klucz publiczny osoby, do
której chce ją wysłać.
Osoba, która odbiera wiadomość, odszyfrowuje ją z użyciem swojego klucza
prywatnego. Nikt, kto nie posiada klucza prywatnego, nie jest w stanie odszyfrować
wiadomości.