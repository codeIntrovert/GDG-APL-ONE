# VOICE AND TEXT-BASED ALEXA CLONES USING GEMINI

This project provides both **voice-based** and **text-based** AI assistants using **Google's Gemini API**. The AI-powered assistants can process user input via text or speech and generate intelligent responses.

## **Skill Tags**

Python, APIs, Google Gemini API, AI, Voice Recognition, Speech-to-Text, Text-to-Speech (TTS), Voice Assistant, Automation, Speech Synthesis

## **Relevant Links**

Visual Studio Code: https://code.visualstudio.com/
Python: https://www.python.org/downloads/

---

## **Getting Started**

Follow these steps to set up and run the project on your local machine.

### **1. Clone the Repository**

First, clone or download the project from the GitHub repository:

```bash
 git clone https://github.com/codeIntrovert/GDG-APL-ONE
 cd GDG-APL-ONE
```

### **2. Get a Free Gemini API Key**

You need an API key from **Google's AI Studio** to use the Gemini AI services.

- Visit [Google AI Studio](https://aistudio.google.com/)
- Sign in with your Google account
- Generate a free API key
- Save the key for later use

### **3. Create a Python Virtual Environment**

Setting up a virtual environment ensures dependencies don’t interfere with system packages.

```bash
py -m venv env  # Create virtual environment
```

Activate the environment:

- **Windows:**
  ```bash
  env\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source env/bin/activate
  ```

### **4. Install Required Dependencies**

Once the virtual environment is activated, install the dependencies:

```bash
pip install -r requirements.txt
```

### **5. Set Up Your API Key**

To securely store your API key, create a `.env` file in the project directory and add:

```plaintext
API_KEY=your_gemini_api_key_here
```

---

## **Usage**

### **Text-Based Chat Assistant**

Run the following command to interact with the text-based AI assistant:

```bash
py text_gemini.py
```

### **Voice-Based AI Assistant**

Run this command to use the voice-enabled assistant:

```bash
py voice_gemini.py
```

---

## **Project Structure**

```
📂 alexa-clone
├── 📂 env/                 # Virtual environment (ignored in .gitignore)
├── 📂 library/             # Helper modules
├── 📜 text_gemini.py       # Text-based AI assistant
├── 📜 voice_gemini.py      # Voice-based AI assistant (final outcome)
├── 📜 requirements.txt     # Required dependencies
├── 📜 .env                 # API key storage (not committed to Git)
└── 📜 README.md            # Documentation
```

---

## **Troubleshooting**

### **Common Issues and Fixes**

#### ❌ `Running Scripts is disabled on this machine`

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### ❌ `ModuleNotFoundError: No module named 'xyz'`

✅ Ensure you've installed all dependencies:

```bash
pip install -r requirements.txt
```

#### ❌ `ImportError: attempted relative import with no known parent package`

✅ Try running the script as a module:

```bash
py -m text_gemini
```

#### ❌ API not responding

✅ Verify your `.env` file contains the correct API key.  
✅ Ensure your internet connection is working.

---

## **Features**

✅ Text-based AI chat assistant  
✅ Voice-based AI assistant  
✅ Uses Google's **Gemini API** for responses  
✅ Lightweight and easy to set up  
✅ Python-based with minimal dependencies

---

## **Acknowledgments**

🔹 Powered by **Google Gemini AI**  
🔹 Inspired by **Alexa Voice Assistant**
🔹 Project by **Google Developer Groups On Campus SSTC**

---

Happy Coding! 🚀
