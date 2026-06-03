# Importing the necessary libraries
import os
import streamlit as st

from datetime import (
    datetime
)

from modules.ats import (
    extract_keywords,
    calculate_ats_score
)

from modules.parser import (
    parse_pdf,
    parse_docx
)

from modules.keyword_gap import (
    find_keyword_gaps
)

from modules.rewrite import (
    rewrite_resume
)

from modules.achievement import (
    quantify_achievements
)

from modules.cover_letter import (
    generate_cover_letter
)

from modules.interview import (
    generate_interview_questions
)

from modules.evaluator import (
    evaluate_resume
)

from modules.pdf_export import (
    create_pdf
)

st.set_page_config(
    page_title="AI Resume Intelligence Platform",
    page_icon="📄",
    layout="wide"
)

if "improved_resume" not in st.session_state:
    st.session_state.improved_resume = ""

if "cover_letter" not in st.session_state:
    st.session_state.cover_letter = ""

if "interview_questions" not in st.session_state:
    st.session_state.interview_questions = ""

if "evaluation_report" not in st.session_state:
    st.session_state.evaluation_report = ""

with st.sidebar:

    st.title("🤖 AI Resume Intelligence")

    st.success("🟢 Groq API Connected")

    st.markdown("---")

    st.subheader("Features")

    st.write("✅ ATS Analysis")
    st.write("✅ Resume Rewrite")
    st.write("✅ Achievements")
    st.write("✅ Cover Letters")
    st.write("✅ Interview Prep")
    st.write("✅ Evaluation")

    st.markdown("---")

    st.caption(
        "Built with Streamlit + Groq"
    )

st.title("📄 AI Resume Intelligence Platform")

resume_text = ""
job_description = ""
word_count = 0
char_count = 0

st.markdown(
    """
Analyze resumes, improve ATS scores,
generate cover letters, prepare for interviews,
and optimize job applications using AI.
"""
)

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

st.subheader("📝 Job Description")

job_description = st.text_area(
    "Paste Job Description Here",
    height=250
)

if uploaded_file:

    if uploaded_file.name.endswith(".pdf"):
        resume_text = parse_pdf(uploaded_file)

    elif uploaded_file.name.endswith(".docx"):
        resume_text = parse_docx(uploaded_file)

    st.subheader("📊 Resume Statistics")

    word_count = len(resume_text.split())
    char_count = len(resume_text)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Words", word_count)

    with col2:
        st.metric("Characters", char_count)

    st.subheader("📄 Extracted Resume Text")

    st.text_area(
        label="Resume Content",
        value=resume_text,
        height=500
    )

    

    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
        [
            "🎯 ATS Analysis",
            "🤖 Resume Rewrite",
            "📈 Achievements",
            "📄 Cover Letter",
            "🎤 Interview Prep",
            "📊 Evaluation",
            "📂 Version History"
        ]
    )

    with tab1:

        st.subheader("ATS Analysis")

        if not job_description.strip():
            st.warning(
                "Please paste a Job Description first."
            )

        else:

            resume_keywords = extract_keywords(
                resume_text
            )

            jd_keywords = extract_keywords(
                job_description
            )

            score = calculate_ats_score(
                resume_keywords,
                jd_keywords
            )

            matched, missing = find_keyword_gaps(
                resume_keywords,
                jd_keywords
            )

            st.subheader("🎯 ATS Score")

            st.metric(
                "Score",
                f"{score}%"
            )

            if score >= 80:
                st.success("Excellent ATS Match")
            elif score >= 60:
                st.warning("Good Match - Add Missing Keywords")
            else:
                st.error("Low ATS Match - Resume Needs Improvement")

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("✅ Matched Keywords")

                for keyword in sorted(matched):
                    st.success(keyword)

            with col2:
                st.subheader("❌ Missing Keywords")

                for keyword in sorted(missing):
                    st.error(keyword)

        st.divider()
    #ATS code ends here
    with tab2:

        st.subheader("🤖 AI Resume Rewriter")

        if st.button("Rewrite Resume for ATS"):

            if not job_description.strip():

                st.warning(
                    "Please paste a Job Description first."
                )

            else:

                with st.spinner(
                    "Optimizing Resume..."
                ):

                    improved_resume = rewrite_resume(
                        resume_text,
                        job_description
                    )

                st.success(
                    "Resume Optimized Successfully"
                )

                st.text_area(
                    "Optimized Resume",
                    improved_resume,
                    height=500
                )

                st.download_button(
                    label="Download Optimized Resume",
                    data=improved_resume,
                    file_name="optimized_resume.txt",
                    mime="text/plain"
                )

        st.divider()
    #Re-write code ends here
    with tab3:

        st.subheader("📈 Achievement Quantifier")

        if st.button("Improve Achievement Statements"):

            with st.spinner(
                "Enhancing achievements..."
            ):

                quantified_text = quantify_achievements(
                    resume_text
                )

            timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )

            filename = (
                f"versions/achievement_{timestamp}.txt"
            )

            with open(filename, "w") as f:
                f.write(quantified_text)

            st.success(
                "Achievements Improved"
            )

            st.text_area(
                "Enhanced Achievements",
                quantified_text,
                height=400
            )

            st.download_button(
                label="Download Improved Achievements",
                data=quantified_text,
                file_name="achievement_improvements.txt",
                mime="text/plain"
            )
            pdf_file = create_pdf(
                    quantified_text,
                    "achievement_improvements.pdf"
                )

            with open(pdf_file, "rb") as f:

                st.download_button(
                    label="Download Achievement Improvements PDF",
                    data=f,
                    file_name="achievement_improvements.pdf",
                    mime="application/pdf"
                )

        st.divider()
    #Achievements code ends here
    with tab4:

        st.subheader("📄 AI Cover Letter Generator")

        if st.button("Generate Cover Letter"):

            if not job_description.strip():

                st.warning(
                    "Please paste a Job Description first."
                )

            else:

                with st.spinner(
                    "Generating Cover Letter..."
                ):

                    cover_letter = generate_cover_letter(
                        resume_text,
                        job_description
                    )

                timestamp = datetime.now().strftime(
                    "%Y%m%d_%H%M%S"
                )

                filename = (
                    f"versions/cover_letter_{timestamp}.txt"
                )

                with open(filename, "w") as f:
                    f.write(cover_letter)

                st.success(
                    "Cover Letter Generated"
                )

                st.text_area(
                    "Cover Letter",
                    cover_letter,
                    height=500
                )

                st.download_button(
                    label="Download Cover Letter",
                    data=cover_letter,
                    file_name="cover_letter.txt",
                    mime="text/plain"
                )

                pdf_file = create_pdf(
                    cover_letter,
                    "cover_letter.pdf"
                )

                with open(pdf_file, "rb") as f:

                    st.download_button(
                        label="Download Cover Letter PDF",
                        data=f,
                        file_name="cover_letter.pdf",
                        mime="application/pdf"
                    )
            

        st.divider()
    #Cover Letter code ends here
    with tab5:

        st.subheader("🎤 AI Interview Question Generator")

        if st.button("Generate Interview Questions"):

            if not job_description.strip():

                st.warning(
                    "Please paste a Job Description first."
                )

            else:

                with st.spinner(
                    "Generating Interview Questions..."
                ):

                    st.session_state.interview_questions = (
                        generate_interview_questions(
                            resume_text,
                            job_description
                        )
                    )

                timestamp = datetime.now().strftime(
                    "%Y%m%d_%H%M%S"
                )

                filename = (
                    f"versions/interview_questions_{timestamp}.txt"
                )

                with open(filename, "w") as f:
                    f.write(
                        st.session_state.interview_questions
                    )

        if st.session_state.interview_questions:

            st.text_area(
                "Interview Questions",
                st.session_state.interview_questions,
                height=500
            )

            st.download_button(
                label="Download Questions",
                data=st.session_state.interview_questions,
                file_name="interview_questions.txt",
                mime="text/plain"
            )
            pdf_file = create_pdf(
                    interview_questions,
                    "interview_questions.pdf"
                )

            with open(pdf_file, "rb") as f:

                st.download_button(
                    label="Download Interview Questions PDF",
                    data=f,
                    file_name="interview_questions.pdf",
                    mime="application/pdf"
                )

        st.divider()
    #Interview Prep code ends here
    with tab6:

        st.subheader("📊 Resume Evaluation Pipeline")

        if st.button("Evaluate Resume"):

            if not job_description.strip():

                st.warning(
                    "Please paste a Job Description first."
                )

            else:

                with st.spinner(
                    "Evaluating Resume..."
                ):

                    st.session_state.evaluation_report = (
                        evaluate_resume(
                            resume_text,
                            job_description
                        )
                    )
                timestamp = datetime.now().strftime(
                    "%Y%m%d_%H%M%S"
                )

                filename = (
                    f"versions/evaluation_{timestamp}.txt"
                )

                with open(filename, "w") as f:
                    f.write(
                        st.session_state.evaluation_report
                    )

        if st.session_state.evaluation_report:

            st.text_area(
                "Evaluation Report",
                st.session_state.evaluation_report,
                height=500
            )

            st.download_button(
                label="Download Evaluation",
                data=st.session_state.evaluation_report,
                file_name="evaluation_report.txt",
                mime="text/plain"
            )

            pdf_file = create_pdf(
                    evaluation_report,
                    "evaluation_report.pdf"
                )

            with open(pdf_file, "rb") as f:

                st.download_button(
                    label="Download Evaluation Report PDF",
                    data=f,
                    file_name="evaluation_report.pdf",
                    mime="application/pdf"
                )
    #Evaluation code ends here
    with tab7:
        st.subheader("📂 Saved Versions")

        files = sorted(
            os.listdir("versions"),
            reverse=True
        )

        if files:
            selected_file = st.selectbox(
                "Select Version",
                files
            )

            filepath = os.path.join(
                "versions",
                selected_file
            )

            with open(filepath, "r") as f:
                content = f.read()

            st.text_area(
                "Version Content",
                content,
                height=500
            )

        else:
            st.info(
                "No saved versions found."
            )