# needs to do some installation
# pip install vaderSentiment
# pip install requests

import pandas as pd
import gzip
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def return_sentiment_scores(sentence):
  analyser = SentimentIntensityAnalyzer()
  sentiment = analyser.polarity_scores(sentence)
  negative = sentiment['neg']
  neutral = sentiment['neu']
  positive = sentiment['pos']
  compound = sentiment['compound']
  return negative, neutral, positive, compound

def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield eval(l)

def getDF(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')

def add_sentiment_column(df):
  df.dropna(subset=["reviewText"])
  df["sentimentScores"] = df.summary.apply(return_sentiment_scores)


