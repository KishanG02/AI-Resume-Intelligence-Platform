from sklearn.feature_extraction.text import CountVectorizer


def extract_keywords(text):

    vectorizer = CountVectorizer(
        stop_words="english"
    )

    vectorizer.fit([text])

    return list(
        vectorizer.get_feature_names_out()
    )


def calculate_ats_score(
    resume_keywords,
    jd_keywords
):

    matched = set(resume_keywords) & set(jd_keywords)

    if len(jd_keywords) == 0:
        return 0

    score = (
        len(matched) /
        len(jd_keywords)
    ) * 100

    return round(score)