import nltk

def remove_stopwords(text):
  words = text.split(" ")
  filtered_words = [word for word in words if word not in set(nltk.corpus.stopwords.words('english'))]
  filtered_text = " ".join(filtered_words)
  return filtered_text
