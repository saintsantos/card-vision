import json

json_data=open('AllCards.json')
data = json.load(json_data)

#pprint(data)

print (data['Mountain'])
#print(card['name'])
#print (data['Necropede'])
#outfile = open("foo.txt", "w")
#print(data.keys())


json_data.close()
# outfile.close()
# with open('AllCards.json', 'r') as CardObjects:
#     cardDict = json.load(CardObjects)
#     for key in cardDict:
#         #print(key + ' ' + value)
#         print (key)
