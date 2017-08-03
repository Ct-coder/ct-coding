class student(object):
	def __init__(self,name,score):
		self.name=name
		self.score=score

	def print_score(self):
		print('%s:%s' % (self.name,self.score))

bart=student('bart',59)
lisa=student('lisa',87)
bart.print_score()
lisa.print_score()
bart.sss=30
print(bart.sss)