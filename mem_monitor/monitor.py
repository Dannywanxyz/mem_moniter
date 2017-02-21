import linecache
import MySQLdb as mysql
import time
db = mysql.connect(user='root', passwd='', db='memory', host='localhost')
db.autocommit(True)
cur = db.cursor()

def getMem():
	linecache.clearcache()
	memavailabal = int(linecache.getline(r'/proc/meminfo', 3).split()[1])/1024
	local_time = int(time.time())
	# print local_time, type(local_time)
	sql = 'insert into memory (memory, time) value (%s, %s)' % (memavailabal, local_time)
	cur.execute(sql)
	# print sql, 'ok'
while True:
	time.sleep(1)
	getMem()
