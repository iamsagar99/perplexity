import json

# Assuming ANSWER contains the parsed data as a list of dictionaries
ANSWER = [
   {'status': 'completed', 'uuid': 'cb035c58-9e1b-41d7-8f06-4ca5ead9d55e', 'read_write_token': 'fe480c87-988d-4a71-9e32-a08677181b81', 'frontend_context_uuid': '9fc04b68-7064-4bd6-878c-f571ec709e87', 'text': '{"answer": "The meaning of life is a profound and subjective question that has intrigued humanity for centuries, often reflecting individual beliefs, cultural backgrounds, and personal experiences. For some, it may revolve around the pursuit of happiness, love, and connection with others; for others, it might be about seeking knowledge, contributing to society, or achieving personal goals. Philosophers, theologians, and scientists have offered diverse perspectives, suggesting that meaning can be found in relationships, creativity, spirituality, or the quest for understanding the universe. Ultimately, the meaning of life is often seen as a journey of self-discovery where each person crafts their own purpose based on their values and aspirations.", "web_results": [], "chunks": ["The meaning of", " life is a profound", " and subjective", " question that", " has intrigued", " humanity for", " centuries, often", " reflecting individual", " beliefs, cultural", " backgrounds, and", " personal experiences", ". For some, it", " may revolve around", " the pursuit of", " happiness, love", ", and connection", " with others; for", " others, it might", " be about seeking", " knowledge, contributing", " to society, or", " achieving personal", " goals. Philosoph", "ers, theologians, and", " scientists have", " offered diverse", " perspectives", ", suggesting that", " meaning can be", " found in relationships", ", creativity, spirituality", ", or the quest", " for understanding", " the universe", ". Ultimately, the", " meaning of life", " is often seen", " as a journey", " of self-discovery where", " each person crafts", " their own purpose", " based on their", " values and aspirations", "."], "extra_web_results": []}', 'final': True, 'text_completed': True, 'backend_uuid': '809b11dd-c32e-40f5-bb08-67da06582d8a', 'context_uuid': '9eeef1f3-851a-4f63-8081-e1ce99bd5239', 'media_items': [], 'widget_data': [], 'knowledge_cards': [], 'expect_search_results': 'false', 'plan': None, 'mode': 'concise', 'search_focus': 'internet', 'gpt4': False, 'display_model': 'turbo', 'attachments': [], 'expect_sponsored_results': False, 'personalized': True, 'subtext': 'NONE', 'step_type': 'FINAL', 'sources': None, 'related_queries': ['How do different cultures interpret the meaning of life', 'What are some philosophical theories about the meaning of life', 'Can science provide insights into the meaning of life', 'How do religious beliefs influence the concept of the meaning of life', 'What role does personal happiness play in the meaning of life'], 'query_str': 'What is the meaning of life? Just write one paragraph only.', 'thread_title': 'What is the meaning of life? Just write one paragraph only.', 'thread_access': 2, 'thread_url_slug': 'what-is-the-meaning-of-life-ju-gJsR3cMuQPW7CGfaBlgtig', 'author_username': None, 'author_image': None, 's3_social_preview_url': 'https://ppl-ai-public.s3.amazonaws.com/static/img/pplx-default-preview.png', 'updated_datetime': '2024-10-29T10:12:33.438606', 'privacy_state': 'NONE', 'expiry_time': None, 'bookmark_state': 'NOT_BOOKMARKED', 'prompt_source': None, 'query_source': None}
]

# Function to structure the response
def structure_response(data):
    structured_response = "## The Meaning of Life\n\n"
    structured_response += "The meaning of life is a complex and subjective topic. Here are the key points:\n\n"

    for entry in data:
        if 'answer' in entry:
            structured_response += f"- {entry['answer']}\n\n"

    return structured_response

# Create a structured response
structured_output = structure_response(ANSWER)

# Save the structured response to a file
with open('structured_response.txt', 'w') as file:
    file.write(structured_output)

print("Structured response saved to 'structured_response.txt'.")