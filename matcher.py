from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(resume_texts, job_description):
    documents = resume_texts + [job_description]
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(documents)

    job_vec = tfidf_matrix[-1]
    resume_vecs = tfidf_matrix[:-1]

    similarity_scores = cosine_similarity(resume_vecs, job_vec).flatten()
    return similarity_scores
