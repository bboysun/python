#
# completion.py
# @author darrylsun
# @description 
# @created 2023-07-19T09:40:14
# @last-modified 2023-07-19T09:40:14
#
import openai
from util import get_api_key_from_yaml, file_path


openai.api_key = get_api_key_from_yaml(file_path)


def completion_process(input_prompt):

    # 创建一个包含输入文本的字典
    # input_text = "Once upon a time"
    prompt = input_prompt
    data = {
        'prompt': prompt,
        # 'text': input_text,
        'max_tokens': 2500,
        'temperature': 0.5
    }

    # 调用 `openai.Completion.create` 函数进行生成
    response = openai.Completion.create(engine='text-davinci-003', **data)

    # 获取生成的文本
    generated_text = response.choices[0].text.strip()

    return generated_text