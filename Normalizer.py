class Normalizer(object):
	"""Normalizes text"""
	dictionary = {}
	lowered = True
	stemmed = True

	def __init__(self):
		super(Normalizer, self).__init__()
	
	def normalize(self, word):
		if self.lowered:
			word = word.lower()
		if self.stemmed:
			word = self.stem(word)

		return word

	@classmethod
	def stem(cls, word):
		
		"""we only consider the last two letters as a suffix""" 
		
		affix1 = word[-1:]
		root1 = word[:-1]

		affix2 = word[-2:]
		root2 = word[:-2]
		
		affix3 = word[-2:]
		root3 = word[:-3]
		
		if affix2 == 'ed' and cls.lookup(root2):
			return root2
		elif affix1 == 's' and cls.lookup(root1):
			return root1
		elif affix2 == 'es' and cls.lookup(root2):
			return root2
		elif affix3 == 'ing' and cls.lookup(root3):
			return root3
		
		# otherwise we regard the word itself a root word
		return word

	@classmethod
	def lookup(cls, word):
		if word in cls.dictionary:
			return True
		return False


