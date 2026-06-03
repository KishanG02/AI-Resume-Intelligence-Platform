from modules.groq_client import ask_llm


def generate_interview_questions(
    resume_text,
    job_description
):

    prompt = f"""
You are a senior technical interviewer.

Based on the candidate resume and job description,
generate:

- 10 Technical Questions
- 5 Behavioral Questions
- 5 Project-Based Questions

Resume:
{resume_text}

Job Description:
{job_description}

Format the output clearly.
"""

    return ask_llm(prompt)