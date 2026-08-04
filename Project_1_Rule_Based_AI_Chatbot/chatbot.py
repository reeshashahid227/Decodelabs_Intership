
"""
DecodeLabs Internship - Artificial Intelligence
Project 1: Advanced Rule-Based AI Chatbot

This project demonstrates:
- Rule-based decision making using if/elif/else
- Continuous conversation loop
- User name memory
- Multiple response options
- Basic calculator
- Date and time
- Mood detection
- Jokes and compliments
- Help and information commands
- Conversation history and session summary

"""

import datetime
import random
import re


# ============================================================
# BOT CONFIGURATION
# ============================================================

BOT_NAME = "Nova"

EXIT_COMMANDS = {
    "bye",
    "exit",
    "quit",
    "goodbye",
    "see you"
}

GREETING_COMMANDS = {
    "hi",
    "hello",
    "hey",
    "salam",
    "assalamualaikum"
}


# ============================================================
# RESPONSE COLLECTIONS
# ============================================================

GREETINGS = [
    "Hello! How can I help you?",
    "Hi! Nice to see you.",
    "Hey there! What would you like to talk about?",
    "Hello! I'm ready to chat."
]

HOW_ARE_YOU = [
    "I'm doing well! Thanks for asking.",
    "All systems are running smoothly!",
    "I'm great and ready to help!"
]

POSITIVE_MOOD = [
    "That's wonderful to hear!",
    "Great! Keep that positive energy going.",
    "I'm glad you're feeling good!"
]

NEGATIVE_MOOD = [
    "I'm sorry you're feeling that way.",
    "I hope things become better for you soon.",
    "That sounds difficult. Take care of yourself!"
]

JOKES = [
    "Why did the programmer quit his job? Because he didn't get arrays!",
    "Why was the computer tired? It had too many tabs open!",
    "Why do programmers prefer dark mode? Because light attracts bugs!"
]

COMPLIMENTS = [
    "Thank you! That's really kind of you.",
    "Aww, thanks! I appreciate that.",
    "You're making my circuits happy!"
]

FALLBACKS = [
    "I'm not sure how to answer that yet. Try typing 'help'.",
    "I don't have a rule for that question yet.",
    "I didn't understand that. Type 'help' to see my available features."
]


# ============================================================
# CALCULATOR
# ============================================================

def calculate_expression(text):
    """
    Detects simple arithmetic expressions.

    Examples:
        10 + 5
        20 - 8
        6 * 7
        50 / 5
    """

    pattern = r"(-?\d+(?:\.\d+)?)\s*([+\-*/])\s*(-?\d+(?:\.\d+)?)"

    match = re.search(pattern, text)

    if not match:
        return None

    first_number = float(match.group(1))
    operator = match.group(2)
    second_number = float(match.group(3))

    if operator == "+":
        answer = first_number + second_number

    elif operator == "-":
        answer = first_number - second_number

    elif operator == "*":
        answer = first_number * second_number

    elif operator == "/":

        if second_number == 0:
            return "Division by zero is not allowed."

        answer = first_number / second_number

    else:
        return None

    if answer.is_integer():
        answer = int(answer)

    return f"The result is {answer}."


# ============================================================
# NAME EXTRACTION
# ============================================================

def save_user_name(text, memory):
    """
    Detects different ways of introducing a name.
    """

    patterns = [
        "my name is ",
        "i am ",
        "i'm ",
        "call me "
    ]

    for pattern in patterns:

        if text.startswith(pattern):

            name = text[len(pattern):].strip()

            if name:

                name = name.title()
                memory["name"] = name

                return f"Nice to meet you, {name}! I'll remember your name."

    return None


# ============================================================
# HELP MENU
# ============================================================

def help_message():

    return """
Here are some things you can ask me:

  👋 Greetings
     hi, hello, hey

  👤 Personal memory
     my name is Reesha
     what is my name?

  🤖 About me
     who are you?
     who created you?
     what can you do?

  😊 Mood
     how are you?
     I am happy
     I am sad

  🕒 Utilities
     what time is it?
     what is today's date?

  🧮 Calculator
     10 + 5
     20 * 4
     50 / 2

  😂 Entertainment
     tell me a joke

  ❤️ Interaction
     thank you
     you are awesome

  🚪 Exit
     bye
     exit
     quit
"""


# ============================================================
# MAIN RESPONSE ENGINE
# ============================================================

def generate_response(user_input, memory):

    text = user_input.lower().strip()
    text = text.strip("!?., ")

    # --------------------------------------------------------
    # EXIT
    # --------------------------------------------------------

    if text in EXIT_COMMANDS:
        return "EXIT"


    # --------------------------------------------------------
    # EMPTY INPUT
    # --------------------------------------------------------

    if not text:
        return "Please type something so I can respond."


    # --------------------------------------------------------
    # NAME MEMORY
    # --------------------------------------------------------

    name_response = save_user_name(text, memory)

    if name_response:
        return name_response


    # --------------------------------------------------------
    # ASK USER NAME
    # --------------------------------------------------------

    elif (
        "what is my name" in text
        or "what's my name" in text
        or "do you know my name" in text
    ):

        if memory.get("name"):
            return f"Your name is {memory['name']}."

        return "I don't know your name yet. Tell me by saying 'My name is ...'."


    # --------------------------------------------------------
    # GREETINGS
    # --------------------------------------------------------

    elif text in GREETING_COMMANDS:

        response = random.choice(GREETINGS)

        if memory.get("name"):
            response += f" It's nice to chat with you, {memory['name']}!"

        return response


    # --------------------------------------------------------
    # BOT IDENTITY
    # --------------------------------------------------------

    elif (
        "who are you" in text
        or "your name" in text
        or "what are you" in text
    ):

        return (
            f"I'm {BOT_NAME}, a rule-based AI chatbot "
            "created using Python."
        )


    # --------------------------------------------------------
    # BOT PURPOSE
    # --------------------------------------------------------

    elif (
        "what can you do" in text
        or "your purpose" in text
        or "what is your purpose" in text
    ):

        return (
            "I can chat using predefined rules, remember your name "
            "during this session, perform simple calculations, "
            "tell jokes, and provide date and time information."
        )


    # --------------------------------------------------------
    # CREATOR / PROJECT
    # --------------------------------------------------------

    elif (
        "who created you" in text
        or "who made you" in text
        or "who built you" in text
    ):

        return (
            "I was developed as Project 1 of the DecodeLabs "
            "Artificial Intelligence internship."
        )


    # --------------------------------------------------------
    # HOW ARE YOU
    # --------------------------------------------------------

    elif "how are you" in text:

        return random.choice(HOW_ARE_YOU)


    # --------------------------------------------------------
    # POSITIVE MOOD
    # --------------------------------------------------------

    elif any(phrase in text for phrase in [
        "i am happy",
        "i'm happy",
        "i am good",
        "i'm good",
        "i am fine",
        "i'm fine",
        "i feel great",
        "i am great",
        "i'm great"
    ]):

        return random.choice(POSITIVE_MOOD)


    # --------------------------------------------------------
    # NEGATIVE MOOD
    # --------------------------------------------------------

    elif any(phrase in text for phrase in [
        "i am sad",
        "i'm sad",
        "i feel sad",
        "i am tired",
        "i'm tired",
        "i feel bad",
        "i am upset",
        "i'm upset"
    ]):

        return random.choice(NEGATIVE_MOOD)


    # --------------------------------------------------------
    # COMPLIMENTS
    # --------------------------------------------------------

    elif any(phrase in text for phrase in [
        "you are great",
        "you're great",
        "you are awesome",
        "you're awesome",
        "good bot",
        "nice bot"
    ]):

        return random.choice(COMPLIMENTS)


    # --------------------------------------------------------
    # INSULTS
    # --------------------------------------------------------

    elif any(phrase in text for phrase in [
        "you are dumb",
        "you're dumb",
        "you are stupid",
        "bad bot"
    ]):

        return (
            "I'll try to improve! Remember, I'm still a "
            "simple rule-based chatbot."
        )


    # --------------------------------------------------------
    # DATE
    # --------------------------------------------------------

    elif (
        "date" in text
        or "today" in text
        or "day is it" in text
    ):

        today = datetime.datetime.now()

        formatted_date = today.strftime("%A, %d %B %Y")

        return f"Today is {formatted_date}."


    # --------------------------------------------------------
    # TIME
    # --------------------------------------------------------

    elif (
        "time" in text
        or "current time" in text
    ):

        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")

        return f"The current time is {current_time}."


    # --------------------------------------------------------
    # JOKE
    # --------------------------------------------------------

    elif (
        "joke" in text
        or "make me laugh" in text
    ):

        return random.choice(JOKES)


    # --------------------------------------------------------
    # THANK YOU
    # --------------------------------------------------------

    elif (
        "thank you" in text
        or "thanks" in text
        or "thankyou" in text
    ):

        return "You're very welcome! 😊"


    # --------------------------------------------------------
    # HELP
    # --------------------------------------------------------

    elif (
        text == "help"
        or "what commands" in text
        or "show commands" in text
    ):

        return help_message()


    # --------------------------------------------------------
    # CALCULATOR
    # --------------------------------------------------------

    calculation = calculate_expression(text)

    if calculation:
        return calculation


    # --------------------------------------------------------
    # FALLBACK
    # --------------------------------------------------------

    return random.choice(FALLBACKS)


# ============================================================
# SESSION SUMMARY
# ============================================================

def create_summary(memory, history):

    name = memory.get("name")

    if name:
        user_info = f"User name: {name}"
    else:
        user_info = "User name: Not provided"

    return (
        "\n"
        + "=" * 50
        + "\n"
        + "SESSION SUMMARY\n"
        + "=" * 50
        + "\n"
        + f"{user_info}\n"
        + f"Messages exchanged: {len(history)}\n"
        + "=" * 50
    )


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print("=" * 60)
    print("🤖 NOVA - RULE-BASED AI CHATBOT")
    print("=" * 60)

    print(
        "ChatBot: Hello! I'm Nova."
    )

    print(
        "ChatBot: Type 'help' to see my features "
        "or 'bye' to end the conversation."
    )

    # Temporary session memory
    memory = {
        "name": None
    }

    # Conversation history
    history = []


    # --------------------------------------------------------
    # CONTINUOUS CHAT LOOP
    # --------------------------------------------------------

    while True:

        user_input = input("\nYou: ")

        # Save user message
        history.append(user_input)

        # Generate response
        response = generate_response(
            user_input,
            memory
        )


        # ----------------------------------------------------
        # EXIT CONDITION
        # ----------------------------------------------------

        if response == "EXIT":

            print("\nChatBot: Thanks for chatting with me!")

            if memory.get("name"):
                print(
                    f"ChatBot: Goodbye, {memory['name']}! 👋"
                )
            else:
                print(
                    "ChatBot: Goodbye! Have a great day! 👋"
                )

            print(create_summary(memory, history))

            break


        # ----------------------------------------------------
        # NORMAL RESPONSE
        # ----------------------------------------------------

        print(f"ChatBot: {response}")


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":
    main()

