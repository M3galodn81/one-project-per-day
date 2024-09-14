import requests
import json

def generate_random_quote():
    response = requests.get('https://zenquotes.io/api/random')
    if response.status_code == 200:
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']

        return (f'Random Quote: \n {quote} \n Author: {author}')

    else:
        return (f'Failed to fetch a quote (Status Code {response.status_code})')




