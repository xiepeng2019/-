import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s%(message)s')
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/score/<int:score>')
def hello_name(score):
    return render_template('score.html', score=score)
if __name__ == '__main__':
    app.run(debug=True,host="192.168.31.237",port="5002")