#!/usr/bin/env python3

def decrypt_vingenere_cipher(text, keyword):
    result = ""
    keyword_length = len(keyword)
    keyword = keyword.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            keyword_shifted = ord(keyword[key_index % keyword_length]) - ord('A')
            alphabet = ord(char) - ascii_offset
            alphabet_shift_reversed = (alphabet - keyword_shifted) % 26
            char = chr(alphabet_shift_reversed + ascii_offset)
            key_index += 1
        result += char

    return result

print("Enter the encryption text.")
encrypted_text = input("> ")

print("Enter the keyword.")
keyword = input("> ")

plain_text = decrypt_vingenere_cipher(encrypted_text, keyword)
print(f"Result: {plain_text}")
