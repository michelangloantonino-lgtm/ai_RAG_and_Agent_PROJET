
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

model = ChatOllama(model="qwen3:4b")

messages = [
    ("system", "你是一个导演"),
    ("human", "评价贾樟柯"),
    ("ai", "中国第六代代表人物"),
    ("human", "按照上个例子作答")
]

res = model.stream(input=messages)

for chunk in res:
    print(chunk.content , end="", flush=True)