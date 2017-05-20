import pytest

PARAMS_TABLE_NORMAL = [
	('my way', 'led'),
	('in a', 'dark')
]

PARAMS_TABLE_DOUBLE = [
	('as i', 'passed', 'looked'),
	('and was', 'hot', 'shown')
]

PARAMS_TABLE_KEYS = [
	(4, {'the twentieth':['of']}),
	(2, {'was on':['the']})
]
'''This tests the keys function'''
@pytest.mark.parametrize('n, result', PARAMS_TABLE_KEYS)
def test_keys(n, result):
	source = open('source.txt').read().split()
	test_dict = {}
	from trigrams import parse_words
	parse_words(source, n, test_dict)
	assert test_dict == result

'''This tests the words fucntion'''
@pytest.mark.parametrize('n, result', PARAMS_TABLE_NORMAL)
def test_words(n, result):
	source = open('source.txt').read().split()
	from trigrams import parse_words, choose_words
	source_dict = {}
	for i in range(0, len(source)):
		parse_words(source, i, source_dict)
	assert choose_words(n, source_dict) == result
	
'''This tests the double words function'''
@pytest.mark.parametrize('n, resultone, resulttwo', PARAMS_TABLE_DOUBLE)
def test_words_double(n, resultone, resulttwo):
	source = open('source.txt').read().split()
	from trigrams import parse_words, choose_words
	source_dict = {}
	for i in range(0, len(source)):
		parse_words(source, i, source_dict)
	choice = choose_words(n, source_dict)
	assert choice == resultone or choice == resulttwo