import os
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class AdvancedRAG:
    def __init__(self):
        self.docs = []
        self.vectorizer = TfidfVectorizer()
        self.vectors = None

    def load_documents(self, folder="data"):
        texts = []

        for file in os.listdir(folder):
            if file.endswith(".pdf"):
                filepath = os.path.join(folder, file)
                if os.path.getsize(filepath) > 0:
                    try:
                        reader = PdfReader(filepath)
                        for page in reader.pages:
                            text = page.extract_text()
                            if text:
                                texts.append(text)
                    except Exception:
                        pass # Ignore corrupted PDFs

        self.docs = texts

        if texts:
            self.vectors = self.vectorizer.fit_transform(self.docs)

    def query(self, question):
        if not self.docs or self.vectors is None:
            return ""

        q_vec = self.vectorizer.transform([question])
        sim = cosine_similarity(q_vec, self.vectors)

        idx = sim.argmax()
        return self.docs[idx]