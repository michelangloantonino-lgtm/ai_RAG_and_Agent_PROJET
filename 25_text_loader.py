from operator import length_hint

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


loader = TextLoader("./Python基础语法.txt")

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500, #分段的最大值字符数
    chunk_overlap=50, #分段之间允许的重复字符数
    separators=["\n\n", '\n', "。", '!','，',',','.','。'],#自然文本段落的分割依据符号
    length_function=len
)

spliet_docs = splitter.split_documents(docs)

print(len(spliet_docs))
for doc in spliet_docs:
    print("="*20)
    print(doc)
    print("="*20)#("="*20)就是个分割线
