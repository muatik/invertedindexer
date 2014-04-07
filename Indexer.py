import Tokenizer
import Normalizer
import shelve, pickle

class Indexer(object):
    """docstring for Indexer"""
    data = {}
    def __init__(self):
        super(Indexer, self).__init__()
        self.tokenizer = Tokenizer.Tokenizer()
        self.normalizer = Normalizer.Normalizer()
    
    def loadFromFile(self, docId, filename):
        f = file(filename)
        self.process(docId, f.read())

    def process(self, docId, text):
        terms = self.tokenizer.tokenize(text.decode('utf-8'))
        Normalizer.Normalizer.dictionary = dict({i : 0 for i in terms})
        terms = {self.normalizer.normalize(i) : docId for i in terms}
        self.insertData(terms)

    def insertData(self, terms):
        for i, docId in terms.items():
            try:
                postings = self.data[i]
            except:
                postings = []
                self.data[i] = postings

            postings.append(docId)



