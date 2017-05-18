from random import randint
import io
source = open('source.txt').read().split()
def main(source, number=100, intropoint='to sherlock'):
	file = io.open('output.txt', 'w')
	story = intropoint
	source_dict = {}
	for i in range(len(source)):
		parse_words(source, i, source_dict)
	while number > 0:
		story += ' ' + choose_words(story, source_dict)


		number-=1
	file.write(story)
	file.close()
def parse_words(source, i, source_dict):
	if len(source) - i > 2:
		if '{0} {1}'.format(source[i].lower(), source[i+1].lower()) in source_dict.keys(): 
			source_dict['{0} {1}'.format(source[i].lower(), source[i+1].lower())].append('{0}'.format(source[i+2].lower()))
		else:
			source_dict['{0} {1}'.format(source[i].lower(), source[i+1].lower())] = ['{0}'.format(source[i+2].lower())]

def choose_words(story, source_dict):
	temp = story.split()[-2:]
	last_two = ' '.join(temp)
	if len(source_dict[last_two]) > 1:
		choice = source_dict[last_two][randint(0, len(source_dict[last_two])-1)]
	else:
		choice = source_dict[last_two][0]
	return choice

if __name__ == '__main__':
	import sys
	if len(sys.argv) > 1: 
		num_words = int(sys.argv[1])
		main(source, num_words)
	else:
		main(source)
