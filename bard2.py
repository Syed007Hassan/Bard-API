from bardapi import Bard
from dotenv import load_dotenv
import os

load_dotenv()  # Load the environment variables from the .env file

# Retrieve the API key from the environment variables
api_key = os.environ.get('BARD_API_KEY')

# create a list of data

data = [
    {
        "name": "John",
        "age": 30,
        "city": "New York"

    },
    {
        "name": "Peter",
        "age": 40,
        "city": "Boston"
    }
]

while True:
    prompt = input("Enter the prompt: ")
    if prompt == "q":
        break
    prompt2 = "From the data list provided at the end, your response should not be in JSON format and it should be concise."
    # Use Bard to get an answer to the prompt
    answer = Bard(api_key).get_answer(
        prompt2 + str(data) + prompt)['content']
    # Print the answer
    print(answer)
