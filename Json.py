#Json to Python Format
import json
x='{"name":"xyx","age":35}'
z=json.loads(x)
print(z["name"])
print(z["age"])

#Dictionary to Json Format
x={"name":"xyz","age":35}
y=json.dumps(x)
print(y)