# 🛡️ LLM Security Helper

An AI-powered security assistant built with **Streamlit** and **Groq (Llama 3)**. This tool helps developers identify vulnerabilities in code and creates threat models for GenAI applications.

## 🚀 Features

- **Part 1: Code Vulnerability Scanner**
  - Takes raw code snippets as input.
  - Identifies security flaws (e.g., SQL Injection).
  - Provides secure, fixed code with explanations.
- **Part 2: GenAI Threat Modeler**
  - Analyzes specifications for LLM Agents/Apps.
  - Maps risks to the **OWASP Top 10 for LLMs**.
  - Identifies relevant **MITRE ATLAS** attack tactics.

## 🛠️ Prerequisites

- **Python 3.8+** installed on your system.
- A **Groq API Key** (Free). You can get one here: [console.groq.com/keys](https://console.groq.com/keys)

## 📦 Installation & Setup

Follow these steps to set up the project locally using a virtual environment.

### 1. Clone or Download the Project

Navigate to the project folder in your terminal:

```bash
cd path/to/your/project
```

### 2. Create a Virtual Environment (Recommended)

This keeps your project dependencies isolated.

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Mac / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

(You will know it worked if you see (venv) appear at the start of your terminal line)

### 3. Install Dependencies

Install the required libraries from requirements.txt:

```bash
pip install -r requirements.txt
```

🏃‍♂️ How to Run

Ensure your virtual environment is active.

Run the Streamlit app:

```bash
streamlit run app.py
```

The app will open automatically in your browser (usually at http://localhost:8501).

Enter your Groq API Key in the sidebar to start scanning.

📂 Project Structure

```plaintext
.
├── app.py              # Main application code
├── requirements.txt    # List of python dependencies
└── README.md           # Project documentation
```
# 🛡️ LLM Security Helper

An AI-powered security assistant built with **Streamlit** and **Groq (Llama 3)**. This tool helps developers identify vulnerabilities in code and creates threat models for GenAI applications.

## 🚀 Features

* **Part 1: Code Vulnerability Scanner**
    * Takes raw code snippets as input.
    * Identifies security flaws (e.g., SQL Injection).
    * Provides secure, fixed code with explanations.
* **Part 2: GenAI Threat Modeler**
    * Analyzes specifications for LLM Agents/Apps.
    * Maps risks to the **OWASP Top 10 for LLMs**.
    * Identifies relevant **MITRE ATLAS** attack tactics.

## 🛠️ Prerequisites

* **Python 3.8+** installed on your system.
* A **Groq API Key** (Free). You can get one here: [console.groq.com/keys](https://console.groq.com/keys)

## 📦 Installation & Setup

Follow these steps to set up the project locally using a virtual environment.

### 1. Clone or Download the Project
Navigate to the project folder in your terminal:
```bash
cd path/to/your/project
2. Create a Virtual Environment (Recommended)
This keeps your project dependencies isolated.

Windows:

Bash
python -m venv venv
venv\Scripts\activate
Mac / Linux:

Bash
python3 -m venv venv
source venv/bin/activate
(You will know it worked if you see (venv) appear at the start of your terminal line)

3. Install Dependencies
Install the required libraries from requirements.txt:

Bash
pip install -r requirements.txt
🏃‍♂️ How to Run
Ensure your virtual environment is active.

Run the Streamlit app:

Bash
streamlit run app.py
The app will open automatically in your browser (usually at http://localhost:8501).

Enter your Groq API Key in the sidebar to start scanning.

📂 Project Structure
Plaintext
.
├── app.py              # Main application code
├── requirements.txt    # List of python dependencies
└── README.md           # Project documentation