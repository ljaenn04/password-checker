# 🔐 Password Checker

A web tool that checks if your password has been leaked in real data breaches, using the HaveIBeenPwned API.

## Features
- Checks if password appears in known data breaches
- Shows how many times it was leaked
- Analyzes password strength
- Suggests improvements
- Your password never leaves your device (k-anonymity method)

## Tech Stack
- Python 3
- Flask
- HaveIBeenPwned API
- HTML/CSS

## How to run

git clone https://github.com/ljaenn04/password-checker.git
cd password-checker
pip install flask requests
python app.py

Then open http://127.0.0.1:5000 in your browser.

## Disclaimer
This tool is for educational purposes only.
