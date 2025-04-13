# Flaskフレームワークから必要なモジュールをインポート
from flask import Flask, jsonify

# datetimeモジュールをインポート（現在時刻取得に使用）
import datetime

# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)

# '/time'というURLパスにアクセスしたときに実行される関数を定義
@app.route('/time')
def get_time():
    # 現在の日時を取得
    now = datetime.datetime.now()
    
    # 現在の秒（second）だけをJSON形式で返却
    return jsonify({
        'second': now.second
    })

# スクリプトが直接実行された場合にFlaskアプリを起動
if __name__ == '__main__':
    # すべてのネットワークインターフェースからのアクセスを許可し、
    # ポート番号10000でFlaskアプリを起動
    app.run(host='0.0.0.0', port=10000)
