# Szyfr Vigenère’a

## Opis szyfru Vigenère’a

Szyfr Vigenère’a to klasyczny szyfr podstawieniowy używający serii szyfrów 
Cezara opartych na literach klucza. Zamiast przesuwać wszystkie litery 
o tę samą wartość (jak w Cezarze), każda litera tekstu jawnego jest 
przesuwana o wartość odpowiadającą literze klucza.

Alfabet ma 26 liter (A-Z).

Litery tekstu jawnego są szyfrowane przy pomocy liter klucza, 
które są powtarzane cyklicznie.

Przesunięcie = numer litery klucza (np. A = 0, B = 1, ..., Z = 25)

```
def vigenere_encrypt(plaintext, key):
    encrypted = []
    key = key.upper()
    key_len = len(key)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            key_char = key[i % key_len].upper()
            key_shift = ord(key_char) - ord('A')
            new_char = chr((ord(char) - offset + key_shift) % 26 + offset)
            encrypted.append(new_char)
        else:
            encrypted.append(char)
    return ''.join(encrypted)
```

```
def vigenere_decrypt(ciphertext, key):
    decrypted = []
    key = key.upper()
    key_len = len(key)
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            key_char = key[i % key_len].upper()
            key_shift = ord(key_char) - ord('A')
            new_char = chr((ord(char) - offset - key_shift + 26) % 26 + offset)
            decrypted.append(new_char)
        else:
            decrypted.append(char)
    return ''.join(decrypted)
```
plaintext = "INFORMATYKA"
key = "DOM"

encrypted = vigenere_encrypt(plaintext, key)
print("Zaszyfrowany tekst:", encrypted)

decrypted = vigenere_decrypt(encrypted, key)
print("Odszyfrowany tekst:", decrypted)

Zaszyfrowany tekst: 
Odszyfrowany tekst: INFORMATYKA