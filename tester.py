import json
from perplexity import Perplexity
from json_parser import parse_finder_data_to_json
perplexity = Perplexity("evotingweb12@gmail.com")

answerpath = '/Users/sagarpoudel/Desktop/automate_pplx/perplexityai/plpx_ui/src/'
response_file = f"{answerpath}resp.json"

query = """I am Nepalese undergrad student, I am planning to go foreign to pursue my phd. I have undergrad degree with GPA 3.1 in CSE. I love doing AI, data engineering, DSA and little bit of mathematics. I am searching for research projects that some professors are currently carrying out so that I can do something on this topic and reach out to them by showing my work. 
I need you to perform research and find 3 entries and  prepare a well structured json and give me in json snippet format that contains following. Finally double check if the response is in strict json format. Ensure that every opening bracket { or [ has a corresponding closing bracket } or ]. if any information can not be found then put "" as value
Response should strictly follow the format below:

Professor: {
    name: name of the professor, 
    link: source where this information cite from
},
Research problem statement: {
    Problem_statement:  clear problem statement that has been stated,
    Description: description of problem statement,
    link: Source this information cited from
},
University: {
    name: name of the university the professor is currently working,
    city: city where university located,
    country: country name,
    cutoff: cutoff for enrolling phd student,
    acceptance_ratio: applied students vs enrolled students if mentioned then put else ""
},
seeking_students: {
    is_seeking: are they (currently or in next 5 to 10 months) expecting to join students in their project (true or false),
    Seeking_description: if is_seeking is true, then what they stated about seeking information else "",
    Seeking_stipend: if is_seeking is true, then stipend amount information else "",
    links: [source where these information cited from]
},
research_progress: {
    status: current status of this research as per the latest information you have,
    description: detail description of the information about current progress update,
    link: source of the information you cited
}
    
environment_information: [
    Ideas_update: here you can search the internet if there are some latest information where the problem statement closely related to, i.e. getting this information can have significant impact on progress of the research, like new paper published that closely relates to problem statement or new approaches that has been uploaded to internet that solves the problem statement if not found ""
    ,
    update_from_professor: any recent news or information that has been out or publish by the professor that can help me 
    ,
    Update_from_university: updates that university posted or any recent news from the university that helps me
    
]"""

query2 = """
Provide the following information about the last 10 US presidential election in a JSON format:
{
"electionYear": (year of the election),
"presidentElected": (full name of the winning candidate),
"presidentAge": (age of the winning candidate at the time of election),
"mainOpponent": (full name of the main opposing candidate),
"presidentVotes": (number of votes received by the winning candidate),
"opponentVotes": (number of votes received by the main opponent),
"voteDifference": (difference in votes between the winner and main opponent)
}
Return only the JSON object without any additional text, markdown formatting, or code blocks. Ensure all values are accurate and up-to-date.
"""


query4 = """As a PHD aspirint undergraduate student i am searching for the oppertunity to connect to professor and work with them. Please conduct research to find current relevant ongoing research projects related to AI, data engineering, and data structures and algorithms (DSA) being conducted by professors. Prepare the results in the following strict JSON format:
{
    "entries": [
        {
            "Professor": {
                "name": "",
                "link": ""
            },
            "Research problem statement": {
                "Problem_statement": "",
                "Description": "",
                "link": "" // strictly needed
            },
            "University": {
                "name": "",
                "city": "",
                "country": "",
                "cutoff": "",
                "acceptance_ratio": ""
            },
            "seeking_students": {
                "is_seeking": false,
                "Seeking_description": "",
                "Seeking_stipend": "",
                "links": [""]
            },
            "research_progress": { // strictly needed
                "status": "",
                "description": "",
                "link": ""
            },
            "environment_information": [
                {
                    "Ideas_update": [
                        {
                            "description":"" // Include recent relevant advancements or techniques like works, papers or tools that could impact the research.
                            "source":""// strictly needed
                        },
                        {
                            //Repeat structure
                        }
                    ], 
                    "update_from_professor": "", // Any recent insights or comments from the professor.
                    "Update_from_university": "" // Updates or announcements from the university related to this research.
                }
            ]
        }
    ]
}
Instructions:
1. Ensure that every opening bracket { or [ has a corresponding closing bracket } or ]. If any information cannot be found, please use an empty string "" as the value. Return only the JSON object without any additional text or formatting.
2. Ensure Completeness: Each entry should be filled with as much relevant information as possible. If any information is not available, use an empty string `""` as the value.
3. Focus on Environment Information: In the `environment_information` section, provide updates on recent advancements, techniques, or methodologies that are relevant to the professor's research area. This could include new models, algorithms, or findings that could influence their work.
4. Return Only JSON: Please return only the JSON object without any additional text or formatting.
"""
# Get the answer from the Perplexity API
answer = perplexity.search(query4)

# Create a list to hold completed responses
completed_responses = []

# Iterate through the answers and collect completed ones
for a in answer:
    if a.get('status') == 'completed':
        print(a)  # Print the completed response
        completed_responses.append(a)  # Add to the list



text_value = [item["text"] for item in completed_responses if "text" in item]
text_value = completed_responses[0]["text"]

# Save the completed responses to resp.json
# with open(response_file, 'w') as f:
#     # json.dump(completed_responses, f, indent=4)
#     json.dump(text_value, f, indent=4)

# parse_finder_data_to_json(text_value)

perplexity.close()
