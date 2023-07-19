#
# util.py
# @author darrylsun
# @description 
# @created 2023-07-19T14:31:03
# @last-modified 2023-07-19T14:31:03
#
import yaml


# 读取本地 YAML 文件并获取 api_key 的值
file_path = 'config/application.yaml' 


def get_api_key_from_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            yaml_data = yaml.safe_load(file)
            api_key = yaml_data.get('openai').get('key')
            return api_key
    except FileNotFoundError:
        raise FileNotFoundError("application yaml file cannot find")
    except IOError:
        raise IOError("read application yaml file IO error")

