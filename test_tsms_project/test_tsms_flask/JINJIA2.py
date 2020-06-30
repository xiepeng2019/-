from flask import Flask, render_template
import records,requests,request
from tsms_pytest_commons.configs import tsms_db_config
import logging
from xml.sax.saxutils import unescape
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')

# db = records.Database(
#     'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
#         tsms_db_config.get("user"),
#         tsms_db_config.get("passwd"),
#         tsms_db_config.get("host"),
#         tsms_db_config.get("port"),
#         tsms_db_config.get("db"),
#     )
# )

db = records.Database('mysql+pymysql://debian-sys-maint:6udZCFBibeLtPuiG@148.70.194.135:3306/flaskblog?charset=utf8')

app = Flask(__name__)


@app.route('/signlist')
def sign_list():
    table_type = "签名列表"
    rows = db.query("select * from sms_sign where is_delete=0 order by sign_id desc limit 10;")
    table_html = rows.export("html")
    # table_html = table_html.replace("<table>", "<table class=\"table table-condensed\" style=\"word-break:break-all; word-wrap:break-all;\">")

    # table_html = table_html.replace("<tr>", "<tr class=\"info\" style=\"word-break:break-all; word-wrap:break-all;>\">")
    table_html = unescape(table_html)
    return render_template("test_jinja2_modify.html", table_html=table_html, table_type=table_type)


@app.route('/sendlist')
def send_list():
    table_type = "发送列表"
    rows = db.query("select * from sms_send where is_delete=0 order by id desc limit 10;")
    logging.info("[rows]: {}".format(rows.as_dict()))
    table_html = rows.export("html")
    # table_html = table_html.replace("<table>", "<table class=\"table table-condensed\" style=\"word-break:break-all; word-wrap:break-all;\">")
    # table_html = table_html.replace("<tr>", "<tr class=\"info\">")
    table_html = unescape(table_html)
    return render_template("test_jinja2_modify.html", table_html=table_html, table_type=table_type)



if __name__ == '__main__':
    app.run(debug=True, host="192.168.31.237",port="5011")