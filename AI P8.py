from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Create training dataset
messages = [
    "Win a free prize now",
    "Claim your free reward",
    "Congratulations you won cash",
    "Get a special offer today",
    "Please attend the meeting tomorrow",
    "Can we meet after class",
    "Your assignment is due Friday",
    "Please please send me the notes"
]

labels = [
    "Spam", "Spam", "Spam", "Spam",
    "Not Spam", "Not Spam", "Not Spam", "Not Spam"
]

# Convert text into numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

# Train the classifier
model = MultinomialNB()
model.fit(X, labels)

# Test the application
new_message = ["Win cash today"]
new_X = vectorizer.transform(new_message)
prediction = model.predict(new_X)

print("Message:", new_message[0])
print("Prediction:", prediction[0])

# Allow user to enter a message
user_message = input("Enter a message: ")
user_X = vectorizer.transform([user_message])
prediction = model.predict(user_X)

print("Prediction:", prediction[0])
