import json

parsed_path = "/Users/sagarpoudel/Desktop/automate_pplx/perplexityai/perplexity/parsed/"

finder_path = f"{parsed_path}/finder_parsed.json"
# Load the JSON data from myjson.json
with open(finder_path, 'r') as file:
    structured_json = json.load(file)

# Function to create Query 1
def generate_query_1(entry):
    entry_id = entry.get("id")
    professor = entry.get("Professor", {})
    research_problem = entry.get("Research problem statement", {})
    university = entry.get("University", {})
    seeking_students = entry.get("seeking_students", {})
    
    query_1 = (
        f"Please search for recent advancements or updates in the research conducted by {professor.get('name', '')} "
        f"[{professor.get('link', '')}]. The research problem statement is: '{research_problem.get('Problem_statement', '')}'. "
        f"The associated university is {university.get('name', '')}, {university.get('country', '')}. "
        f"Additionally, find out if the university is currently seeking students interested in this research domain, "
        f"especially if previously it was not. If the university is seeking students now, provide any updated descriptions, "
        f"stipend details, and relevant links. Please include all sources with links for verification and credibility."
    )
    return query_1

# Function to create Query 2
def generate_query_2(entry):
    entry_id = entry.get("id")
    research_progress = entry.get("research_progress", {})
    environment_info = entry.get("environment_information", [{}])[0]
    
    query_2 = (
        f"Investigate the latest updates and progress related to the ongoing research described as: "
        f"'{research_progress.get('description', '')}'. Specifically, look for new methodologies, discoveries, or recent advancements "
        f"that have been introduced or are being explored in the field. Additionally, review any new or emerging techniques that could "
        f"enhance the research. Search for any recent publications, news articles, or academic resources detailing advancements in this area. "
        f"Furthermore, examine the following existing updates for new information: {json.dumps(environment_info, indent=2)}. "
        f"Provide detailed summaries and links to sources for a comprehensive understanding."
    )
    return query_2

# Generate the output JSON structure
updates_info = []
update_path = f"{parsed_path}/update_info.json"
for entry in structured_json["entries"]:
    # professor_name = entry.get("Professor", {}).get("name", "")
    entryId = entry.get("id", "")
    # research_problem_statement = entry.get("Research problem statement", {}).get("Problem_statement", "")
    query1 = generate_query_1(entry)
    query2 = generate_query_2(entry)
    
    updates_info.append({
        "entry_id": entryId,
        # "Professor_name": professor_name,
        # "research_problem_statement": research_problem_statement,
        "query1": query1,
        "query2": query2
    })

# Write the output to updates_info.json
with open(update_path, 'w') as output_file:
    json.dump(updates_info, output_file, indent=4)

# design prompt and store in same way

print("updates_info.json has been created successfully!")
