import os
from flask import Flask, request, jsonify
from services.response_service import ResponseService
from repositories.response_repository import ResponseRepository
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


# Get the API key from the environment variable
api_key = 'XQimvVD1RUeYIhVVJKDM-oilymZHrWdzXIuwZjiTdcxuwYFZ1qNgE7MDBvgMwrEykrp0XQ.'
# api_key = os.environ.get("BARD_API_KEY")


# Initialize the service and repository
response_service = ResponseService(api_key)
response_repository = ResponseRepository()


@app.route('/create-response/<prompt>', methods=['GET', 'OPTIONS'])
def create_response_controller(prompt):
    try:
        # Log the prompt in the terminal
        print(prompt)

        # Call the create_response method of the ResponseService to get the answer
        answer = response_service.create_response(prompt)

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
    # Use the PORT environment variable provided by Azure
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
