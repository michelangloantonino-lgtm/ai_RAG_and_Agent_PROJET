from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import OllamaLLM#接入模型
from openai import models

#第一步先构建模版

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一个诗人，会写诗"),
        MessagesPlaceholder("history"), #历史消息后续动态注入
        ("human","请为我们吟诗一首")
    ]
)
#第二部，写出相对应的history的数据，动态，可更改
history_data = [
    ("human", "你来写一首后现代主义诗歌"),
    ("ai", "我是一朵穿裤子的云，无形于天地"),
    ("human", "你来写一首模仿辛波斯卡的诗歌"),
    ("ai", "死不是生的对立面"),
]

#第三步，把数据注入到模版中去，就完成了prompt的创造
prompt_text = chat_prompt_template.invoke({"history": history_data}).to_string()#注入之后，获得完整提示词
print(prompt_text)
#第四部接入模型
model = OllamaLLM(model="qwen3:4b")
#第五步，获得了结果
res = model.invoke(prompt_text)
print(res)



