from http.client import responses
from pyexpat.errors import messages

from openai import OpenAI

# 1. 获取client对象

Client = OpenAI(
    base_url="http://127.0.0.1:11434/v1",#没买，统一就调用本地ollama
    api_key="ollama"
)

# 2. 调用模型

response = Client.chat.completions.create(
    model="qwen3:4b",
    messages=[
        {"role":"system","content":"你是我的第一个agent项目体"},
        {"role":"assistant","content":"好的，我是你的第一个agent项目"},
        {"role":"user","content":"输出一到十的二进制数字"}

    ]
)

# 3. 处理结果

print(response.choices[0].message.content)

