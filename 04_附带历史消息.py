from openai import OpenAI

# 1. 获取 client 对象
client = OpenAI(
    base_url="http://127.0.0.1:11434/v1",
    api_key="ollama"
)

# 2. 调用模型
response = client.chat.completions.create(
    model="qwen3:4b",  # 请确保你本地 ollama list 里有这个模型，qwen3 还没发布哦
    messages=[
        {"role": "system", "content": "你是我的第一个agent项目体，回答风格很简洁"},
        {"role": "user", "content": "hugo是个摄影师"},
        {"role": "assistant", "content": "c'est bon"},
        {"role": "user", "content": "hugo是个学生"},
        {"role": "assistant", "content": "c'est bon"},
        {"role": "user", "content": "hugo的身份是什么"}
    ],
    stream=True
)

# 3. 处理结果
# 注意：这里迭代的是 response 而不是 responses
for chunk in response:
    # 获取 delta 内容
    content = chunk.choices[0].delta.content

    # 检查内容是否不为空
    if content is not None:
        print(content, end="", flush=True)