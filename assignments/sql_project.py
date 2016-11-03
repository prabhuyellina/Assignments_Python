import MySQLdb
from ConfigParser import SafeConfigParser
class mysql:
    def __init__(self):
        fp=open('details.cfg','r')
        print fp
        parser=SafeConfigParser()
        parser.read(fp)
        print parser.get('[hai]','host')
      #  self.db = MySQLdb.connect(host, user, password, dbname)
      #  self.cursor = self.db.cursor()


    def select(self,Table_name, col_name, val):
        if col_name is 'all':
            quiery = "select *from %s" % (Table_name)
        else:
            quiery = "select *from %s where %s=%d" % (Table_name, col_name, val)
        self.cursor.execute(quiery)
        result = self.cursor.fetchall()
        for i in result:
            print i

    def insert(self,Table_name, data):
#        list_column_names = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'Testdb' AND TABLE_NAME = 'employee'"
        quiery = "INSERT INTO employee VALUES('%d','%s','%d','%d')" % (data['id'], data['name'], data['salary'], data['age'])
        self.cursor.execute(quiery)
        self.db.commit()

    def update(self,Table_name, data):
        quiery = "UPDATE %s SET id='%d', name='%s',salary='%d',age='%d' WHERE id='%d'" % (Table_name,data['id'], data['name'], data['salary'], data['age'], data['id'])
        self.cursor.execute(quiery)
        self.db.commit()

data = {"id": 6, "name": "Prem", "salary": 3622, "age": 32}
obj=mysql()
#obj.select('employee','all',2)
#obj.insert('employee',data)