from bardapi import Bard
import os
import json


os.environ['_BARD_API_KEY'] = "XQimvVD1RUeYIhVVJKDM-oilymZHrWdzXIuwZjiTdcxuwYFZ1qNgE7MDBvgMwrEykrp0XQ."

# Open the input file
with open('allData.json', 'r') as f:
    # Load the JSON data
    data = json.load(f)

# Initialize variables
chunk_size = 4
chunk_num = 1
chunk = []

# Iterate over the data
for obj in data:
    # Add the object to the current chunk
    chunk.append(obj)
    # Check if the current chunk has reached the desired chunk size
    if len(chunk) >= chunk_size:
        # Write the current chunk to a separate file
        filename = f'chunk{chunk_num}.json'
        with open(filename, 'w') as f:
            json.dump(chunk, f)
        # Increment the chunk number and reset the chunk
        chunk_num += 1
        chunk = []

# Write the final chunk to a separate file if there are remaining objects
if chunk:
    filename = f'chunk{chunk_num}.json'
    with open(filename, 'w') as f:
        json.dump(chunk, f)

# Print the number of chunks created
print(f'{chunk_num} chunks created.')


while True:
    prompt = input("Enter the prompt: ")
    if prompt == "q":
        break

    # Iterate over the chunk files in the directory
    for filename in os.listdir('.'):
        if filename.startswith('chunk') and filename.endswith('.json'):
            # Open the current chunk file and load the JSON data
            with open(filename, 'r') as f:
                data = json.load(f)
            # Prompt the user for a response
            prompt2 = "From the data list provided at the end, your response should not be in JSON format and it should be concise."
            # Use Bard to get an answer to the prompt
            answer = Bard().get_answer(prompt + prompt2 + str(data))['content']
            # Print the answer
            print(answer)
