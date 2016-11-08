import sql_project
import unittest
import ConfigParser

class Test_select(unittest.TestCase):
    def setUp(self):
        self.fp=ConfigParser.ConfigParser()
        self.fp.read('details.cfg')
        self.host_name = self.fp.get('Details', 'host')
        self.user_name = self.fp.get('Details', 'user')
        self.password = self.fp.get('Details', 'password')
        self.dbname = self.fp.get('Details', 'dbname')
        self.count = self.fp.get('Details', 'count')
        self.obj=sql_project.mysql()
        self.obj.connect(self.host_name, self.user_name, self.password, self.dbname,self.count)

    def test_select(self):
        self.obj.select('employee','id',1,False)
        print self.obj.cursor.fetchone()
#        self.assertIn(self.obj.cursor.fetchall(),(1L, 'Prabhu', 2500L, 26L))
    def tearDown(self):
        self.obj.db.close()

if __name__=='__main__':
    unittest.main()


