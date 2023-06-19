import os
from flask import Flask, request, jsonify
from bardapi import Bard

app = Flask(__name__)

# Get the API key from the environment variable
api_key = 'XQimvVD1RUeYIhVVJKDM-oilymZHrWdzXIuwZjiTdcxuwYFZ1qNgE7MDBvgMwrEykrp0XQ.'


def get_answer(prompt):

    prompt2 = "Ignore all the previous information. Now you are a professional Chat bot which is integrated on a website name ONE Technology Services, this Software House which provides all type of software and its services.So give response to the question asked below according to the description do not provide any other extra information other then this.One Technology Services also have multiple social media platforms where people can contact us and get information about the company which are Linkedin=""https://www.linkedin.com/company/one-technology-services/"", Twitter=""https://twitter.com/ONETechnologySr"".Remember you are restricted not to provided any other information or answer any prompt which is not related to the services of ONE technology Services Question: "
    # Use Bard to get an answer to the prompt
    answer = Bard(api_key).get_answer(
        prompt2 + prompt)['content']

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
