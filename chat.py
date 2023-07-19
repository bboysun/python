#
# chat.py
# @author darrylsun
# @description
# @created 2023-07-10T17:20:30
# @last-modified 2023-07-10T17:20:30
#
import openai


openai.api_key = 'key'


chat_history = [{'role': 'system', 'content': 'You are a helpful assistant.'}]


def process_user_input(user_input):
    global chat_history

    message = {"role": "user", "content": user_input}
    chat_history.append(message)
    
    # prompt_val = '\n'.join([f'{m["role"]}: {m["content"]}' for m in chat_history])

    # print(prompt_val)

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=chat_history
    )

    if 'choices' in response:
        reply = response['choices'][0]['message']['content']
        print("reply is ", reply)
        reply_message = {"role": "assistant", "content": reply}
        chat_history.append(reply_message)
        return reply
    else:
        return None

