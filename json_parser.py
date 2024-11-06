import json

finder_parsed_path = "/Users/sagarpoudel/Desktop/automate_pplx/perplexityai/perplexity/parsed/finder_parsed.json"

def parse_finder_data_to_json(data_string):
    try:
        # Load the string as a dictionary
        raw_data = json.loads(data_string)
        
        # Check if the "answer" key exists and parse its contents
        if "answer" in raw_data:
            structured_data = json.loads(raw_data["answer"])
        else:
            raise ValueError("Key 'answer' not found in the data")

        # Save to a JSON file
        with open(finder_parsed_path, "w") as json_file:
            json.dump(structured_data, json_file, indent=4)
        print("Data successfully parsed and saved to structured_data.json")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")



def parse_update_data_to_json(data_string):
    try:
        # Load the string as a dictionary
        raw_data = json.loads(data_string)
        
        # Check if the "answer" key exists and parse its contents
        if "answer" in raw_data:
            structured_data = json.loads(raw_data["answer"])
        else:
            raise ValueError("Key 'answer' not found in the data")
        
        # Return the structured data (parsed JSON)
        return structured_data
        
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
