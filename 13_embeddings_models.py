from langchain_ollama import OllamaEmbeddings

#选择嵌入模型即可

model = OllamaEmbeddings(model="qwen3-embedding:latest")

print(model.embed_query("J'taime"))#单个的用query
print(model.embed_documents(["J'taime", "ti amo"]))#一堆的用documents

#潜入模型的本质，文本转化为向量

