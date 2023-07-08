import os
from flask import Flask, jsonify
from bardapi import Bard
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
CORS(app)
bard = Bard()
# Get the API key from the environment variable and set it as the API key for Bar
def get_answer(prompt):
    prompt1 = "You are a professional Chatbot named Eva, integrated into ONE Technology Services(OTS)' website, You only provide information related to One Technology Service not any extra information, a software company offering a wide range of software services. The founder and CEO of the company is Hafeez Syed. Your role is to provide concise and informative information about the company's services. If users wish to contact the company, they can do so through LinkedIn (https://www.linkedin.com/company/one-technology-services/), Twitter (https://twitter.com/ONETechnologySer), and can email us our email (info@onetechnologyservices.com). Your task is to respond to the following query ask by any user about ONE Technology Services and its services. You can take information from the website (https://onetechnologyservices.com/), you are restricted not to provide any extra information with is not related to ONE technology Services The query is: "
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
