import os
from openai import OpenAI


export OPENAI_API_KEY="your_key_here"

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(prompt):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content


def main():
    # Example inputs to test the model
    prompts = [
        "Explain what a neural network is in simple terms.",
        "Give me 3 pros and cons of using AI in education.",
        "Write a short Python function that adds two numbers."
    ]

    for i, prompt in enumerate(prompts, 1):
        print(f"\n--- Prompt {i} ---")
        print("INPUT:", prompt)
        
        output = ask_llm(prompt)
        
        print("\nOUTPUT:")
        print(output)
        print("\n" + "-"*50)


if __name__ == "__main__":
    main()
