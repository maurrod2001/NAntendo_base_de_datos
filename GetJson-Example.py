import json

# f = open('example.json', 'r')
# c =f.read()
# print(c)
# data = json.loads(c)
with open('example.json') as f:
  data = json.load(f)

print(data["all"])

for el in data["all"]:
  print(el["saludo"])