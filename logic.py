import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import string
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import string
import uuid

def caesar_cipher(text, shift, mode='encrypt'):
    s = shift if mode == 'encrypt' else -shift
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + s) % 26 + start)
        else:
            result += char
    return result

def vigenere_cipher(text, key, mode='encrypt'):
    mode = (mode or 'encrypt').lower()
    if mode not in ('encrypt', 'decrypt'):
        raise ValueError("Action must be 'encrypt' or 'decrypt'.")

    cleaned_key = ''.join(c for c in (key or '').upper() if c.isalpha())
    if not cleaned_key:
        raise ValueError("Key must contain at least one letter.")

    result = ""
    key_idx = 0
    for char in text:
        if char.isalpha():
            shift = ord(cleaned_key[key_idx % len(cleaned_key)]) - ord('A')
            if mode == 'decrypt':
                shift = -shift

            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
            key_idx += 1
        else:
            result += char
    return result

def frequency_analysis(text):
    filtered = [c for c in text.upper() if c.isalpha()]
    total = len(filtered)
    if total == 0:
        return []

    counts = {letter: 0 for letter in string.ascii_uppercase}
    for char in filtered:
        counts[char] += 1

    return [
        {
            "letter": letter,
            "count": counts[letter],
            "percent": round((counts[letter] / total) * 100, 2),
        }
        for letter in string.ascii_uppercase
        if counts[letter] > 0
    ]

def generate_freq_chart(text, filename=None):
    letters_only = ''.join(c for c in text.upper() if c.isalpha())
    if not letters_only:
        return ""

    filename = filename or f"chart_{uuid.uuid4().hex}.png"
    letters = string.ascii_uppercase
    counts = [letters_only.count(l) for l in letters]

    plt.figure(figsize=(8, 4), facecolor='#1a1a1a')
    ax = plt.axes()
    ax.set_facecolor("#1a1a1a")
    plt.bar(letters, counts, color='#00ff41')
    plt.title("Letter Frequency Analysis", color="white")
    plt.xticks(color="white")
    plt.yticks(color="white")
    plt.tight_layout()

    path = os.path.join('static', 'images', filename)
    plt.savefig(path)
    plt.close()
    return filename