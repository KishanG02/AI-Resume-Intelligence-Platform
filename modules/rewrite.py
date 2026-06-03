from modules.groq_client import ask_llm


def rewrite_resume(
    resume_text,
    job_description
):

    prompt = f"""
You are an expert ATS Resume Writer.

TASK:
Rewrite the resume to better match the job description.

RULES:
- Improve ATS compatibility
- Add relevant keywords naturally
- Improve bullet points
- Use strong action verbs
- Keep information truthful
- Do not invent experience

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Return only the improved resume.
"""

    return ask_llm(prompt)