
import json
import gzip


def parse(path):
    o = open(path, 'r')
    j= o.readlines()
    for line in j:
        jsonObject = json.loads(line)
        print(jsonObject['reviewText'])
        print('--------------')
    o.close()

#here goes the variable to use the api
parse('reviews_Musical_Instruments_5.json')
