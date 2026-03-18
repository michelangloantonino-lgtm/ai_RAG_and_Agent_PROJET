from langchain_community.document_loaders import JSONLoader
from sqlalchemy import false

# loader = JSONLoader(
#     file_path="./stu.json",
#     jq_schema=".",
#     text_content=False#如果要全部都照着输出下来的话，必须要带这个，不然就报错
# )

# loader = JSONLoader(
#     file_path="./stus.json",
#     jq_schema=".[].name",
#     text_content=False#如果要全部都照着输出下来的话，必须要带这个，不然就报错
# )
#像这种既不是单个json，也不是json数组的，单纯的把一个个json排在一起的这种，就需要这么写，加一个变量
loader = JSONLoader(
    file_path="./stu_json_lines.json",
    jq_schema=".name",
    text_content=False,#如果要全部都照着输出下来的话，必须要带这个，不然就报错
    json_lines=True
)
document = loader.load()
print(document)
