encrypted_text = input("Podaj tekst zaszyfrowany: ")
shift = int(input("Podaj ilość znaków do przesunięcia: "))
# CHEUD - ZEBRA
def szyfrCezara(encrypted_text, shift):
    plain_text = ''
    for letter in encrypted_text:
        if ord(letter) - shift < ord('A'):
            plain_text += chr(ord(letter) - shift + 26)
        else:
            plain_text += chr(ord(letter) - shift)
    return plain_text


print(szyfrCezara(encrypted_text, shift))



print(ord('A') + ord('B') + 9 - ord('Z'))