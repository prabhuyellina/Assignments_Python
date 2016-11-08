import sql_project
import unittest
import ConfigParser


class TestMyFunctions(unittest.TestCase):
    def setUp(self):
        self.fp=ConfigParser.ConfigParser()
        self.fp.read('details.cfg')
    def test_connect_correct_args(self):
        host_name = self.fp.get('Details', 'host')
        user_name = self.fp.get('Details', 'user')
        password = self.fp.get('Details', 'password')
        dbname = self.fp.get('Details', 'dbname')
        count = self.fp.get('Details', 'count')
        self.obj_connect = sql_project.mysql()
        self.obj_connect.connect(host_name, user_name, password, dbname,count)
        self.assertNotIn('Access denied',str(self.obj_connect.cursor))

    def test_connect_wrong_args(self):
        host_name = self.fp.get('Wrong_Details', 'host')
        user_name = self.fp.get('Wrong_Details', 'user')
        password = self.fp.get('Wrong_Details', 'password')
        dbname = self.fp.get('Wrong_Details', 'dbname')
        count = self.fp.get('Wrong_Details', 'count')
        self.obj_connect1 = sql_project.mysql()
        self.obj_connect1.connect(host_name, user_name, password, dbname,count)
        self.assertIn('Access denied',str(self.obj_connect1.cursor))


if __name__=='__main__':
    unittest.main()