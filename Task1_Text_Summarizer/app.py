from transformers import pipeline

print("Loading AI Model... Please wait.")

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

with open("article.txt", "r", encoding="utf-8") as file:
    text = file.read()

summary = summarizer(
    text,
    max_length=60,
    min_length=20,
    do_sample=False
)

print("\nSUMMARY:\n")
print(summary[0]["summary_text"])