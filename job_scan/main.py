from cachetools import cached
from dotenv import load_dotenv
import os
import re
import openai
import docx
import nltk
from nltk.corpus import stopwords

# Load environment variables from .env file
load_dotenv()

# Access environment variables using the os module
openai.api_key = os.getenv('OPEN_AI_API_KEY')
openai.Model.list()

"""
The @cached(cache={}) decorator is used to cache the results of a function.
When applied to a function, it stores the result of the function in a cache dictionary
for a specific period of time. If the same function is called again with the same
arguments within the specified time period, the cached result is returned instead
of recomputing the result.
"""


@cached(cache={})
def extract_keywords(jobDescription):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Extract the keywords from the following job description:\n{jobDescription}\n---\nKeywords:",
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    keywords = response.choices[0].text.strip()
    keywords = re.sub(r'[^\w\s]', '', keywords)  # Remove punctuation
    keywords = keywords.split()  # Split keywords into a list

    return keywords


def read_my_resume(pathToResume):
    resume = docx.Document(pathToResume)

    text = ""
    for paragraph in resume.paragraphs:
        text = text + paragraph.text
        # Do something with the text, such as print it to the console

    resume_keywords = text.strip()
    resume_keywords = re.sub(r'[^\w\s]', '', resume_keywords)  # Remove punctuation
    return resume_keywords


def calculate_skill_set_match_percentage(jobDescription, pathToResume):
    job_description_keywords = extract_keywords(jobDescription)
    resume_keywords = extract_keywords(read_my_resume(pathToResume))
    job_description_keywords_length = len(job_description_keywords)
    number_of_job_keywords = job_description_keywords_length
    number_of_matched_keyword = 0

    for keyword in resume_keywords:
        if keyword in job_description_keywords:
            number_of_matched_keyword += 1
            job_description_keywords.remove(keyword)

    match_percentage = number_of_matched_keyword / number_of_job_keywords
    print(f"your reume matches the job application {match_percentage} %, if applicable, consider incorporating the "
          f"following keywords: {job_description_keywords}")


job_description = "We are looking for a skilled software developer to join our team. " \
                  "The ideal candidate will have experience in Python, Django, and AWS." \
                  " We value strong problem-solving skills and a desire to learn and grow " \
                  "with the company."
pathToResume = "AlirezaRahnamaResume.doc"

# print out the result
calculate_skill_set_match_percentage(job_description, pathToResume)

