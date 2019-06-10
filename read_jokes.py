import sys
import random

def tell_jokes(input):
	if input == '笑話':
		all_lines = []
		with open('joke.txt') as f:
			for line in f:
				all_lines.append(line)
		#print(len(all_lines))
		joke_list = range(len(all_lines))
		joke_idx = random.choice(joke_list)
		joke = all_lines.pop(joke_idx)
		joke = joke[:len(joke)-1]
		return joke
	else:
		pass

		

if __name__ == '__main__':
	joke = tell_jokes('笑話')
	print(joke)