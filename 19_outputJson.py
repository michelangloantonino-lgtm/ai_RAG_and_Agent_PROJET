from langchain_ollama import OllamaLLM
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import PromptTemplate

model = OllamaLLM(model="qwen3:4b")

json_parser = JsonOutputParser()
str_parser = StrOutputParser()

premiere_prompt = PromptTemplate.from_template(
"""
我是作家{name}，我写了一本书《{title}》。
请评价这本书，并严格返回JSON：


{{
"name":"{name}",
"title":"{title}"
}}

不要输出任何其他内容。
"""
)
#第二句提示词很重要，要强调给出的是json格式，不然的话，第二个模版不知道传进来的是什么玩意儿

deuxieme_prompt = PromptTemplate.from_template(
"书名是{title}，请解释这本书背后的意味"
)

chain = (
    premiere_prompt
    | model
    | json_parser
    | deuxieme_prompt
    | model
    | str_parser
)

for chunk in chain.stream({
    "name": "金宇澄",
    "title": "繁花"}):
    print(chunk, end="", flush=True)