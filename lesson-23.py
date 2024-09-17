message = input("Typer your message: ")
seperate_words = message.split(' ')
print(seperate_words)

emoji = {
    ":)": "😊",
    ":(": "😔"
}
output = ""
for word in seperate_words:
    output += emoji.get(word, word) + " "
print(output)