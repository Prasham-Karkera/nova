import openai
from Scarping import *
import output
import env
def generate_summary(text):
    openai.api_key = env.key
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  
        prompt = f"Summarize: {text} under 50 words",
        max_tokens=150, 
        temperature=0.7
    )
    summary_text = response['choices'][0]['text'].strip()
    return summary_text
def set(URL,is_url):
    utext = scrap(URL , is_url)
    if utext == "":
        return "ERROR URL cannot be extracted"
    summary = generate_summary(utext)
    return output.gem(summary)

