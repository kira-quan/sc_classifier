"""
A filter file for the Sandy dataset

Currently:
- Removes RT, MT
- Removes tweets that do not have a specific set of hashtags. 
- Replaces user mentions and urls in tweet text
- Condenses JSON to the following fields: id, coordinates, created_at, user.id, user.screen_name, text
"""

import json
import re
import sys

def process_tweet(input_tweet):
	tweet_json = json.loads(input_tweet)
	
	# Create a smaller JSON object with desired fields
	return tweet_json

def process_file(input_filename):
	"""
	Process the file one input at a time and write the given output file
	"""
	
	#Split the outfile into n parts...
	outfile1 = open("sandy_final_Oct_24.json", 'w')
	outfile2 = open("sandy_final_Oct_25.json", 'w')
	outfile3 = open("sandy_final_Oct_26.json", 'w')
	outfile4 = open("sandy_final_Oct_27.json", 'w')
	outfile5 = open("sandy_final_Oct_28.json", 'w')
	outfile6 = open("sandy_final_Oct_29.json", 'w')
	outfile7 = open("sandy_final_Oct_30.json", 'w')
	outfile8 = open("sandy_final_Oct_31.json", 'w')

	# Process one line of the file
	with open(input_filename, 'r') as infile:
		
		for line in infile:
			tweet_output = process_tweet(line)
			if tweet_output is not None:
				
				
				# Conditions for splitting
				if ("Oct 24" in tweet_output['created_at']):
					json.dump(tweet_output, outfile1)
					outfile1.write('\n')
				if ("Oct 25" in tweet_output['created_at']):
					json.dump(tweet_output, outfile2)
					outfile2.write('\n')
				if ("Oct 26" in tweet_output['created_at']):
					json.dump(tweet_output, outfile3)
					outfile3.write('\n')
				if ("Oct 27" in tweet_output['created_at']):
					json.dump(tweet_output, outfile4)
					outfile4.write('\n')
				if ("Oct 28" in tweet_output['created_at']):
					json.dump(tweet_output, outfile5)
					outfile5.write('\n')
				if ("Oct 29" in tweet_output['created_at']):
					json.dump(tweet_output, outfile6)
					outfile6.write('\n')
				if ("Oct 30" in tweet_output['created_at']):
					json.dump(tweet_output, outfile7)
					outfile7.write('\n')
				if ("Oct 31" in tweet_output['created_at']):
					json.dump(tweet_output, outfile8)
					outfile8.write('\n')

		infile.close()

	outfile1.close()
	outfile2.close()
	outfile3.close()
	outfile4.close()
	outfile5.close()
	outfile6.close()
	outfile7.close()
	outfile8.close()

if __name__ == '__main__':

	# Get arguments
	arguments = sys.argv
	arguments_len = len(arguments)

	# Data set name 
	input_filename = arguments[1]
	process_file(input_filename)
