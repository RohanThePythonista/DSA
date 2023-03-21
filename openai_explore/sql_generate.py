import openai
openai.api_key = "YOUR_API_KEY"

prompt = (f"Generate SQL code to {action} {object} from {table}")

model_engine = "text-davinci-002"
temperature = 0.7
max_tokens = 256
stop_sequence = "\n\n"

response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens,
    stop=stop_sequence
)

generated_code = response.choices[0].text.strip()

connection.execute(generated_code)

"""
openai.api_key = "YOUR_API_KEY"

def generate_sql_query(prompt, max_tokens=100, temperature=0.5, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
    )
    return response.choices[0].text

prompt = input("Enter your prompt - What data do you need?: ")
print(generate_sql_query(prompt))
"""

