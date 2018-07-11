"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    return open(file_path).read()



def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here

    words = text_string.split()

    for i in range(len(words) - 2):
    	if tuple([words[i], words[i + 1]]) in chains:
    		# by indexing into the key of the list we get the value which is a list, then we can append to that list
    		chains[tuple([words[i], words[i + 1]])].append(words[i +2])
    	else:
    		chains[tuple([words[i], words[i + 1]])] = [words[i + 2]]

    return chains


def make_text(chains):
	"""Return text from chains."""

	words = []

	random_key = choice(list(chains.keys()))
	random_value = choice(chains[random_key])
	words.extend([random_key[0],random_key[1], random_value])

	while True:
		new_key = tuple((words[-2], words[-1]))

		if new_key in chains:
			new_value = choice(chains[new_key])
			words.append(new_value)
		else:
			break

	return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
