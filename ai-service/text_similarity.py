from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_text_similarity(resume_text, job_description):

    # Handle empty input
    if not resume_text.strip() or not job_description.strip():
        similarity_percentage = 0.0

    else:
        # Store both documents
        documents = [
            resume_text,
            job_description
        ]

        # Convert text into TF-IDF vectors
        vectorizer = TfidfVectorizer()

        tfidf_matrix = vectorizer.fit_transform(documents)

        # Calculate cosine similarity
        similarity = cosine_similarity(
            tfidf_matrix[0:1],
            tfidf_matrix[1:2]
        )[0][0]

        # Convert into percentage
        similarity_percentage = round(similarity * 100, 2)

    # Assign similarity category
    if similarity_percentage >= 80:
        category = "Highly Similar"

    elif similarity_percentage >= 60:
        category = "Moderately Similar"

    elif similarity_percentage >= 40:
        category = "Somewhat Similar"

    else:
        category = "Low Similarity"

    return {
        "similarity_percentage": similarity_percentage,
        "category": category
    }