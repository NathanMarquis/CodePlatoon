# Don't forget to run the tests (and create some of your own)
import functools

def anagrams_for(word, list_of_words):
	sortedWord = sorted(list(word.upper()))
	sortedWord = filter((lambda a: a != ' '), sortedWord)
	print(sortedWord)

print(anagrams_for('yes', ['sey', 'no', 'yes', 'seyyes']))