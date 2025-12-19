from flask import Flask, render_template, request
import logic  # Ensure you renamed your cipher logic file to logic.py

app = Flask(__name__)

@app.route('/')
def index():
    # Pass project metadata to the template
    project_info = {
        "students": "Hala Meltaha, Sara Samir, Ehdaa Alajarma",
        "instructor": "Dr. Muhannad Tahboush",
        "title": "Classical Cipher Learning Website"
    }
    return render_template('index.html', info=project_info)

@app.route('/caesar', methods=['GET', 'POST'])
def caesar():
    result = ""
    attempts = [] # For the "Hacking" demo
    if request.method == 'POST':
        text = request.form.get('text')
        
        # Check if user is trying to Encrypt/Decrypt or Brute Force
        if 'shift' in request.form and request.form.get('shift'):
            shift = int(request.form.get('shift'))
            action = request.form.get('action')
            result = logic.caesar_cipher(text, shift, mode=action)
        else:
            # Brute Force Attack: Try all 26 shifts
            for i in range(26):
                attempts.append({
                    "shift": i, 
                    "text": logic.caesar_cipher(text, i, mode='decrypt')
                })
                
    return render_template('caesar.html', result=result, attempts=attempts)

@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere():
    result = ""
    chart_url = ""
    if request.method == 'POST':
        # These MUST match the 'name' attributes in your HTML
        text = request.form.get('text')
        key = request.form.get('key')
        action = request.form.get('action')
        
        if text and key:
            import logic # Ensure logic is imported
            result = logic.vigenere_cipher(text, key, mode=action)
            chart_url = logic.generate_freq_chart(result)
            
    return render_template('vigenere.html', result=result, chart=chart_url)
if __name__ == '__main__':
    app.run(debug=True)