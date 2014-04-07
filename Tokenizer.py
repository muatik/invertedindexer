import sys

class Tokenizer(object):
	separator = ' '
	def tokenize(self,text):
		return text.split(self.separator)

if __name__ == '__main__':
	if len(sys.argv) > 1 :
		t = Tokenizer()
		print t.tokenize('this is an example')