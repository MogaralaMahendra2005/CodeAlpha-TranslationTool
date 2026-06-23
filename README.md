# 🌍 AI-Based Translator Tool using Flask

## 📌 About the Project
This is a web-based translator application built using Flask. It allows users to translate text into multiple languages instantly with a simple and clean UI.

---

## 🚀 Features
- 🌍 Multi-language support (20+ languages)
- ⚡ Real-time translation
- 🎤 Voice input support
- 🔊 Text-to-speech output
- 📋 Copy translated text
- 🌙 Dark mode UI
- 🔁 Swap languages feature

---

## 🛠️ Tech Stack
- Frontend: HTML, CSS, JavaScript  
- Backend: Python (Flask)  
- Library: deep-translator (GoogleTranslator)

---

## ⚙️ How It Works
1. User enters text in input box  
2. Selects target language  
3. Frontend sends request to Flask backend  
4. Backend processes translation using API  
5. Translated text is returned and displayed on screen  

---

## 📂 Project Structure
Translation-Tool/
│
├── app.py
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js

---

## 📂 Setup Instructions
```bash
pip install flask
pip install deep-translator
python app.py
