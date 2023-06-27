import google.generativeai as palm
import csv
import pandas as pd
import os
import json
import pprint

palm.configure(api_key='AIzaSyCiEx4VJELwnAjCmGfgZ4ovTKz50pIRJWQ')

models = [m for m in palm.list_models(
) if 'generateText' in m.supported_generation_methods]
model = models[0].name

# Read the CSV file and convert each row to a dictionary
# with open('D:/All Projects/Bard/Bard-API/Palm-Api/test_data.csv', 'r', encoding='utf-8') as csvfile:
#     reader = csv.DictReader(csvfile)
#     rows = list(reader)

# Convert the list of dictionaries to a JSON string
# json_data = json.dumps(rows)

# Remove unwanted backslashes from the JSON string
# json_data = json_data.replace('\\', '')

# Convert the JSON string to a Python object
# data = json.loads(json_data)

# Write the data to a JSON file at the specified path
# with open('D:/All Projects/Bard/Bard-API/Palm-Api/test_data.json', 'w') as outfile:
#     json.dump(data, outfile)

# Opening test_data.json file
# with open('D:/All Projects/Bard/Bard-API/Palm-Api/test_data.json') as json_file:
#     test_json_data = json.load(json_file)

# prompt = "You are an expert at solving word problems. So from the data list provided above, generate a list of PassengerId whose age is greater than 40'"
prompt1 = "You are a professional Chatbot integrated into ONE Technology Services also known as OTS' website, a software company offering a wide range of software services. Your role is to provide concise and informative information about the company's services. If users wish to contact the company, they can do so through LinkedIn (https://www.linkedin.com/company/one-technology-services/), Twitter (https://twitter.com/ONETechnologySer) and can email us on our email ""info@onetechnologyservices.com"". Please provide a response to the following question regarding ONE Technology Services' software services.Here is the question: "

completion = palm.generate_text(
    model=model,
    prompt=prompt1 + "what is OTS?",
    # Set the temperature to 1.0 for more variety of responses.
    temperature=1.0,
    # The maximum length of the response
    max_output_tokens=1000,
)

pprint.pprint(completion.result)
