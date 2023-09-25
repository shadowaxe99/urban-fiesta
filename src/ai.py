import openai

openai.api_key = 'YOUR_API_KEY'


def interact_with_ai(input_text):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=input_text,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text
