from bardapi import Bard
from dotenv import load_dotenv
import os

load_dotenv()  # Load the environment variables from the .env file

api_key = os.getenv('BARD_API_KEY1')  # Retrieve the API key from the environment variables

while input != "q":
    question = input("Enter Prompt: ")
    print(Bard(api_key).get_answer(question)['content'])
