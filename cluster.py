
import pandas as pd
import json

def getDF(path):
    i= 0
    df= {}
#    for d in parse(path):
#        df[i]= d
#        i += i

def jsonToPanda(path):
    file = open(path, 'r')
    r = file.readlines()
    times = 0
    df = {}
    for line in r:
        if times == 0:
            line = line[1:-2]
        else:
            line = line[:-1]
        last = line[-1:]
        if last == ',':
            line = line[:-1]
        df[times] = json.loads(line)
        times = times +1
    return df

values =(jsonToPanda('years/2005.json'))
#products is a panda 
product = pd.DataFrame.from_dict(values,orient = 'index')
print(product.head())
