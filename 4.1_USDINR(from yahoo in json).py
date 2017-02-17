import json

with open('(JSON)yahoo INRUSD(2016-01-01to2017-10-02).json') as json_data:
    data=json.load(json_data)
    node=data['query']['results']['quote']
    for d in node:
        print d['Symbol'], d['Date'], d['Open']
