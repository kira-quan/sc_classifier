"""
A Naive Bayes classifier using a multinomial distribution for the Sandy data set. 
The features are the words in the tweet text, the score is for the different sentiment
categories.
"""

from nltk.classify import NaiveBayesClassifier
from nltk.classify import accuracy
from nltk.corpus import stopwords
import sys
import json

twitter_stopwords = ['u', 'ur', '<user', '<url>']
english_stopwords = stopwords.words('english')


def word_features(text):
	# Create a feature set
	words = text.split()
	return dict([(word.lower(), True) for word in words if word.lower() not in english_stopwords or word.lower() not in twitter_stopwords])

def run_classifier(training_filename, input_filename, output_filename):
	# Create output file
	outfile = open(output_filename, 'w')

	# Open and read the training data
	training_data = []
	test_data = []

	with open(training_filename, 'r') as infile:
		for line in infile:
			tweet_json = json.loads(line)
			training_data.append((word_features(tweet_json['text']), tweet_json['sentiment']))

		infile.close()

	# Create classifier
	nb_classifier = NaiveBayesClassifier.train(training_data)

	nb_classifier.show_most_informative_features()

	with open(input_filename, 'r') as infile:
		for line in infile:
			tweet_json = json.loads(line)
			classify_info = word_features(tweet_json['text'])
			classification = nb_classifier.classify(classify_info)
			tweet_json.update({'sentiment' : classification})
			json.dump(tweet_json, outfile)
			outfile.write('\n')


	#print accuracy(nb_classifier, training_data)
	#print nb_classifier.classify(test_data)
	#print nb_classifier.classify(test_data_2)
	#print nb_classifier.labels()

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
	output_filename = arguments[3]
	run_classifier(training_filename, input_filename, output_filename)