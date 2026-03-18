from click import prompt
from langchain_ollama import OllamaLLM
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from openai import vector_stores

model = OllamaLLM(model="qwen3:4b")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","以我给你提供的资料为基础，简介专业的回答问题，参考资料:{context}。"),
        ("user","用户提问:{input}")
    ]
)#两个变量，有待注入{context}，input



#暂存到内存里去
vector_store = InMemoryVectorStore(embedding=DashScopeEmbeddings(model="text-embedding-v4"))

#准备一下资料（向量库里的数据）
#add_texts 传入一个list[str]

vector_store.add_texts(["减肥就是要少吃多练","减脂期间吃东西很重要，尽量少糖少盐","跑步是很好的运动"])

input_text = "怎么减肥?"


#检索向量库
result = vector_store.similarity_search(input_text,2)#如果能匹配得到，最多返回两个结果

reference_text = "["
for doc in result:
    reference_text += doc.page_content
reference_text += "]" # 再转化为纯文本字符串形式

#print(reference_text)

def print_prompt(prompt):
    print(prompt.to_string())
    print("="*20)
    return prompt


#chain
chain = prompt | print_prompt |model | StrOutputParser()

res = chain.invoke({"input": input_text, "context": reference_text})
print(res)

#把向量库检索出来的内容作为prompt喂给模型的链，并输出模型的思考和回答