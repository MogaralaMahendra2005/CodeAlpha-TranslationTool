function translateText() {

    let text = document.getElementById("text").value;
    let lang = document.getElementById("lang").value;

    fetch("/translate", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({text: text, language: lang})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText = data.translation;
    });
}

/* 🔁 Swap */
function swapLang() {
    let text = document.getElementById("text");
    let result = document.getElementById("result");
    let lang = document.getElementById("lang");

    let temp = text.value;
    text.value = result.innerText;
    result.innerText = temp;
}

/* 📋 Copy */
function copyText() {
    navigator.clipboard.writeText(document.getElementById("result").innerText);
    alert("Copied!");
}

/* 🔊 Speak */
function speakText() {
    let text = document.getElementById("result").innerText;
    let speech = new SpeechSynthesisUtterance(text);
    speechSynthesis.speak(speech);
}

/* 🎤 Voice Input */
function startVoice() {
    let recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = "en-US";

    recognition.onresult = function(event) {
        document.getElementById("text").value = event.results[0][0].transcript;
    };

    recognition.start();
}

/* 🌙 Dark Mode */
function toggleDarkMode() {
    document.body.classList.toggle("dark");
}