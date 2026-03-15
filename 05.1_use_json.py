import json
d = {
    "name": "hugo",
    "age": 22,
    "gender": "male",
}#一个是json对象

s = json.dumps(d, ensure_ascii=False)#后面这个防止中文乱码
print(s)
#python字典转json字符串

print(s)

l = [
    {"name": "hugo",
    "age": 22,
    "gender": "male"
     },
    {"name": "antoni",
    "age": 23,
    "gender": "male"
     },
    {"name": "niki",
    "age": 20,
    "gender": "male"
     }
]

s2=json.dumps(l, ensure_ascii=False)
print(s2)
#两个是json数组