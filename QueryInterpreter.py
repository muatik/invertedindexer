from Indexer import Indexer
class QueryInterpreter(object):
    """docstring for QueryInterpreter"""
    def __init__(self, index):
        super(QueryInterpreter, self).__init__()
        self.index = index
    
    def find(self, keywords):
        postings = [self.index.data[keyword] for keyword in keywords]
        return self.mergePostings(*postings);
        intersect = postings[0][1]
        for i in range(1, len(postings)):
            intersect = self.mergePostings(intersect, postings[i][1])

        print intersect
        return intersect
        

    @staticmethod
    def mergePostings(*postings):
        intersect = []
        
        """
        for i in postings1:
            for k in postings2:
                if i == k:
                    intersect.append(i)
        """

        """
        intersect = set(postings[0]).intersection(*postings)
        """

        

        return intersect


x = Indexer()

lines = file('tweets.txt').read().split('\n')
for r in range(1):
    for i in range(1000):
        x.process(docId = i+r*10000, text = lines[i])
#
#for i in x.data.items():
#    print i

#shelf = shelve.open('dump.txt')
#shelf['indexes'] = x.data

#f = file('dump.txt', 'w')
#for i in x.data.items():
#    f.write(str(i) + '\n')

q = QueryInterpreter(x)
print q.find(["amk","tamam","gelmiyom"])