english_to_german = {
    "good day": "Guten Tag!",
    "good morning": "Guten Morgen!",
    "goodbye": "Auf Wiedersehen!",
    "how are you": "Wie geht's?",
    "my name is python": "Mein Name ist Python!",
    "do you speak english": "Sprechen sie Englisch?",
    "where is the bathroom": "Wo ist die Toilette?",
    "thank you": "Danke!",
    "i am sorry": "Es tut mir leid!",
    "a large beer please": "Ein grosses Bier, bitte!"
}


def translate():
    user_input = input("English sentence to translate: ")
    cleaned_input = ""
    for char in user_input:
        if char.isalpha() or char.isspace():
            cleaned_input += char.lower()

    translation = english_to_german.get(cleaned_input, "No translation found!")
    print(translation)


if __name__ == "__main__":
    translate()