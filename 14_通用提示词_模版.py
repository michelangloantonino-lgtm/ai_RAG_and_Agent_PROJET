from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
#这个训练本质上也是个zero_shot

prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname},喜得子，帮忙取一个名字"
)#先给到一个通用的模版

#调用.format方法，注入信息
# prompt_text = prompt_template.format(lastname="罗")
#
# print(prompt_text)
#
model = OllamaLLM(model="qwen3:4b")
# res = model.invoke(input=prompt_text)
# print(res)
chain = prompt_template | model
res = chain.invoke(input={"lastname":"罗"})
print(res)

//使用chain链取表达