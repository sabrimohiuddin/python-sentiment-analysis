# Task 1: Import TextBlob and confirm it loaded.
from textblob import TextBlob

print("Task 1 - TextBlob imported successfully.")

# Task 2: Analyze one product review.
sample_text = (
    "I absolutely love this product! "
    "The quality is excellent and it arrived on time."
)
sentiment = TextBlob(sample_text).sentiment

print("\nTask 2 - Single product review")
print("Original text:", sample_text)
print("Polarity:", sentiment.polarity)
print("Subjectivity:", sentiment.subjectivity)

# Task 3: Score each customer comment so we can compare the feedback.
feedback_comments = [
    "The service was fantastic and the staff was very helpful.",
    "I am unhappy with the product quality and delivery was delayed.",
    "The product is okay, but it could be improved.",
    "Amazing experience! I am very satisfied with my purchase.",
]


def analyze_sentiment(text):
    return TextBlob(text).sentiment.polarity


print("\nTask 3 - Customer feedback")
for comment in feedback_comments:
    polarity = analyze_sentiment(comment)
    print(f"Feedback: {comment}")
    print(f"Sentiment polarity: {polarity}")
    print()