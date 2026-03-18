from langchain_community.document_loaders import CSVLoader

#就是把csv文件里的东西读出来

loader = CSVLoader(
    file_path="./stu.csv"
)
#已经把csv里的文件读出来了

#全加载出来，批量记载
# documents = loader.load()
#
# for document in documents:
#     print(document)

#懒加载

for document in loader.lazy_load():
    print(document)