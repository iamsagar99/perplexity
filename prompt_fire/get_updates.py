import json
from datetime import datetime
import os
import sys

current_script_path = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_script_path)
sys.path.append(parent_dir)

from perplexity import Perplexity
from json_parser import parse_update_data_to_json


current_script_path = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_script_path)
sys.path.append(parent_dir)

# Initialize Perplexity with your credentials
perplexity = Perplexity("evotingweb12@gmail.com")

new_updates_file = '/Users/sagarpoudel/Desktop/automate_pplx/updates/new_updates.json'

# Load prompts from prompts.json
with open('/Users/sagarpoudel/Desktop/automate_pplx/perplexityai/perplexity/query/prompts.json', 'r') as f:
    prompts = json.load(f)

# Load existing updates from new_updates.json if it exists
try:
    with open(new_updates_file, 'r') as f:
        new_updates = json.load(f)
except FileNotFoundError:
    # If the file doesn't exist, initialize with an empty list
    new_updates = []

for entry in prompts:
    entry_id = entry.get('entry_id')
    completed_responses1 = []
    completed_responses2 = []
    prompt1 = entry.get('prompt1')  
    prompt2 = entry.get('prompt2')

    print("======================prompts=====================")
    print(prompt1)
    print(prompt2)
    print("===================================================")
    

    # Get responses from Perplexity for prompt1 and prompt2
    answer1 = perplexity.search(prompt1)
    print("======================answer1=====================")
    print(answer1)
    print("===================================================")

    answer2 = perplexity.search(prompt2)
    print("======================answer2=====================")
    print("===================================================")
    print(answer2)
    for a in answer1:
        if a.get('status') == 'completed':
            completed_responses1.append(a) 
    for a in answer2:
        if a.get('status') == 'completed':
            completed_responses2.append(a) 

    text_value1 = [item["text"] for item in completed_responses1 if "text" in item]
    text_value2 = [item["text"] for item in completed_responses2 if "text" in item]
    print("======================text_value=====================")
    
    print(text_value1)
    print("===================================================")
    print(text_value2)
    print("===================================================")
    # Parse the responses into structured data
    parsed_prompt1 = parse_update_data_to_json(text_value1)
    parsed_prompt2 = parse_update_data_to_json(text_value2)
    print("======================parsed_prompt=====================")
    print(parsed_prompt1)
    print("===================================================")
    print(parsed_prompt2)
    print("===================================================")
    # Get the current date and time
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Find the entry for the current entry_id or create a new one
    entry_exists = False
    for update in new_updates:
        if update['entry_id'] == entry_id:
            # Append the new response for this entry_id
            update['updates'].append({
                'date': current_datetime,
                'prompt1': parsed_prompt1,
                'prompt2': parsed_prompt2
            })
            entry_exists = True
            break

    if not entry_exists:
        # Create a new entry for this entry_id
        new_updates.append({
            'entry_id': entry_id,
            'updates': [{
                'date': current_datetime,
                'prompt1': parsed_prompt1,
                'prompt2': parsed_prompt2
            }]
        })

print("======================parsed_prompt=====================")
print(new_updates)
print("===================================================")
# Save the updated new_updates.json file
with open(new_updates_file, 'w') as f:
    json.dump(new_updates, f, indent=4)

# Close the Perplexity session
perplexity.close()
