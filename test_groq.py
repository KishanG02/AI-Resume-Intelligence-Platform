from modules.groq_client import ask_llm

response = ask_llm(
    "Explain ATS score in simple words."
)

print(response)