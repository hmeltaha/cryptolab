# Classical Cipher Learning Website

A Flask based web application for learning and demonstrating classical ciphers (Caesar and Vigenere).

**Student:** Hala Meltaha
**Instructor:** Dr. Muhannad Tahboush

---

## How to Run the Program

### Prerequisites
- Python 3.7 or higher installed on your system
- pip (Python package manager)

---

## Windows

### Step 1: Create Virtual Environment
```bash
python -m venv venv
```

### Step 2: Activate Virtual Environment
```bash
venv\Scripts\activate
```

### Step 3: Install Flask
```bash
pip install flask
```

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Access the Application
Open your browser and go to: `http://localhost:5000`

---

## macOS / Linux

### Step 1: Create Virtual Environment
```bash
python3 -m venv venv
```

### Step 2: Activate Virtual Environment

**On Linux/macOS (bash/zsh):**
```bash
source venv/bin/activate
```

**On Linux (fish shell):**
```bash
source venv/bin/activate.fish
```

### Step 3: Install Flask
```bash
pip install flask
```

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Access the Application
Open your browser and go to: `http://localhost:5000`

---

## Subsequent Sessions

Once you've completed the setup above, for future sessions you only need to:

### Windows
```bash
venv\Scripts\activate
python app.py
```

### macOS / Linux
```bash
source venv/bin/activate
python app.py
```

Or on fish shell:
```bash
source venv/bin/activate.fish
python app.py
```

---

## Stopping the Application

Press `Ctrl + C` in your terminal to stop the Flask server.

---

## Features

- **Caesar Cipher:** Encrypt/decrypt with a shift value and brute force attack demo
- **Vigenere Cipher:** Encrypt/decrypt with a keyword
- **Interactive Interface:** User-friendly web interface
- **Educational Focus:** Designed for learning cryptography concepts
