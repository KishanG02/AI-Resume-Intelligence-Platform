<div align="center">

# 🧠 AI Resume Intelligence Platform

**An end-to-end resume optimization engine — parse, score, rewrite, and export.**  
Powered by Groq's blazing-fast inference and a streamlined Streamlit UI.

</div>

---

## ✨ Features

| Feature | Description |
|---|---|
| 📄 **Resume Parsing** | Upload PDF or DOCX — extracts structured content automatically |
| 📊 **ATS Score Analysis** | Real-time ATS compatibility scoring with actionable breakdown |
| 🔍 **Keyword Gap Detection** | Compares your resume to job descriptions — finds what's missing |
| ✏️ **Resume Rewriting** | Groq-powered rewrites tailored to specific job postings |
| 📈 **Achievement Quantification** | Transforms vague bullets into impact-led, metrics-driven statements |
| 💌 **Cover Letter Generation** | Personalized cover letters from resume + job description input |
| 🎤 **Interview Questions** | Predicts likely interview questions based on your resume content |
| 🗂️ **Version History** | Track and compare all resume versions across sessions |
| 📥 **PDF Export** | Download a polished, ATS-ready PDF built with ReportLab |

---

## 🚀 Live Demo

> 🔗 **[https://ai-resume-intelligence-kxv2gowfesfmj5reqbuwqt.streamlit.app/](https://ai-resume-intelligence-kxv2gowfesfmj5reqbuwqt.streamlit.app/)**

---

## 🛠️ Tech Stack

- **Python** — core backend logic
- **Streamlit** — interactive web UI
- **Groq API** — LLaMA-powered resume rewriting and generation
- **scikit-learn** — TF-IDF keyword gap and ATS scoring
- **PyPDF** — PDF resume parsing
- **python-docx** — DOCX resume parsing
- **ReportLab** — PDF export

---

## ⚡ Quick Start

### 1. Clone and install

```bash
git clone <repo-url>
cd ai-resume-intelligence

python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### 2. Set up your environment

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key_here
```

> Get a free key at [groq.com/keys](https://console.groq.com/keys) — no credit card required.

### 3. Run the app

```bash
streamlit run app.py
```

Opens at **http://localhost:8501**

---

## 📖 Usage

1. **Upload your resume** — drag and drop a PDF or DOCX file
2. **Paste the job description** — the ATS engine scores your match using TF-IDF vectorization
3. **Get scored + rewritten** — Groq rewrites your resume, fills keyword gaps, and quantifies achievements
4. **Export as PDF** — download an ATS-ready PDF and submit immediately

---

## 📁 Project Structure

```
ai-resume-intelligence/
├── modules/            # Feature modules (parser, scorer, rewriter, etc.)
├── uploads/            # Temporary resume storage
├── versions/           # Resume version history
├── app.py              # Main Streamlit entrypoint
├── requirements.txt    # All Python dependencies
└── .env                # API keys (never commit this)
```

---

## 🤝 Contributing

Contributions are welcome! Please open an issue first to discuss what you'd like to change.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

<div align="center">
Built with ⚡ Groq + Streamlit
</div>
