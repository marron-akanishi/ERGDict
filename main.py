import os
import flask
import make_title as title
import make_brand as brand

# 自身の名称を app という名前でインスタンス化する
app = flask.Flask(__name__)

# ここからウェブアプリケーション用のルーティングを記述
# トップページ
@app.route('/')
def index():
    return flask.render_template('index.html')

# タイトル辞書生成
@app.route('/maketitle', methods=['GET'])
def maketitle():
    startday = flask.request.args.get('sellday', default='1995-01-01', type=str)
    unknown = checkbox(flask.request.args.get('unknown', default='off', type=str))
    okazu = checkbox(flask.request.args.get('okazu', default='off', type=str))
    return title.make(startday, unknown, okazu)

# ブランド辞書生成
@app.route('/makebrand', methods=['GET'])
def makebrand():
    circle = checkbox(flask.request.args.get('circle', default='off', type=str))
    lost = checkbox(flask.request.args.get('lost', default='off', type=str))
    return brand.make(circle, lost)

def checkbox(text):
    if text == "on":
        return True
    else:
        return False

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080))) # どこからでもアクセス可能に
