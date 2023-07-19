chat_history = []
message = {"role": "用户", "content": "user_input"}
chat_history.append(message)
chat_history.append({"role": "模型", "content": "模型"})
    
prompt = '\n'.join([f'{m["role"]}: {m["content"]}' for m in chat_history])

print(prompt)