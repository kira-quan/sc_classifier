"""
A Naive Bayes classifier using a multinomial distribution for the Sandy data set. 
The features are the words in the tweet text, the score is for the different sentiment
categories.
"""

from nltk.classify import NaiveBayesClassifier
from nltk.classify import accuracy
import sys
import json


def word_features(text):
	# Create a feature set
	words = text.split()
	return dict([(word, True) for word in words])

def run_classifier(training_filename, input_filename):
	#output_filename = input_filename += "_results"

	# Open and read the training data
	training_data = []
	test_data = []

	with open(training_filename, 'r') as infile:
		for line in infile:
			tweet_json = json.loads(line)
			training_data.append((word_features(tweet_json['text']), tweet_json['classification']))

		infile.close()

	test_data = word_features("<user> Whatssgood man how u been!")
	# Create classifier
	nb_classifier = NaiveBayesClassifier.train(training_data)

	nb_classifier.show_most_informative_features()

	print accuracy(nb_classifier, training_data)
	print nb_classifier.classify(test_data)

	# Fit to the training data
	# TODO: Look into if it needs to be fit to the training ata
	# mnb_classifier.fit()

	# Classify the input
	# mnb_predict()


if __name__ == '__main__':

	# Get arguments
	arguments = sys.argv
	arguments_len = len(arguments)

	# Data set name 
	training_filename = arguments[1]
	input_filename = arguments[2]
	run_classifier(training_filename, input_filename)