# needs to do some installation
# pip install vaderSentiment
# pip install requests

import pandas as pd
import gzip
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

def return_sentiment_scores(sentence):
  snt = analyser.polarity_scores(sentence)
  return str(snt)

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


# end with declaring functions #

df = getDF('reviews_Books_5.json.gz')
df.dropna(subset=["summary", "reviewText"])
df["sentimentScores"] = df.summary.apply(return_sentiment_scores)