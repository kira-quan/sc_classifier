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
import csv

def process_tweet(input_tweet):
	tweet_json = json.loads(input_tweet)
	
	# Create a smaller JSON object with desired fields
	return tweet_json

def process_file(input_filename):
	"""
	Process the file one input at a time and write the given output file
	"""
	
	#Split the outfile into n parts...
	outfile1 = csv.writer(open("sandy_geo_Oct_24.csv", 'w'))
	outfile2 = csv.writer(open("sandy_geo_Oct_25.csv", 'w'))
	outfile3 = csv.writer(open("sandy_geo_Oct_26.csv", 'w'))
	outfile4 = csv.writer(open("sandy_geo_Oct_27.csv", 'w'))
	outfile5 = csv.writer(open("sandy_geo_Oct_28.csv", 'w'))
	outfile6 = csv.writer(open("sandy_geo_Oct_29.csv", 'w'))
	outfile7 = csv.writer(open("sandy_geo_Oct_30.csv", 'w'))
	outfile8 = csv.writer(open("sandy_geo_Oct_31.csv", 'w'))


	outfile1.writerow(["Lon", "Lat", "Date", "User", "Text", "Sentiment"])
	outfile2.writerow(["Lon", "Lat", "Date", "User", "Text", "Sentiment"])
	outfile3.writerow(["Lon", "Lat", "Date", "User", "Text", "Sentiment"])
	outfile4.writerow(["Lon", "Lat", "Date", "User", "Text", "Sentiment"])
	outfile5.writerow(["Lon", "Lat", "Date", "User", "Text", "Sentiment"])
	outfile6.writerow(["Lon", "Lat", "Date", "User", "Text", "Sentiment"])
	outfile7.writerow(["Lon", "Lat", "Date", "User", "Text", "Sentiment"])
	outfile8.writerow(["Lon", "Lat", "Date", "User", "Text", "Sentiment"])
	
	
	# Process one line of the file
	with open(input_filename, 'r') as infile:
		
		for line in infile:
			tweet_output = process_tweet(line)
			if (tweet_output is not None) and (tweet_output['coordinates'] is not None):
				
				
				if ((tweet_output['coordinates'][0]>=-78) and (tweet_output['coordinates'][0]<=-68)
					and (tweet_output['coordinates'][1] >=35) and (tweet_output['coordinates'][1]<=45)):
						
						
					print(tweet_output['coordinates'])
						
					# Conditions for splitting
					if ("Oct 24" in tweet_output['created_at']):
						outfile1.writerow([tweet_output['coordinates'][0],tweet_output['coordinates'][1],
						tweet_output["created_at"], tweet_output['user']['screen_name'], tweet_output['text'].encode('ascii', 'ignore'), tweet_output['sentiment']])
					if ("Oct 25" in tweet_output['created_at']):
						outfile2.writerow([tweet_output['coordinates'][0],tweet_output['coordinates'][1],
						tweet_output["created_at"], tweet_output['user']['screen_name'], tweet_output['text'].encode('ascii', 'ignore'), tweet_output['sentiment']])
					if ("Oct 26" in tweet_output['created_at']):
						outfile3.writerow([tweet_output['coordinates'][0],tweet_output['coordinates'][1],
						tweet_output["created_at"], tweet_output['user']['screen_name'], tweet_output['text'].encode('ascii', 'ignore'), tweet_output['sentiment']])
					if ("Oct 27" in tweet_output['created_at']):
						outfile4.writerow([tweet_output['coordinates'][0],tweet_output['coordinates'][1],
						tweet_output["created_at"], tweet_output['user']['screen_name'], tweet_output['text'].encode('ascii', 'ignore'), tweet_output['sentiment']])
					if ("Oct 28" in tweet_output['created_at']):
						outfile5.writerow([tweet_output['coordinates'][0],tweet_output['coordinates'][1],
						tweet_output["created_at"], tweet_output['user']['screen_name'], tweet_output['text'].encode('ascii', 'ignore'), tweet_output['sentiment']])
					if ("Oct 29" in tweet_output['created_at']):
						outfile6.writerow([tweet_output['coordinates'][0],tweet_output['coordinates'][1],
						tweet_output["created_at"], tweet_output['user']['screen_name'], tweet_output['text'].encode('ascii', 'ignore'), tweet_output['sentiment']])
					if ("Oct 30" in tweet_output['created_at']):
						outfile7.writerow([tweet_output['coordinates'][0],tweet_output['coordinates'][1],
						tweet_output["created_at"], tweet_output['user']['screen_name'], tweet_output['text'].encode('ascii', 'ignore'), tweet_output['sentiment']])
					if ("Oct 31" in tweet_output['created_at']):
						outfile8.writerow([tweet_output['coordinates'][0],tweet_output['coordinates'][1],
						tweet_output["created_at"], tweet_output['user']['screen_name'], tweet_output['text'].encode('ascii', 'ignore'), tweet_output['sentiment']])

		infile.close()


if __name__ == '__main__':

	# Get arguments
	arguments = sys.argv
	arguments_len = len(arguments)

	# Data set name 
	input_filename = arguments[1]
	process_file(input_filename)
