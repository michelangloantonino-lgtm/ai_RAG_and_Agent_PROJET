from langchain_ollama import OllamaLLM
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

model = OllamaLLM(model="qwen3:4b")
str_parser = StrOutputParser()
my_fun = RunnableLambda(lambda ai_msg: {"name": ai_msg})

fist_prompt = PromptTemplate.from_template(
    "我邻居姓{lastname},刚生了{gender}，请起名，只要名字，不要别的信息"

)

second_prompt = PromptTemplate.from_template(
    "姓名为{name},请帮我解析其含义"
)

chain = fist_prompt | model | my_fun | second_prompt | model | str_parser

#res = chain.invoke({"lastname":"张","gender":"女"})
#print(res)

for chunk in chain.stream(
    {"lastname":"张","gender":"女"}):
    print(chunk, end=" ", flush=True)
