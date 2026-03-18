from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain_chroma import Chroma


#chroma 向量数据库（轻量级）

#确保langchain-chroma 和chromadb这两个库是安装了的
vector_store = Chroma(
    collection_name="test",#给当前存储起名字，类似数据库的表名称
    embedding_function=DashScopeEmbeddings(),#文本转化为向向量模型的话，就用DashScopeEmbeddings
    persist_directory="./chroma_db"#指定数据存放的文件夹
)
# loader = CSVLoader(
#     file_path="./info.csv",
#     encoding="utf-8",
#     source_column="source",  #  指定本条数据的来源是哪里
#
# )
# documents = loader.load()
#
# vector_store.add_documents(
#     documents=documents,
#     ids=["id"+str(i) for i in range(1,len(documents)+1)]
# )
# #把每一条信息都转化为向量，并编号储存

#使用chroma库的话，直接跳过内存，存储在本地，就不需要挨个再loader了

result = vector_store.similarity_search(
    "python很简单",
    3,
    #用向量的形式，挨个儿搜索
    filter={"source":"黑马程序员"}#只提取其中的黑马程序员，这一项，起到过滤的挪用
)
print(result)
