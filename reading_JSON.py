
import json
import gzip


def parse(path):
    o = open(path, 'r')
    j= o.readlines()
    for line in j:
        jsonObject = json.loads(line)
        return (jsonObject['reviewText'])
    o.close()

#here goes the variable to use the api
parse('Books_5.json')
