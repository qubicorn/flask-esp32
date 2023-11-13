from flask import Flask, request

app = Flask(__name__)

@app.route('/write', methods = ['POST'])
def write():
    rows = ['='.join(item) for item in request.form.items()]
    s_post_data = '\n'.join(rows)
    with open("post.log", "a") as f_log:
        f_log.writelines(s_post_data)
        f_log.write("\n")
    return s_post_data

@app.route('/log')
def log():
    try:
        with open("post.log", "r") as f_log:
            return f_log.read()
    except FileNotFoundError:
        return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
