#
# util.py
# @author darrylsun
# @description 
# @created 2023-07-19T14:31:03
# @last-modified 2023-07-19T14:31:03
#

def read_file():
    file_path = 'path/to/your/file.txt'  # 替换为你的文件路径

    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
        return file_content
    except FileNotFoundError:
        return 'File not found'
    except IOError:
        return 'Error reading file'