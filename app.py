#
# hello.py
# @author darrylsun
# @description
# @created 2023-07-05T16:37:32
# @last-modified 2023-07-05T16:37:32
#
from flask import Flask, request, render_template, jsonify
from chat import process_user_input
from completion import completion_process

app = Flask(__name__)


@app.get("/")
def hello_world():
    return render_template('index.html')


@app.post("/login")
def login():
    print(request.form)
    username = request.form.get('username')
    password = request.form.get('password')   
    if username == 'darrylsun' and password == "admin999":
        # 返回自定义响应
        response = {
            'code': 0,
            'message': 'Success',
            'data': {
                'username': username,
                'password': password
            }
        }
        return response
    else:
        # 返回自定义响应
        # 返回自定义响应
        response = {
            'code': 401,
            'message': 'Forbidden',
            'data': {
                'username': username,
                'password': password
            }
        }
        return response


@app.route('/denied')
def denied():
    return render_template('denied.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/process', methods=['POST'])
def process():
    user_input = request.json['userInput']
    # 处理用户输入，返回机器人响应
    bot_response = process_user_input(user_input)
    return jsonify({'botResponse': bot_response})


@app.route('/extraction', methods=['POST'])
def extraction():
    user_input = request.json['input']
    # 处理用户输入
    bot_response = completion_process(user_input)
    return jsonify({'botResponse': bot_response})
