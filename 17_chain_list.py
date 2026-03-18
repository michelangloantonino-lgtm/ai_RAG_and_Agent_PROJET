from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import OllamaLLM#接入模型
from langchain_core.runnables.base import Runnable
from openai import models

#第一步先构建模版

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一个诗人，会写诗"),
        MessagesPlaceholder("history"), #历史消息后续动态注入
        ("human","请为我们吟诗一首"),
    ]
)
#第二部，写出相对应的history的数据，动态，可更改
history_data = [
    ("human", "你来写一首后现代主义诗歌"),
    ("ai", "我是一朵穿裤子的云，无形于天地"),
    ("human", "你来写一首模仿辛波斯卡的诗歌"),
    ("ai", "死不是生的对立面")
]

model = OllamaLLM(model = "qwen3:4b")

#在这里就直接组成一个链，每一个都是runnable的子类
chain = chat_prompt_template | model

#再通过链去调用invoke/stram

#res = chain.invoke({"history": history_data})
#print(res)

#流式输出
for chunk in chain.stream({ "history": history_data}):
    print(chunk, end="", flush=True)
