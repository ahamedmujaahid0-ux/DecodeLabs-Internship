from textblob import TextBlob

text = input("Enter some text: ")

blob = TextBlob(text)

print("Corrected text:", blob.correct())
print("Words:", blob.words)
