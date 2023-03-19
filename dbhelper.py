import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host="localhost",
                                     port="3306",
                                     user="root",
                                     password="pugalmurugan",
                                     database="pythontest")
        query = "create table if not exists user (userId int primary key, userName varchar(200), phone varchar(12))"
        cur = self.con.cursor()
        cur.execute(query)
        print("Created")

    def insert_user(self, userid, username, phone):
        query = "insert into user(userId, userName, phone) values({}, '{}', '{}')".format(userid, username, phone)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Inserted!")

    def fetch_all(self):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("UserId: ", row[0], "\nUserName: ", row[1], "\nPhone: ", row[2], "\n")

    def fetch(self, userId):
        query = "select userName, phone from user where userId = {}".format(userId)
        cur = self.con.cursor()
        cur.execute(query)
        for i in cur:
            print("Username: ", i[0], "\nPhone: ", i[1], "\n")

    def delete_user(self, userId):
        query = "delete from user where userId = {}".format(userId)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Data Deleted")

    def update(self, userid, updated_username, updated_phone):
        query = "update user set userName = '{}', phone = '{}' where userId = {}".format(updated_username, updated_phone, userid)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Data Updated")
