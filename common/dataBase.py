# coding=utf-8 

import pymysql
from common.readConfig import confParam


class dataBase:
    def __init__(self, db):
        self.host = confParam("host")
        self.user = confParam("user")
        self.password = confParam("dbpassword")
        self.port = int(confParam("port"))
        self.db = db
        self.con = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                  db=self.db, port=self.port, charset="utf8")
        self.cur = self.con.cursor()

    def get_companyinfo(self,col_name,table_name,project_name,key):
        sql="select {} from {} where {}='{}' ".format(col_name,table_name,project_name,key)
        self.cur.execute(sql)
        return self.cur.fetchall()[0][0]

    def getId(self, col_name, table_name):
        sql = "Select max({}) from {}".format(col_name, table_name)
        self.cur.execute(sql)
        return self.cur.fetchall()[0][0]

    def getworkId(self, col_name, table_name):
        sql = "select {} from {} ORDER BY {} desc LIMIT 1".format(col_name, table_name,col_name)
        self.cur.execute(sql)
        return self.cur.fetchall()[0][0]

    def getprojectId(self, col_name, table_name):
        sql = "select {} from {} ORDER BY {} desc LIMIT 1".format(col_name, table_name,"id")
        self.cur.execute(sql)
        return self.cur.fetchall()[0][0]

    def flowId(self, col_name, table_name):
        sql = "select {} from {} ORDER BY {} desc LIMIT 1".format(col_name, table_name,"id")
        self.cur.execute(sql)
        return self.cur.fetchall()[0][0]

    def taskId(self, col_name, table_name):
        sql = "select {} from {} ORDER BY {} desc LIMIT 1".format(col_name, table_name,col_name)
        self.cur.execute(sql)
        return self.cur.fetchall()[0][0]

    def closeDb(self):
        self.cur.close()
        self.con.close()


if __name__ == "__main__":
    dbName = confParam("用户信息")
    db = dataBase(dbName)
    a = db.get_companyinfo("company_name","a_company_info","id",26)
    print(a)

    dbName = confParam("电站管理")
    db = dataBase(dbName)
    a = db.getId("id", "station_inverter_info")
    print(a)

    dbName = confParam("电站管理")
    db = dataBase(dbName)
    a = db.getId("id", "work_order_info")
    print(a)
    print(type(a))

    dbName = confParam("电站管理")
    db = dataBase(dbName)
    a = db.getprojectId("project_id", "work_order_info")
    print(a)

    dbName = confParam("电站管理")
    db = dataBase(dbName)
    a = db.getprojectId("flow_id", "work_order_info")
    print(a)

    dbName = confParam("电站管理")
    db = dataBase(dbName)
    a = db.getworkId("task_id", "work_order_flow")
    print(a)
    print(type(a))