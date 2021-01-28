import json

with open('input') as f:
    j = json.load(f)


num = 0

def traverse(obj):
    global num
    if isinstance(obj, int):
        num += obj
    elif isinstance(obj, list):
        for v in obj:
            traverse(v)
    elif isinstance(obj, dict):
        s = any(v == "red" for v in obj.values())
        if not s:
            for v in obj.values():
                traverse(v)


traverse(j)
print(num)
