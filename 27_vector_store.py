from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader

vector_store = InMemoryVectorStore(
    embedding=DashScopeEmbeddings(),
)
loader = CSVLoader(
    file_path="./info.csv",
    encoding="utf-8",
    source_column="source",  #  指定本条数据的来源是哪里

)
documents = loader.load()

vector_store.add_documents(
    documents=documents,
    ids=["id"+str(i) for i in range(1,len(documents)+1)]
)
#把每一条信息都转化为向量，并编号储存

result = vector_store.similarity_search(
    "python很简单",
    3
    #用向量的形式，挨个儿搜索
)
print(result)
