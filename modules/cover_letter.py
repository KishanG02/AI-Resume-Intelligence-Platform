from modules.groq_client import ask_llm


def generate_cover_letter(
    resume_text,
    job_description
):

    prompt = f"""
You are an expert career coach.

Generate a professional cover letter.

Use:

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Requirements:
- Professional tone
- Tailored to the job
- Highlight relevant skills
- Keep under 500 words
- Return only the cover letter
"""

    return ask_llm(prompt)