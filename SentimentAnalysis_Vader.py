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

def add_sentiment_column(df):
  df.dropna(subset=["reviewText"])
  df['negative'], df['neutral'], df['positive'], df['compound'] = zip(*df['reviewText'].map(return_sentiment_scores))
  return df

