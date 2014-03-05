from warnings import filterwarnings
import MySQLdb
filterwarnings('ignore', category = MySQLdb.Warning)
# MYSQL class made as a technical test for dedsert by Adam Marc Jeanes.
# usage:
# import dedsert
# db = dedsertDB('ip', '3306', 'user', 'password' 'database')
# db.create_user('Adam Marc Jeanes', 22, 'Server Developer')
# db.list_users()
class dedsertDB():
	def __init__(self, ip, port, user, password, database):
		self.__server = ip
		self.__port = port #this might be superfulous
		self.__database = database
		self.__db_user = user #yeah, yeah, ethical hacker and all that
		self.__db_pass = password
		self.setup()
	def setup(self):
		#create table if it doesnt exist
		setupconn = MySQLdb.connect(self.__server, self.__db_user, self.__db_pass, self.__database)
		setupcur = setupconn.cursor()
		setupcur.execute('CREATE TABLE IF NOT EXISTS dedsert_test(id INT NOT NULL AUTO_INCREMENT, name VARCHAR (20), age INT, job_title VARCHAR (20), PRIMARY KEY(id))ENGINE=InnoDB') 
		setupconn.commit()
		del setupcur
		del setupconn
	def __startDBop(self):
		self.__DB = MySQLdb.connect(self.__server, self.__db_user, self.__db_pass, self.__database)
		self.datastore = self.__DB.cursor()
	def __stopDBop(self):
		del self.datastore
	def execute(self, cmd, insert=False):
		self.__startDBop()
		if(self.datastore):
			self.datastore.execute(cmd)
			output = self.datastore.fetchall()
			if(insert == True):
				self.__DB.commit()
			self.__stopDBop()
			return output
		else:
			print 'DB error'
	def list_users(self):
		sql = 'SELECT * FROM dedsert_test;'
		for row in self.execute(sql):
			print '[%s] Name: %s Job Title: %s Age: %s' % (int(row[0]), row[1], row[3], int(row[2]))
	def create_user(self, name, age, job):
		sql = 'INSERT INTO dedsert_test (name, age, job_title) VALUES(\'%s\', \'%s\', \'%s\');' % (name, int(age), job)
		print self.execute(sql, True)
