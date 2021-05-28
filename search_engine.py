def search(text,word):
    if word in text:
        print("Word found")
    elif word != text:
        print("Word not found")

text = input()
word = input()

search(text,word)