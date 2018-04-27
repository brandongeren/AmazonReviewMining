import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# df is a dataframe of amazon rating 5-core data
# the data is in the format as read in by the code available on the ucsd website
def plot_distribution(df, colname, filename):
	ratings = df[colname].value_counts().sort_index()
	ratings = ratings.to_frame()
	ratings['index'] = ratings.index
	ax = sns.barplot(x="index", y=colname, data=ratings)
	plt.savefig(filename)
