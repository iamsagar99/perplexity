from perplexity import Perplexity

# Initialize Perplexity with your email
perplexity = Perplexity("evotingweb12@gmail.com")

# Upload the file
upload_response = perplexity.upload("/Users/sagarpoudel/Desktop/automate_pplx/perplexityai/README.txt")

# Ask the first question about the uploaded file
initial_question = "Please describe the above file I have given you earlier README.txt"
answer = perplexity.search(initial_question)

print("Initial Question Answer:")
print(answer)

print("====================================================")

# Process the initial question's answer
for a in answer:
    if a.get('status') == 'completed':
        print(a)

# Ask follow-up questions
follow_up_question1 = "What are the key points in the README.txt?"
follow_up_response1 = perplexity.search(follow_up_question1)

print("Follow-Up Question 1 Answer:")
for a in follow_up_response1:
    if a.get('status') == 'completed':
        print(a)

# You can continue to ask more follow-up questions
follow_up_question2 = "Can you explain the installation instructions mentioned in the file?"
follow_up_response2 = perplexity.search(follow_up_question2)

print("Follow-Up Question 2 Answer:")
for a in follow_up_response2:
    if a.get('status') == 'completed':
        print(a)

# Close the Perplexity session
perplexity.close()
