import MySQLdb
import ConfigParser
import logging
class mysql:
    def __init__(self):
        logging.basicConfig(format='%(asctime)s %(message)s',filename='log.txt',level=logging.DEBUG)
        fp=ConfigParser.ConfigParser()
        fp.read('details.cfg')
        try:
            host_name=fp.get('Details', 'host')
            user_name = fp.get('Details', 'user')
            password = fp.get('Details', 'password')
            dbname = fp.get('Details', 'dbname')
            count = fp.get('Details', 'count')
        except ConfigParser.Error as e:
            print e
            logging.debug('Error near config file')
        self.connect(host_name, user_name, password, dbname,count)

    def connect(self,host_name, user_name, password, dbname,count):
        try:
            logging.debug('Tried to connect')
            self.db = MySQLdb.connect(host_name, user_name, password, dbname)
            self.cursor =self.db.cursor()
            if self.db and self.cursor != None:
                return
            for i in count:
                self.connect(self, host_name, user_name, password, dbname, count)

        except MySQLdb.Error as e:
            print e
            logging.debug('Error near in connect call')


    def select(self,Table_name, col_name, val,All_coloums=True):
        logging.debug('In select function')
        if All_coloums is True:
            quiery = "select *from %s" % (Table_name)
        else:
            if type(col_name) is not 'dict':
                quiery = "select *from %s where %s=%d" % (Table_name, col_name, val)
            else:
                for key in col_name:
                    quiery = "select *from %s where %s=%d" % (Table_name, key,col_name[key])
                    self.cursor.execute(quiery)
                return

        try:
            self.cursor.execute(quiery)
            result = self.cursor.fetchall()
            for i in result:
                print i
        except MySQLdb.Error as e:
            print e
            logging.debug('Error near select call')
            self.select(Table_name, col_name, val, All_coloums)

    def insert(self,Table_name, data):
        logging.debug('In Insert Function')
#        list_column_names = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'Testdb' AND TABLE_NAME = 'employee'"
        quiery = "INSERT INTO employee VALUES('%d','%s','%d','%d')" % (data['id'], data['name'], data['salary'], data['age'])
        try:
            self.cursor.execute(quiery)
            self.db.commit()

        except MySQLdb.Error as e:
            print e
            logging.debug('Error near Insert function')
            self.insert(Table_name, data)

    def update(self,Table_name, data):
        logging.debug('In Update function')
        quiery = "UPDATE %s SET id='%d', name='%s',salary='%d',age='%d' WHERE id='%d'" % (Table_name,data['id'], data['name'], data['salary'], data['age'], data['id'])

        try:
            self.cursor.execute(quiery)
            self.db.commit()
        except MySQLdb.Error as e:
            print e
        logging.debug('Error near update function')
        self.update(Table_name, data)

#data = {"id": 6, "name": "Prem", "salary": 3622, "age": 32}
obj=mysql()
#obj.select('employee','all',2)
#obj.insert('employee',data)