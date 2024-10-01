class Vectorizer():
    def _init_(self, vocab):
        self.vocabulary = vocab
        self.stopWords = get_stopwords()
        self.dictionary = dict()
        
    def fit(self):
        for index, word in enumerate(self.vocabulary):
            self.dictionary[word] = index + 1

    def preprocess(self, doc):
        doc = handle_punctuation(doc)
        doc = doc.lower()
        words = doc.split(' ')
        for word in words:
            word.replace('\n', '')
        return words
        
    def fit_transform(self, documents):
        vector = []
        for doc in documents:
            doc = self.preprocess(doc)
            doc_vector = []
            self.fit()
            for word in doc:
                if word not in self.stopWords:
                    doc_vector.append(self.dictionary.get(word, random.randint(len(vectorizer.dictionary), 100000000)))
            vector.append(doc_vector)
        return vector
        
    def similarity(self, doc1, doc2):
        sim = 0
        # write your code
        return sim