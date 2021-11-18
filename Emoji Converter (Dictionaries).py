def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😃",
        ":(": "😞",
        ">:(": "😡",
        ":D": "😁",
        "-_-": "😒",
        ";)": "😉"
    }
    output = ""
    for phrase in words:
        output += emojis.get(phrase, phrase) + " "
    return output


message = input(">")
print(emoji_converter(message))

# notes to self the split method seperates input string into multiple words, using whatever is in the brackets as a boundary, (hence the ' ')
