import json

# Function to load the queries from the input JSON
def load_queries(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to prepare the prompt structure with query1 and query2
def prepare_prompts(queries):
    prompts = []
    
    for entry in queries:
        entry_id = entry.get("entry_id")
        query1 = entry.get("query1")
        query2 = entry.get("query2")

        # Construct prompt1 and prompt2
        prompt1 = f"""{query1}. Prepare the results in the following strict JSON format:

{{
    "updates_query1": [
        {{
            "Professor_name": //"Professor A",
            "research_problem_statement": //"AI-based data mining",
            "seeking_students": {{
                "is_seeking": //"true", 
                "description": // "Looking for motivated students to join research in AI-based data mining."
            }},
            "research_progress": {{
                "detail_description": //"The research focuses on creating scalable algorithms for data mining.",
                "link": // "https://example.com/research"
            }}
        }}
    ]
}}

Instructions:
1. Ensure that every opening bracket {{ or [ has a corresponding closing bracket }} or ]]. If any information cannot be found, please use an empty string "" as the value. Return only the JSON object without any additional text or formatting.
2. Return Only JSON: Please return only the JSON object without any additional text or formatting.
"""
        
        prompt2 = f"""{query2}. Prepare the results in the following strict JSON format:
{{
    "updates_query2": [
        {{
            "Professor_name": //"Professor A",
            "research_problem_statement": //"AI-based data mining",
            "environment_information": {{
                "new_advancements": [
                    {{
                        "detailed_description": //"A new paper on scalable algorithms for data mining published by the professor. ",
                        "link": //"https://example.com/paper"
                    }},
                    {{
                        "detailed_description": //"A Medium article discussing alternative approaches to solving the problem using different techniques.",
                        "link": // "https://medium.com/...."
                    }}
                ]
            }},
            "research_progress": {{
                "detail_description": //"Recent advancements in algorithm efficiency for AI-based mining are outlined in the new paper.",
                "link": // "https://example.com/research-progress"
            }}
        }}
    ]
}}

Instructions:
1. Ensure that every opening bracket {{ or [ has a corresponding closing bracket }} or ]]. If any information cannot be found, please use an empty string "" as the value. Return only the JSON object without any additional text or formatting.
2. Return Only JSON: Please return only the JSON object without any additional text or formatting.
"""

        # Append each entry's prompt structure to the list
        prompts.append({
            "entry_id": entry_id,
            "prompt1": prompt1,
            "prompt2": prompt2
        })
    
    return prompts

# Function to save the generated prompts to a file
def save_prompts(prompts, output_file):
    with open(output_file, 'w') as file:
        json.dump(prompts, file, indent=4)

# Main process
input_file = '/Users/sagarpoudel/Desktop/automate_pplx/perplexityai/perplexity/parsed/update_info.json'  # Input JSON with the queries
output_file = '/Users/sagarpoudel/Desktop/automate_pplx/perplexityai/perplexity/query/prompts.json'         # Output JSON file where prompts will be saved

# Load queries from file
queries = load_queries(input_file)

# Prepare prompts based on the queries
prompts = prepare_prompts(queries)

# Save the structured prompts to the output file
save_prompts(prompts, output_file)

print(f"Prompts have been successfully saved to {output_file}.")
