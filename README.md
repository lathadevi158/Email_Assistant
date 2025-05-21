# 📧 Gmail Assistant using Streamlit, LangChain, Azure OpenAI 

This project is an intelligent Gmail assistant built with **Streamlit**, powered by **Azure OpenAI**, **Google Generative AI**, and **LangChain**. It allows you to search emails, create drafts, send messages, and interact with Gmail threads — all through a natural language interface.

---

## 🚀 Features

- 🔍 Search Gmail emails with natural queries
- ✏️ Compose and save email drafts
- 📤 Send emails from the drafts folder
- 🧵 View entire conversation threads
- ⚡ Interact using conversational AI powered by Azure OpenAI

---

## 🛠 Tech Stack

- [Streamlit](https://streamlit.io/) – UI
- [LangChain](https://www.langchain.com/) – Agent and tool framework
- [Azure OpenAI](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/) – LLM backend
- [Gmail API](https://developers.google.com/gmail/api) – Email operations
- [Python](https://www.python.org/downloads/release/python-3119/) – 3.11.*

---

## 📁 Project Structure

.
├── app.py # Main application code
├── .env # Environment variables 
├── token.json # Gmail OAuth token (auto-generated after first auth)
├── credentials.json # Gmail OAuth 2.0 credentials
├── requirements.txt # Project dependencies
└── README.md # Project documentation




--------🔑 Gmail API Setup--------

Step-by-step: Get credentials.json and token.json
✅ 1. Enable Gmail API
Go to Google Cloud Console

Create or select a project

Enable Gmail API for the project

✅ 2. Set Up OAuth Consent Screen
Go to "OAuth Consent Screen"

Select External, click Create

Fill out required fields

Add https://mail.google.com/ as a scope

✅ 3. Create OAuth 2.0 Credentials
Go to Credentials → Create Credentials → OAuth Client ID

Choose Desktop App as the application type

Download the credentials.json file and place it in your project directory

✅ 4. Generate token.json
On first run, the app will open a browser asking for Gmail access. After logging in and granting permissions, a token.json will be automatically created.

---------▶️ Run the App-----------

streamlit run app.py
Then, open your browser at http://localhost:8501 (or Streamlit will auto-launch it).

--------📝 Example Commands You Can Try---------
"Search for emails from Google"

"Create a draft email to Alice about the meeting tomorrow"

"Send the draft email I just created"

"Show the latest email thread with Bob"


-----📄 License---------
This project is licensed under the MIT License.

---------🙋‍♀️ Author---------
Marpally Latha Devi,
Prompt Engineer | Generative AI Developer
GitHub: yourusername








