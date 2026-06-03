from modules.groq_client import ask_llm


def quantify_achievements(resume_text):

    prompt = f"""
You are an expert resume coach.

TASK:
Improve and quantify resume achievements.

RULES:
- Use action verbs
- Add measurable impact where reasonable
- Do not invent unrealistic numbers
- Improve weak bullet points
- Keep output professional

RESUME:

{resume_text}

Return the improved achievement bullets only.
"""

    return ask_llm(prompt)