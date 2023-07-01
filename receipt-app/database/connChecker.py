import mysql.connector

class Checker:
    def __init__(self, host, user, passwd, dbname):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbname = dbname
           
    def connCheck(self):
        connection = True
        message = "Pass"
        try:
            mysql.connector.connect(host=self.host, user=self.user, password=self.passwd, database=self.dbname)
        except Exception as e:
            y = str(e).split(" ")[0]
            connection = False
            if (str(y) == "2003:"): message = "Server Error"
            elif (str(y) == "1045"): message = "User Error"
            elif (str(y) == "Authentication"): message = "Password Error"
            elif (str(y) == "1049"): message = "Database Error"
            else: message = "Unknown Error"
        return (connection, message)