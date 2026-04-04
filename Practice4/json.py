import json

# Convert JSON string to Python

x = '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)

print(y["name"])


# Convert Python to JSON

mydict = {
  "name": "Anna",
  "age": 25,
  "city": "London"
}

z = json.dumps(mydict)

print(z)


# Write JSON to file

with open("data.json", "w") as file:
    json.dump(mydict, file)


# Read JSON from file

with open("data.json", "r") as file:
    data = json.load(file)
    print(data)