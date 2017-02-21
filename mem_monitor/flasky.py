from flask import Flask, render_template
import MySQLdb as mysql
import json
db = mysql.connect(user='root', passwd='', db='memory', host='localhost')
db.autocommit(True)
cur = db.cursor()

app = Flask(__name__)
tmp_time = 0
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/data')
def data():
	global tmp_time
	if tmp_time > 0:
		sql = 'select * from memory where time>%s' % (tmp_time/1000)
	else:
		sql = 'select * from memory'
	cur.execute(sql)
	arr = []
	for i in cur.fetchall():
		arr.append([i[1]*1000, i[0]])
	if len(arr)>0:
		tmp_time = arr[-1][0]
	return json.dumps(arr)
if __name__=='__main__':
	app.run(debug=True)

