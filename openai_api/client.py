import openai
import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')

def get_car_ai_bio(model, brand, year):
    prompt= f'''
    Me mostre uma descrição de venda para o carro {brand} {model} {year} em apenas 250 caracteres. 
    Fale coisas específicas desse modelo de carro.
    '''
    openai.api_key = OPENAI_API_KEY
    try:
        response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        max_tokens=1000,
        )
        return response['choices'][0]['text']
    except:
        return "No Description from API"


