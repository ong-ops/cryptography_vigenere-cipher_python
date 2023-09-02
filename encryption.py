#!/usr/bin/env python3


def encrypt_vigenere_cipher(text, keyword):
    result = ""
    keyword_length = len(keyword)
    keyword = keyword.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            keyword_shifted = ord(keyword[key_index % keyword_length]) - ord('A')
            alphabet = ord(char) - ascii_offset
            alphabet_shifted = (alphabet + keyword_shifted) % 26
            char = chr(alphabet_shifted + ascii_offset)
            key_index += 1
        result += char

    return result

print("Enter the message.")
plain_text = input("> ")

print("Enter the keyword.")
keyword = input('> ')

encrypted = encrypt_vigenere_cipher(plain_text, keyword)
print(f"Result: {encrypted}")
