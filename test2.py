from gensim import corpora, models, similarities, downloader, models
import csv
from gensim.models import Word2Vec

file = open("word2vec-google-news-300-details.csv", 'r')
read_data = file.read()
correct_count = read_data.lower().count("correct")
wrong_count = read_data.lower().count("wrong")
accuracy = (correct_count/(correct_count+wrong_count))
