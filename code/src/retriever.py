from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

with open("../data/corpus.txt", "r") as f:
    corpus = f.readlines()

vectorizer = TfidfVectorizer(stop_words='english')
doc_vectors = vectorizer.fit_transform(corpus)


def retrieve(query):
    q_vec = vectorizer.transform([query])
    sims = cosine_similarity(q_vec, doc_vectors)[0]
    
    idx = sims.argmax()
    score = sims[idx]
    
    return corpus[idx], score