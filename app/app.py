from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return "Hello"
    elif request.method == 'POST':
        rows = ['='.join(item) for item in request.form.items()]
        s_post_data = '\n'.join(rows)
        with open("post.log", "a") as f_log:
            f_log.writelines(s_post_data)
        return s_post_data + '\n'

@app.route('/log')
def log():
    try:
        with open("post.log", "r") as f_log:
            return f_log.read() + '\n'
    except FileNotFoundError:
        return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
