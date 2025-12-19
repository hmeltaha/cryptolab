import matplotlib.pyplot as plt
import os
import string

# --- Caesar Cipher ---
def caesar_cipher(text, shift, mode='encrypt'):
    s = shift if mode == 'encrypt' else -shift
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + s) % 26 + start)
        else: result += char
    return result

# --- Vigenère Cipher ---
def vigenere_cipher(text, key, mode='encrypt'):
    result = ""
    key = key.upper()
    key_idx = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_idx % len(key)]) - ord('A')
            if mode == 'decrypt': shift = -shift
            
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
            key_idx += 1
        else: result += char
    return result

# --- Frequency Analysis & Visualization ---
def generate_freq_chart(text, filename="chart.png"):
    text = text.upper()
    letters = string.ascii_uppercase
    counts = [text.count(l) for l in letters]
    
    plt.figure(figsize=(8, 4), facecolor='#1a1a1a')
    ax = plt.axes()
    ax.set_facecolor("#1a1a1a")
    plt.bar(letters, counts, color='#00ff41')
    plt.title("Letter Frequency Analysis", color="white")
    plt.xticks(color="white"); plt.yticks(color="white")
    plt.tight_layout()
    # Save to static folder
    path = os.path.join('static', 'images', filename)
    plt.savefig(path)
    plt.close()
    return filename