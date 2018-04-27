import pandas as pd
import gzip

def split_helpful(data):
  data['helpful']=data['helpful'].str.replace('[','')
  data['helpful']=data['helpful'].str.replace(']','')
  data['helpful']=data['helpful'].str.replace(',','')
  data[['helped','totalhelp']] = data.helpful.str.split(' ',expand=True)
  del data['helpful']	
  return data
