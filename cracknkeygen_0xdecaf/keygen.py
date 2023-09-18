#!/usr/bin/env python3
import random
import shlex

def create_key() -> int:
    secret_string = "secret"
    key = 0
    for index, char in enumerate(secret_string):
        key += ord(char) ^ index

    return key

def generate_random_char() -> chr:
    return chr(random.randint(ord('!'), ord('~')))

def is_printable(character : chr) -> bool:
    return ord(character) in range(ord('!'), ord('~'))

def generate_key(target_value : int) -> str:
    while True:
        out = ""
        index = 0
        count = 0

        while count < (target_value - (ord('~') ^ index)):
            char = generate_random_char()
            xored_char = ord(char) ^ index
            count += xored_char
            index = index + 1
            out += char

        char = chr((target_value - count) ^ index)
        if not is_printable(char):
            continue

        out += char
        return out

def main():
    source_key = create_key()
    generated_key = generate_key(source_key)

    print(f"Your key is: {shlex.quote(generated_key)}")

if __name__ == "__main__":
    main()
