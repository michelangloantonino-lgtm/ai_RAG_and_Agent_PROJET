from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_ollama import OllamaLLM
from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory

# 1️⃣ 初始化 Ollama 模型
model = OllamaLLM(model="qwen3:4b")

# 2️⃣ 构建 ChatPromptTemplate，放置历史消息占位符
prompt = ChatPromptTemplate(
    messages=[
        ("system", "你需要根据对话的历史，来回答用户的问题"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "请回答如下问题:{input}")
    ]
)

# 3️⃣ 输出解析器
str_parser = StrOutputParser()

# 4️⃣ 构建基础链
base_chain = prompt | model | str_parser

# 5️⃣ session历史存储
store = {}

def get_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# 6️⃣ 构建带历史的可运行链
conversation_chain = RunnableWithMessageHistory(
    base_chain,
    get_history,
    input_messages_key="input",
    history_messages_key="chat_history"
)

# 7️⃣ 测试对话
if __name__ == "__main__":
    session_config = {"configurable": {"session_id": "user_001"}}

    res1 = conversation_chain.invoke({"input": "小明有两只猫"}, session_config)
    print("第一次执行:", res1)

    res2 = conversation_chain.invoke({"input": "小明有一只狗"}, session_config)
    print("第二次执行:", res2)

    res3 = conversation_chain.invoke({"input": "总共有几只宠物"}, session_config)
    print("第三次执行:", res3)