import pandas as pd
from SentimentAnalysis_Vader import * 
from import_as_pandas import getDF
from split_helpful import *
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('filename', type=str, help="filename for Amazon data")


#reviewText,asin,overall,unixReviewTime,helpful,reviewerID,negative,neutral,positive,compound
def make_csv(filename):
  df = getDF(filename)
  df_with_sentiment = df[['reviewText', 'asin', 'overall', 'unixReviewTime', 'helpful', 'reviewerID']]
  df_with_sentiment = add_sentiment_column(df_with_sentiment)
  df_with_sentiment = df_with_sentiment[['asin', 'overall', 'unixReviewTime', 'helpful', 'negative', 'neutral', 'positive']]
  df_with_sentiment.to_csv('/work/cse496dl/bgeren/' + 'data_with_sentiment.csv', index=False)
  df_with_sentiment = split_helpful(df_with_sentiment)
  df_with_sentiment.to_csv('/work/cse496dl/bgeren/' + 'data_with_sentiment.csv', index=False)
  return df_with_sentiment

args = parser.parse_args()

make_csv(args.filename)
