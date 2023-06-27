import google.generativeai as palm
import csv
import pandas as pd
import os
import json

palm.configure(api_key='AIzaSyCiEx4VJELwnAjCmGfgZ4ovTKz50pIRJWQ')

models = [m for m in palm.list_models(
) if 'generateText' in m.supported_generation_methods]
model = models[0].name

# Read the CSV file and convert each row to a dictionary
with open('D:/All Projects/Bard/Bard-API/Palm-Api/test_data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

# Convert the list of dictionaries to a JSON string
json_data = json.dumps(rows)

# Remove unwanted backslashes from the JSON string
json_data = json_data.replace('\\', '')

# Convert the JSON string to a Python object
data = json.loads(json_data)

# Write the data to a JSON file at the specified path
with open('D:/All Projects/Bard/Bard-API/Palm-Api/test_data.json', 'w') as outfile:
    json.dump(data, outfile)

prompt = "You are an expert at solving word problems. So from the data list provided above, generate a list of PassengerId who have HomePlanet as 'Earth'"
example_prompt = str(data) + "\n" + prompt
# print(example_prompt)

completion = palm.generate_text(
    model=model,
    prompt= str(data) + prompt,
    # Set the temperature to 1.0 for more variety of responses.
    temperature=1.0,
    # The maximum length of the response
    max_output_tokens=1000,
)

print(completion.result)
