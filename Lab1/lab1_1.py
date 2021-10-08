import nltk
from nltk.corpus import twitter_samples, stopwords, movie_reviews
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer
import matplotlib.pyplot as plt
import random
import re
import string

nltk.download('movie_reviews', download_dir='C:/Users/HP/Documents/Sem7/ML/Lab1')

movie_reviews.words()
# all_positive_tweets = twitter_samples.strings('positive_tweets.json')
# all_negative_tweets = twitter_samples.strings('negative_tweets.json')

# print("Number of positive tweets : " , len(all_positive_tweets))
# print("Number of negative tweets : ", len(all_negative_tweets))

# print("\nThe type of all positive tweets : ", type(all_positive_tweets))
# print("The type of a tweet entry is : ", type(all_negative_tweets[0]))

# # fig = plt.figure(figsize=(5, 5))
# # labels = 'Ml-BSB-lec', 'Ml-HAP-lec', 'Ml-HAP-lab'

# # sizes = [40, 35, 25]
# # plt.pie(sizes, labels=labels, autopct='%.2f%%', shadow=True, startangle=90)
# # plt.axis('equal')
# # plt.show()

# # print("\033[92m", all_positive_tweets[random.randint(0, 5000)])
# # print("\033[91m", all_negative_tweets[random.randint(0, 5000)])
# print("\n")

# tweet = all_positive_tweets[2277]
# # print("\n", tweet)

# # nltk.download('stopwords', download_dir='C:/Users/Hp/Downloads')

# # print('\033[92m' + tweet)
# # print('\033[94m')

# tweet2 = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)
# tweet2 = re.sub(r'#', '', tweet2)
# # print("hello", tweet2)

# print()
# # print('\033[92m', tweet2)
# # print('\033[94m')

# tokenizer = TweetTokenizer(preserve_case=False)
# tweet_tokens = tokenizer.tokenize(tweet2)
# print()
# # print('Tokenized strings : ')
# # print(tweet_tokens)

# stopwords_eng = stopwords.words('english')
# print('Stop Words\n')
# print(stopwords_eng)

# # print('\033[92m')
# # print(tweet_tokens)
# # print('\033[94m')

# tweet_cleans = []
# for word in tweet_tokens:
#     if(word not in stopwords_eng and word not in string.punctuation):
#         tweet_cleans.append(word)

# # print('removed stop words and punctuations  : \n', tweet_cleans )

# print('\033[92m')
# print(tweet_cleans)
# print('\033[94m')

# stemmer = PorterStemmer()
# tweets_stem = []

# for word in tweet_cleans:
#     stem_word = stemmer.stem(word)
#     tweets_stem.append(stem_word)

# print('stemmed words : \n', tweets_stem)