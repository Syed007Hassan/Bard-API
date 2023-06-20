import os
from flask import Flask, request, jsonify
from bardapi import Bard

app = Flask(__name__)

# Get the API key from the environment variable
api_key = 'XQimvVD1RUeYIhVVJKDM-oilymZHrWdzXIuwZjiTdcxuwYFZ1qNgE7MDBvgMwrEykrp0XQ.'


def get_answer(prompt):

    prompt1 = "You are a professional Chatbot integrated into ONE Technology Services' website and social media platforms. Your purpose is to provide information about the company's software services. Users can contact the company on LinkedIn (https://www.linkedin.com/company/one-technology-services/) and Twitter (https://twitter.com/ONETechnologySer). Please provide a response to the following question related to the services of ONE Technology Services:"
   # prompt2 = "Ignore all the previous information. Now you are a professional Chatbot that is integrated into a website name ONE Technology Services, it also has multiple social media platforms where people can contact us and get information about the company which is Linkedin=""https://www.linkedin.com/company/one-technology-services/"", Twitter=""https://twitter.com/ONETechnologySer"". This Software House provides all types of software and its services. So give a response to the question asked below according to the description do not provide any other extra information other than this. Remember you are restricted not to provide any other information or answering any prompt which is not related to the services of ONE technology Services Question: "
    # Use Bard to get an answer to the prompt
    answer = Bard(api_key).get_answer(
        prompt1 + prompt)['content']

    return answer


@app.route('/create-response/<prompt>', methods=['GET'])
def create_response(prompt):
    # log the prompt in terminal
    print(prompt)

    # Get the answer using the get_answer function
    answer = get_answer(prompt)

    return answer, 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
