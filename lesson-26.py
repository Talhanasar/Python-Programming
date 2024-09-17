def emoji_converted(message):
    seperate_words = message.split(' ')
    emoji = {
        ":)": "😊",
        ":(": "😔"
    }
    output = ""
    for word in seperate_words:
        output += emoji.get(word, word) + " "
    return output


message = input("Type you message: ")
result = emoji_converted(message)
print(result)