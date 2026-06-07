from transformers import pipeline

print("=" * 60)
print("PROMPTCRAFT AI WRITER")
print("=" * 60)

generator = pipeline(
    "text-generation",
    model="gpt2"
)

prompt = input("\nEnter a topic: ")

result = generator(
    prompt,
    max_length=120,
    num_return_sequences=1,
    truncation=True
)

print("\nGenerated Content:\n")
print(result[0]["generated_text"])