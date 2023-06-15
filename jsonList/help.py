import json
import os

# Open the input file
with open('a.json', 'r') as f:
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
        with open(f'chunk{chunk_num}.json', 'w') as f:
            json.dump(chunk, f)
        # Increment the chunk number and reset the chunk
        chunk_num += 1
        chunk = []

# Write the final chunk to a separate file if there are remaining objects
if chunk:
    with open(f'chunk{chunk_num}.json', 'w') as f:
        json.dump(chunk, f)

# Print the number of chunks created
print(f'{chunk_num} chunks created.')
