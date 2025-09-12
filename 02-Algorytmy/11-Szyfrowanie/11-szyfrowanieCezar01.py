plain_text = input("Podaj tekst do szyfrowania: ")
shift = int(input("Podaj ilość znaków do przesunięcia: "))

def szyfrCezara(text, shift):
    encrypted_text = ''
    for letter in text:
        if ord(letter) + shift > ord('Z'):
            encrypted_text += chr(ord(letter) + shift - 26)
        else:
            encrypted_text += chr(ord(letter) + shift)
    return encrypted_text


print(szyfrCezara(plain_text, shift))