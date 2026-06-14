import json
import os
import math

class BM25Okapi:
    def __init__(self, corpus):
        self.corpus_size = len(corpus)
        if self.corpus_size == 0:
            self.avgdl = 0
        else:
            self.avgdl = sum(float(len(x)) for x in corpus) / self.corpus_size
        self.corpus = corpus
        self.f = []
        self.df = {}
        self.idf = {}
        self.k1 = 1.5
        self.b = 0.75
        if self.corpus_size > 0:
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
        if self.corpus_size == 0:
            return []
        scores = [self.get_score(query, index) for index in range(self.corpus_size)]
        return scores

def load_knowledge(domain):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    knowledge_dir = os.path.join(base_dir, "knowledge")
    
    if domain == "all":
        all_data = []
        if os.path.exists(knowledge_dir):
            for file in os.listdir(knowledge_dir):
                if file.endswith(".json"):
                    with open(os.path.join(knowledge_dir, file), "r", encoding="utf-8") as f:
                        data = json.load(f)
                        # Normalize to list
                        if isinstance(data, dict) and "scale" in data:
                            all_data.extend(data["scale"])
                        elif isinstance(data, list):
                            all_data.extend(data)
                        elif isinstance(data, dict):
                            all_data.append(data)
        return all_data

    knowledge_path = os.path.join(knowledge_dir, f"{domain}.json")
    if os.path.exists(knowledge_path):
        with open(knowledge_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Normalize spacing_systems dict to list
            if isinstance(data, dict) and "scale" in data:
                return data["scale"]
            elif isinstance(data, dict):
                return [data]
            return data
            
    industries_path = os.path.join(base_dir, "industries")
    if os.path.exists(industries_path):
        if domain == "industries_all":
            all_data = []
            for file in os.listdir(industries_path):
                if file.endswith(".json"):
                    with open(os.path.join(industries_path, file), "r", encoding="utf-8") as f:
                        all_data.append(json.load(f))
            return all_data
            
    return []

def extract_text(item):
    """Recursively extract all string values from a JSON object to build the search corpus."""
    if isinstance(item, str):
        return item
    elif isinstance(item, dict):
        return " ".join(extract_text(v) for v in item.values())
    elif isinstance(item, list):
        return " ".join(extract_text(v) for v in item)
    return str(item)

def search(query, domain="all"):
    data = load_knowledge(domain)
    if not data:
        return []
        
    corpus = [extract_text(item) for item in data]
    
    bm25 = BM25Okapi([doc.lower().split() for doc in corpus])
    scores = bm25.get_scores(query.lower().split())
    
    if not scores:
        return []
        
    top = sorted(zip(scores, data), reverse=True, key=lambda x: x[0])[:5]
    return [item for score, item in top if score > 0]

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python search.py <query> [domain]")
        sys.exit(1)
        
    q = sys.argv[1]
    domain = sys.argv[2] if len(sys.argv) > 2 else "all"
    
    results = search(q, domain)
    print(json.dumps(results, indent=2))
