from transformers import pipeline

# Load a free model from Hugging Face (like FLAN-T5 or similar)
agent = pipeline("text2text-generation", model="google/flan-t5-base")

def break_down_task(user_input):
    prompt = f"Break down this task into a step-by-step plan: {user_input}"
    response = agent(prompt, max_length=256, do_sample=True)[0]["generated_text"]
    return response

