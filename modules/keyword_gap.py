def find_keyword_gaps(
    resume_keywords,
    jd_keywords
):

    matched = list(
        set(resume_keywords) &
        set(jd_keywords)
    )

    missing = list(
        set(jd_keywords) -
        set(resume_keywords)
    )

    return matched, missing