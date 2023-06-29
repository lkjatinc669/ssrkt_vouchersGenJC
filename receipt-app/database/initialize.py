import mysql.connector

class RecieptDatabase:
    def __init__(self, hostname, username, password, database):
        self.database = database
        self.table = "vouchers"
        self.connection =  mysql.connector.connect(
            host=hostname,
            user=username,
            password=password,
            database=database
        )

    def _insert(self, voucherNo, accHead, paidTo, rupeeNo, rupeeTxt, accountOf, byCCNo, bankAccNo):
        cursor = self.connection.cursor()
        sql = f"INSERT INTO {self.table} (voucherNo, accountHead,  paidTo, rupeesNo, rupeesText, onAccountOf, byChequeNoCash, bankAccount) VALUES \
        ('{voucherNo}', '{accHead}', '{paidTo}', '{rupeeNo}', '{rupeeTxt}', '{accountOf}', '{byCCNo}', '{bankAccNo}')"
        cursor.execute(sql)
        self.connection.commit()
        if cursor.rowcount == 1: return True
        else: return False

    def _fetch(self, voucherNo):
        cursor = self.connection.cursor()
        sql = f"SELECT * FROM {self.table} where voucherNo = {voucherNo}"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        if len(myresult) == 0:
            return False
        else:
            return myresult[0]
    
    def getLastVoucher(self):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT voucherNo from {self.table}")
        result = cursor.fetchall()
        result = result[-1]
        return result[0]
