from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_ollama import OllamaLLM#接入模型
#给出示例的模版
example_temple = PromptTemplate.from_template("单词：{word},反义词:{antonym}")
#示例的动态数据，list套内的字典

example_data = [
    {"word":"大", "antonym":"小"},
    {"word":"近", "antonym":"远"}

]


few_shot_template = FewShotPromptTemplate(
    example_prompt=example_temple,#示例的模版
    examples=example_data,#式例的数据，用来注入动态的数据，list内套字典
    prefix="告知我单词的反义词，我给出了如下的示例",#示例之前的提示词
    suffix="基于前面的示例告诉我,{input_word}的反义词是什么",#示例之后的提示词
    input_variables=["input_word"]#生命在前缀/后缀中所需要注入的变量名
)

prompt_test = few_shot_template.invoke(input={"input_word":"左"}).to_string()

#给一个prompt变量去存入这个结果

print(prompt_test)

model = OllamaLLM(model="qwen3:4b")#定义模型
print(model.invoke(input=prompt_test))#直接传入prompt，prompt_test,即可
