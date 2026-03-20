# 🤖 Multi-Mode AI Chatbot (Funny | Serious | Sad)

A simple command-line AI chatbot built using **LangChain** and **Mistral AI**, where users can interact with different personalities of the bot.

## 🚀 Features

* 🎭 Multiple AI modes:

  * Funny AI Agent 😂
  * Serious AI Agent 🧑‍💼
  * Sad AI Agent 😔
* 💬 Interactive CLI-based chat
* 🧠 Powered by Mistral LLM via LangChain
* 🔄 Maintains conversation history

---

## 🛠️ Tech Stack

* Python
* LangChain
* Mistral AI API
* dotenv (for environment variables)

---

## 📂 Project Structure

```
├── chatbot.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/your-username/multi-mode-chatbot.git
cd multi-mode-chatbot
```

### 2. Create virtual environment (recommended)

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Add API Key

Create a `.env` file and add:

```
MISTRAL_API_KEY=your_api_key_here
```

---

## ▶️ Run the Chatbot

```
python chatbot.py
```

---

## 🎮 Usage

* Choose the AI mode:

  * `1` → Funny
  * `2` → Serious
  * `3` → Sad
* Start chatting
* Type `0` to exit

---

## 📸 Example

```
Choose your AI Mode
1. Funny AI Agent
2. Serious AI Agent
3. Sad AI Agent

Enter your choice: 1
You: Hello
Bot: Why did the AI cross the road? To optimize the chicken! 🤖😂
```

## 🤝 Contributing

Feel free to fork this repo and improve it!

---

## 📜 License

This project is open-source and free to use.
