import string

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def frequency_analysis(text):
    # Simplified frequency analysis: returns the most common letter
    text = "".join(filter(str.isalpha, text)).upper()
    if not text: return None
    freq = {letter: text.count(letter) for letter in string.ascii_uppercase}
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)