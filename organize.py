#This code read a json dataset and sort all the json objects to the respect
#year file
#must be run with a python version less thatn 3.0

import json

def parse(path):
    o = open(path, 'r')
    j= o.readlines()
    elements = 0
    for line in j:
        jsonObject = json.loads(line)
        date = jsonObject['reviewTime']
        write = open('years/'+date[-4:]+'.json','a')
        write.write(json.dumps(jsonObject)+',\n')
        write.close()
    o.close()

def starting(year):
    file = open('years/'+str(year)+'.json','w')
    file.write('[')
    file.close()

def ending(year):
    file = file = open('years/'+str(year)+'.json','a+')
    file.seek(-1,2)
    char = file.read()

    if char == '[':
        file.seek(-1,2)
        file.truncate()
        file.write('')
    else:
        file.seek(-2,2)
        file.truncate()
        file.write(']')
#
for year in range(1996,2015):
    starting(year)
parse('reviews_Beauty_5.json')

for year in range(1996,2015):
    ending(year)
print('end of the program')
