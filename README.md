# 🤖 AI Chatbot

An AI-powered chatbot application built with **Python, FastAPI, Streamlit, and Google Gemini**. The project separates the backend API from the frontend interface, making it easier to develop, test, and deploy.
--
#### link - https://ai-chatbot-frontend-v7x0.onrender.com/
## ✨ Features

* 💬 AI-powered conversational chatbot
* 🧠 Google Gemini integration
* ⚡ FastAPI backend
* 🎨 Streamlit frontend
* 🔐 Environment variables for API key management
* 📁 Separate frontend and backend architecture
* 🚀 Ready for deployment

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* Google Gemini API
* Uvicorn

### Frontend

* Python
* Streamlit
* Requests

### Deployment

* GitHub
* Render
* GitHub Actions (CI/CD)

## 📂 Project Structure

```text
AI chatbot/
│
├── backend/
│   ├── app.py
│   ├── chatbot.py
│   └── requirements.txt
│
├── frontend/
│   └── app.py
│
├── .gitignore
└── README.md
```

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd AI-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r backend/requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_api_key_here
```

**Never commit your `.env` file or API key to GitHub.**

## ▶️ Run the Backend

From the project root:

```bash
uvicorn backend.app:app --reload
```

The backend will run locally on:

```text
http://127.0.0.1:8000
```

## ▶️ Run the Frontend

Open another terminal:

```bash
streamlit run frontend/app.py
```

The Streamlit application will open in your browser.

## 🔄 Architecture

```text
User
  │
  ▼
Streamlit Frontend
  │
  │ HTTP Request
  ▼
FastAPI Backend
  │
  ▼
Chatbot Logic
  │
  ▼
Google Gemini API
  │
  ▼
AI Response
  │
  ▼
Streamlit Frontend
```

## 🚀 Deployment

The project is designed to be deployed with:

* **GitHub** for source control
* **GitHub Actions** for CI/CD
* **Render** for hosting

Every update pushed to the repository can be tested through GitHub Actions and deployed automatically.

## 🔒 Environment Variables

The application requires the following environment variable:

```text
GOOGLE_API_KEY
```

Add the value through your deployment platform's environment-variable settings rather than committing it to the repository.

## 👩‍💻 Author

**Vaishnavi Agrawal**

B.Tech in Artificial Intelligence

---

⭐ If you find this project useful, consider giving it a star!
