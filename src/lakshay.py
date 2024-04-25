# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

completion = client.chat.completions.create(
    model="TheBloke/Mistral-7B-Instruct-v0.2-GGUF/mistral-7b-instruct-v0.2.Q4_K_S.gguf",
    messages=[
        {"role": "system", "content": """
Below is an instruction that describes a task. Write a response that appropriately completes the request.
"""},
        {"role": "user", "content": 'list the meaning of word "empathetic", also list 3 examples along with antonyms and synonyms'}
    ],
    temperature=0.7,
)

print(completion.choices[0].message)
