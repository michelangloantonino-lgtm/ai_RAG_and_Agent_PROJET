from langchain_ollama import OllamaLLM
from langchain_core.output_parsers import  StrOutputParser
from langchain_core.prompts import PromptTemplate



model = OllamaLLM(model="qwen3:4b")
prompt = PromptTemplate.from_template(
    "我是:{名字},希望拍{内容},请评价我的摄影风格"

)

#chain = prompt | model | model 这么直接写是绝对不行的，要报错，中间差一个解释器

parser = StrOutputParser()
chain = prompt | model | parser | model #这么写才行，model与model之间必须要有解释器
res = chain.invoke({"名字":"布列松", "内容":"决定性瞬间"})
print(res)


