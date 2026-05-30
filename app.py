import hashlib
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

def check_password(password):
    # Convertir contraseña a SHA1
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]

    # Enviar solo los primeros 5 caracteres del hash (nunca la contraseña)
    r = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
    hashes = r.text.splitlines()

    # Buscar si nuestro hash está en la respuesta
    for line in hashes:
        h, count = line.split(":")
        if h == suffix:
            return int(count)
    return 0

def analyze_strength(password):
    score = 0
    tips = []

    if len(password) >= 8:
        score += 1
    else:
        tips.append("Usa al menos 8 caracteres")

    if any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("Añade letras mayúsculas")

    if any(c.islower() for c in password):
        score += 1
    else:
        tips.append("Añade letras minúsculas")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("Añade números")

    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        score += 1
    else:
        tips.append("Añade caracteres especiales (!@#$...)")

    if score <= 2:
        strength = "Débil"
    elif score <= 3:
        strength = "Media"
    elif score == 4:
        strength = "Fuerte"
    else:
        strength = "Muy fuerte"

    return strength, tips

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        password = request.form.get("password")
        times_leaked = check_password(password)
        strength, tips = analyze_strength(password)
        result = {
            "leaked": times_leaked > 0,
            "times": times_leaked,
            "strength": strength,
            "tips": tips
        }
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)