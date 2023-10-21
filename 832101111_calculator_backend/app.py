from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name)

# MySQL数据库连接配置
db_config = {
    "host": "127.0.0.1",  # MySQL主机名
    "user": "root",  # MySQL用户名
    "password": "IchLiebeMori",  # MySQL密码
    "database": "calculator_db"  # MySQL数据库名
}

# 创建MySQL数据库连接
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# 创建历史记录表
cursor.execute('''CREATE TABLE IF NOT EXISTS history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    expression TEXT,
    result FLOAT
)''')
conn.commit()

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression')

    try:
        result = eval(expression)
        store_history(expression, result)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/history', methods=['GET'])
def get_history():
    cursor.execute("SELECT expression, result FROM history ORDER BY id DESC LIMIT 10")
    history = cursor.fetchall()
    return jsonify(history)

@app.route('/ans', methods=['GET'])
def get_ans():
    cursor.execute("SELECT result FROM history ORDER BY id DESC LIMIT 1")
    ans = cursor.fetchone()
    if ans:
        return jsonify({'ans': ans[0]})
    else:
        return jsonify({'ans': None})

def store_history(expression, result):
    cursor.execute("INSERT INTO history (expression, result) VALUES (%s, %s)", (expression, result))
    conn.commit()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
