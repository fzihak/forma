import json
import os
import math

class BM25Okapi:
    def __init__(self, corpus):
        self.corpus_size = len(corpus)
        self.avgdl = sum(float(len(x)) for x in corpus) / self.corpus_size
        self.corpus = corpus
        self.f = []
        self.df = {}
        self.idf = {}
        self.k1 = 1.5
        self.b = 0.75
        self.initialize()

    def initialize(self):
        for document in self.corpus:
            frequencies = {}
            for word in document:
                if word not in frequencies:
                    frequencies[word] = 0
                frequencies[word] += 1
            self.f.append(frequencies)

            for word, freq in frequencies.items():
                if word not in self.df:
                    self.df[word] = 0
                self.df[word] += 1

        for word, freq in self.df.items():
            self.idf[word] = math.log(self.corpus_size - freq + 0.5) - math.log(freq + 0.5)

    def get_score(self, document, index):
        score = 0
        doc_len = len(self.corpus[index])
        for word in document:
            if word not in self.f[index]:
                continue
            freq = self.f[index][word]
            numerator = self.idf[word] * freq * (self.k1 + 1)
            denominator = freq + self.k1 * (1 - self.b + self.b * doc_len / self.avgdl)
            score += (numerator / denominator)
        return score

    def get_scores(self, query):
        scores = [self.get_score(query, index) for index in range(self.corpus_size)]
        return scores

def load_knowledge(domain):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    knowledge_path = os.path.join(base_dir, "knowledge", f"{domain}.json")
    
    if os.path.exists(knowledge_path):
        with open(knowledge_path, "r", encoding="utf-8") as f:
            return json.load(f)
            
    # Try industries if not found in knowledge
    industries_path = os.path.join(base_dir, "industries")
    if os.path.exists(industries_path):
        # We can either load all industries or a specific one
        if domain == "industries_all":
            all_data = []
            for file in os.listdir(industries_path):
                if file.endswith(".json"):
                    with open(os.path.join(industries_path, file), "r", encoding="utf-8") as f:
                        all_data.append(json.load(f))
            return all_data
            
    return []

def search(query, domain="ui_styles"):
    data = load_knowledge(domain)
    if not data:
        return []
        
    corpus = [
        str(item.get("description", "")) + " " + " ".join(item.get("use_cases", []))
        for item in data
    ]
    
    bm25 = BM25Okapi([doc.lower().split() for doc in corpus])
    scores = bm25.get_scores(query.lower().split())
    
    top = sorted(zip(scores, data), reverse=True, key=lambda x: x[0])[:5]
    return [item for score, item in top if score > 0]

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        q = sys.argv[1]
        results = search(q)
        print(json.dumps(results, indent=2))
