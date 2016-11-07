import sql_project

def connect_test1():
    obj_connect=sql_project.mysql()
    obj_connect.connect('localhost','Admin','Admin@123','Testdb',3)
    print obj_connect.cursor
    print str(obj_connect.cursor).find('Access denied')
    if (str(obj_connect.cursor).find('Access denied')) !=-1:
        print 'Test Fail and Connection denied'
    else:
        print 'Pass and Connection Accepted'

#pssword wrong
def connect_test2():
    obj_connect=sql_project.mysql()
    obj_connect.connect('localhost','Admin','Admin!123','Testdb',3)
    if (str(obj_connect.cursor).find('Access denied')) ==-1:
        print 'Test success and Connection denied'
    else:
        print 'Fail'


#connect_test1()
connect_test2()