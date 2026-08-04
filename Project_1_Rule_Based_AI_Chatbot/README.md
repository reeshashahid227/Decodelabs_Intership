# 🤖 Nova — Rule-Based AI Chatbot

A Python-based **Rule-Based AI Chatbot** developed as **Project 1 of the DecodeLabs Artificial Intelligence Internship**.

The chatbot uses predefined rules and `if-elif-else` decision-making to simulate a simple conversational AI. It runs continuously in a loop and responds to different types of user input without using Machine Learning, Large Language Models, or external AI APIs.

---

## 📌 Project Overview

This project focuses on the fundamentals of Artificial Intelligence through **rule-based decision making and control flow**.

Instead of learning from data, the chatbot follows explicitly programmed rules to determine an appropriate response to the user's input.

The chatbot can remember the user's name during the current session, answer basic questions, perform simple calculations, provide date and time information, respond to moods and compliments, and display a help menu.

---

## 🎯 Objectives

* Understand rule-based Artificial Intelligence
* Practice `if-elif-else` decision-making
* Implement a continuous conversation loop
* Handle predefined user inputs
* Store temporary session information
* Practice Python functions and data structures
* Build a simple interactive command-line application

These objectives align with the DecodeLabs Project 1 requirements for a rule-based chatbot using greetings, exit commands, predefined responses, and continuous interaction.

---

## ✨ Features

### 👋 Greetings

The chatbot recognizes common greetings such as:

```text
hi
hello
hey
salam
assalamualaikum
```

---

### 👤 User Name Memory

The chatbot can remember the user's name during the current session.

Example:

```text
You: My name is Reesha

ChatBot: Nice to meet you, Reesha! I'll remember your name.

You: What is my name?

ChatBot: Your name is Reesha.
```

---

### 😊 Mood Detection

The chatbot can respond to basic positive and negative moods.

Examples:

```text
You: I am happy
ChatBot: That's wonderful to hear!

You: I am sad
ChatBot: I'm sorry you're feeling that way.
```

---

### 🤖 Bot Identity

The chatbot can explain who it is and what it can do.

Example:

```text
You: Who are you?

ChatBot: I'm Nova, a rule-based AI chatbot created using Python.
```

---

### 🧮 Basic Calculator

The chatbot can perform simple arithmetic operations.

Supported operations:

* Addition
* Subtraction
* Multiplication
* Division

Examples:

```text
You: 10 + 5
ChatBot: The result is 15.

You: 20 * 4
ChatBot: The result is 80.

You: 50 / 2
ChatBot: The result is 25.
```

The chatbot also handles division by zero.

---

### 🕒 Date and Time

The chatbot can provide the current date and time.

Example:

```text
You: What time is it?

ChatBot: The current time is 02:30:15 PM.
```

---

### 😂 Jokes

The chatbot contains a collection of predefined programming-related jokes.

Example:

```text
You: Tell me a joke

ChatBot: Why do programmers prefer dark mode?
        Because light attracts bugs!
```

---

### ❤️ Compliment Handling

The chatbot responds to positive feedback.

Example:

```text
You: You are awesome!

ChatBot: Aww, thanks! I appreciate that.
```

---

### ❓ Help Menu

Users can type:

```text
help
```

to see the chatbot's available commands and capabilities.

---

### 🔄 Continuous Conversation

The chatbot runs inside a `while` loop, allowing multiple interactions until the user enters an exit command.

Supported exit commands include:

```text
bye
exit
quit
goodbye
see you
```

---

### 📊 Session Summary

When the conversation ends, the chatbot displays a small session summary containing:

* User name, if provided
* Number of messages exchanged

Example:

```text
==================================================
SESSION SUMMARY
==================================================
User name: Reesha
Messages exchanged: 8
==================================================
```

---

## 🧠 How It Works

The chatbot follows a simple rule-based pipeline:

```text
User Input
    ↓
Input Cleaning
    ↓
Rule Checking
    ↓
if / elif / else Decisions
    ↓
Generate Response
    ↓
Display Response
    ↓
Continue Conversation
```

For example:

```python
if text in GREETING_COMMANDS:
    return random.choice(GREETINGS)

elif "how are you" in text:
    return random.choice(HOW_ARE_YOU)

elif "joke" in text:
    return random.choice(JOKES)

else:
    return random.choice(FALLBACKS)
```

The chatbot does **not learn from the conversation**. Its behavior is determined by the rules programmed in Python.

---

## 🗂️ Project Structure

```text
Project-1-Rule-Based-AI-Chatbot/
│
├── chatbot.py
└── README.md
```

---

## 🛠️ Technologies Used

* **Python**
* `if-elif-else`
* `while` loop
* Functions
* Dictionaries
* Lists
* Sets
* Regular Expressions
* `datetime`
* `random`

---

## 📦 Python Modules

The project uses only Python's standard library:

```python
import datetime
import random
import re
```

No external packages are required.

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project folder

```bash
cd Project-1-Rule-Based-AI-Chatbot
```

### 3. Run the chatbot

```bash
python chatbot.py
```

---

## 💬 Example Conversation

```text
============================================================
🤖 NOVA - RULE-BASED AI CHATBOT
============================================================
ChatBot: Hello! I'm Nova.
ChatBot: Type 'help' to see my features or 'bye' to end the conversation.

You: hello

ChatBot: Hello! How can I help you?

You: my name is Reesha

ChatBot: Nice to meet you, Reesha! I'll remember your name.

You: what is my name

ChatBot: Your name is Reesha.

You: 15 * 4

ChatBot: The result is 60.

You: tell me a joke

ChatBot: Why was the computer tired? It had too many tabs open!

You: bye

ChatBot: Thanks for chatting with me!
ChatBot: Goodbye, Reesha! 👋

==================================================
SESSION SUMMARY
==================================================
User name: Reesha
Messages exchanged: 6
==================================================
```

---

## 🎓 Internship Context

**Program:** DecodeLabs Artificial Intelligence Internship
**Project:** Project 1 — Rule-Based AI Chatbot
**Focus:** Control Flow, Decision Making, and Basic AI Concepts

The project is designed as a foundation in AI programming before moving toward more advanced AI concepts.

---

## 🔮 Possible Future Improvements

The chatbot can be extended in future versions with:

* More conversational rules
* More user intents
* Expanded vocabulary
* More advanced nested conditions
* Additional utilities
* A graphical user interface
* Persistent user profiles
* Natural Language Processing

These would be future enhancements; the current project intentionally remains a **pure rule-based chatbot**.

---


```
```
