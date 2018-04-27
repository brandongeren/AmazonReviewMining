
import pandas as pd
import json

#return a dictionary containt all the json objects
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
    return pd.DataFrame.from_dict(df,orient = 'index')
