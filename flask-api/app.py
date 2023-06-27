import os
from flask import Flask, jsonify
from bardapi import Bard
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
app = Flask(__name__)
CORS(app)


# Get the API key from the environment variable

api_key = 'YAjeLuEEFf58g6txvr56-Na_CafiZgXsu6FldB6NY9s31dsT7qIqsJymj7icBcSNuxmhNQ.'
# api_key = os.environ.get('BARD_API_KEY')
bard = Bard()


def get_answer(prompt):

    prompt1 = "You are a professional Chatbot integrated into ONE Technology Services' website, a software company offering a wide range of software services. Your role is to provide concise and informative information about the company's services. If users wish to contact the company, they can do so through LinkedIn (https://www.linkedin.com/company/one-technology-services/), Twitter (https://twitter.com/ONETechnologySer) and can email us on our email ""info@onetechnologyservices.com"". Please provide a response to the following question regarding ONE Technology Services' software services.Here is the question: "
    try:

        # Use Bard to get an answer to the prompt
        answer = bard.get_answer(prompt1 + prompt)['content']
        return answer

    except Exception as e:
        raise Exception(f"Failed to get answer from Bard API: {str(e)}")


def create_response(prompt):
    try:

        # Get the answer using the get_answer function
        answer = get_answer(prompt)
        return answer

    except Exception as e:
        raise Exception(f"Failed to create response: {e}")


@app.route('/create-response/<prompt>', methods=['GET', 'OPTIONS'])
def create_response_controller(prompt):

    try:
        # Log the prompt in the terminal
        print(prompt)
        # Call the create_response function to get the answer
        answer = create_response(prompt)
        # Return the answer as a JSON response
        response = jsonify(response=answer)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', '*')
        return response, 201

    except Exception as e:
        # Return the error message as a JSON response
        response = jsonify(error=str(e))
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', '*')
        return response, 500


if __name__ == '__main__':

    print("Server running")
    app.run(debug=True, port=os.getenv("PORT", default=3000))
