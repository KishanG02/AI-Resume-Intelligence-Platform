from modules.groq_client import ask_llm


def evaluate_resume(
    resume_text,
    job_description
):

    prompt = f"""
You are an expert resume reviewer.

Evaluate the resume against the job description.

Return:

1. ATS Compatibility Score (1-10)
2. Skills Match Score (1-10)
3. Projects Score (1-10)
4. Achievements Score (1-10)
5. Formatting Score (1-10)
6. Overall Score (1-10)

Also provide:

- Strengths
- Weaknesses
- Recommendations

Resume:
{resume_text}

Job Description:
{job_description}

Format clearly.
"""

    return ask_llm(prompt)