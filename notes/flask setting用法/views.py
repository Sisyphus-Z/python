from flask import Flask,current_app

app = Flask(__name__)

app.config.from_object('setting.BaseConfig')


@app.route('/index',methods=['GET'])
def index():
    print(current_app.config['MESSAGE_CLASSES'])
    print(current_app.config['NNN'])
    return '123'

if __name__ == '__main__':
    app.run()