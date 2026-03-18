from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path="./pdf2.pdf",
    mode="single", #默认就是page模式，原来多少页，就返回多少页，single模式，不管有多少页，最后只返回一页
    password="itheima"#像这种带密码的pdf，需要再额外输入一个password
)
i = 0
for doc in loader.lazy_load():
    i += 1
    print(doc)
    print("="*20, i)