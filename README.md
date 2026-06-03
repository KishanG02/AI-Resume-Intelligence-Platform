# AI Resume Intelligence Platform

An AI-powered resume optimization platform built with Streamlit and Groq.

## Features

- Resume Parsing (PDF/DOCX)
- ATS Score Analysis
- Keyword Gap Detection
- Resume Rewriting
- Achievement Quantification
- Cover Letter Generation
- Interview Question Generation
- Resume Evaluation Pipeline
- Resume Version History
- PDF Export

## Tech Stack

- Python
- Streamlit
- Groq API
- Scikit-Learn
- PyPDF
- Python-Docx
- ReportLab

## Installation

```bash
git clone <repo-url>
cd ai-resume-intelligence

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

Run:

```bash
streamlit run app.py
```

## Project Structure

```text
modules/
uploads/
versions/
app.py
requirements.txt
```