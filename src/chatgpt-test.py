import openai

openai.api_key = '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'

while True:
    prompt = input("\nIntroducir pregunta ('exit' para salir): ")
    if prompt == "exit":
        break
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=3000,
    )
    print("ChatGPT: " + response.choices[0].text)
