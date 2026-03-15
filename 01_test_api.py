from openai import OpenAI

# 初始化客户端
client = OpenAI(
    base_url="http://127.0.0.1:11434/v1",  # 本地 Ollama
    api_key="ollama"
)

# 1. 初始化对话记录，添加图片中的 System 和 Assistant 预设
messages = [
    {"role": "system", "content": "你是一个Python编程专家。"},
    {"role": "assistant", "content": "我是一个Python编程专家。请问有什么可以帮助您的吗？"}
]

print("AI：我是一个Python编程专家。请问有什么可以帮助您的吗？")

while True:
    question = input("\n你：")
    if question.lower() in ['exit', 'quit']:
        break

    # 2. 将用户的输入加入到对话历史中
    messages.append({"role": "user", "content": question})

    # 3. 发起请求，传入完整的 messages 列表
    completion = client.chat.completions.create(
        model="qwen3:4b",  # 确保此名称与你本地模型库一致
        messages=messages,
        stream=True
    )

    print("AI：", end="")
    full_response = ""

    for chunk in completion:
        content = chunk.choices[0].delta.content
        if content:
            print(content, end="", flush=True)
            full_response += content

    # 4. 关键点：将 AI 的回复也存入 history，以便下次对话时它能记得自己说过什么
    messages.append({"role": "assistant", "content": full_response})

    print()