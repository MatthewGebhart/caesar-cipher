from caesar_cipher.is_english_word import count_words
def encrypt(plaintext, shift):
    # """
    # Takes in a plaintext phrase and a numeric shift and returns the phrase shifted by that much, mod 10 ("number wrap")
    #
    # :param plaintext: plaintext phrase
    # :param shift: integer
    # :return: encrypted string
    # """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                shift_char = chr((ord(char) + shift - 65) % 26 + 65)
            else:
                shift_char = chr((ord(char) + shift - 97) % 26 + 97)
            ciphertext += shift_char
        else:
            ciphertext += char
    return ciphertext


def decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                shift_char = chr((ord(char) - shift - 65) % 26 + 65)
            else:
                shift_char = chr((ord(char) - shift - 97) % 26 + 97)
            plaintext += shift_char
        else:
            plaintext += char
    return plaintext


def crack(ciphertext):
    for shift in range(26):
        plaintext = decrypt(ciphertext, shift)
        real_word_accuracy = count_words(plaintext) / len(plaintext.split())
        if real_word_accuracy == 1:
            print(plaintext)
            return plaintext
    return ''



if __name__ == "__main__":
    code = encrypt("Matt is the greatest in the world", 6)
    print(code)
    print(decrypt(code, 6))
    crack(code)
