from langchain_ollama import OllamaLLM

model = OllamaLLM(model="qwen3:4b")

res = model.stream("你是谁，能做什么？")
#改流式输出，本质上就是改这两个地方
for chunk in res:
    print(chunk, end="", flush=True)
    #invoke改为chunk