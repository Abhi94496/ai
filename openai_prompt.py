import openai as OpenAI
import os

os.environ['API_KEY'] = 'xyz'
openai.api_key = os.getenv('API_KEY')
client = OpenAI(api_key = os.environ.get('API_KEY'))

promt = 'roast me by previous prompts of mine'

response = client.chat.completions.create(messages=[ 
                                                { 'role' : "user",
                                                    'content' : promt,
                                                      'max_tokens' : 300 }],
                                          model = "gpt-3.5-turbo")

print(response.choices[0].message.content)


