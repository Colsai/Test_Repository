class personal_greeting:

	def __init__(self, name):
		self.name = name
	
	def say_hi(self):
		print(f"Hello, my name is {self}")
        
	def say_bye(self):
		print(f"Goodbye {self}! Have a nice day!")   
        
	def say_what(self):
		print(f"Hey {self}, what did you say?")   

p = person("Scott")

p.say_hi
p.say_what
p.say_bye