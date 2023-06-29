from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import json
import datetime
from libs import wordGen
from database import initialize
from libs import listUpdater
from libs import printer

listUpdater

class App():
    def __init__(self, master):
        self.y = 190
        self.increment = 40
        self.master = master

        self.loadList()
        self.dbConnStatics = self.getDBStatics()
        self.currtime = self.getCurrTime()

        self.cashorbank = ["Cash", "Bank"]

        self.stringVar_voucherNoS = StringVar()
        self.stringVar_voucherNo = StringVar()
        self.stringVar_accHead = StringVar()
        self.stringVar_accHead.set("Select")
        self.stringVar_accHeadO = StringVar()
        self.stringVar_paidTo = StringVar()
        self.stringVar_rupeesNo = StringVar()
        self.stringVar_rupeesTxt = StringVar()
        self.stringVar_accountOf = StringVar()
        self.stringVar_byCCNo = StringVar()
        self.stringVar_bankAccNo = StringVar()
        self.stringVar_onDate = StringVar()

        self.topBanner1 = Label(self.master, text="Seva Sadan's", width=110)
        self.topBanner1.place(x=10, y=10)
        self.topBannerDate = Label(self.master, text=f"Date: {self.currtime}")
        self.topBannerDate.place(x=10, y=10)
        self.topBannerVoucherL = Label(self.master, text=f"Voucher No: ")
        self.topBannerVoucherL.place(x=730, y=10)
        self.topBannerVoucherE = Entry(self.master, textvariable=self.stringVar_voucherNo, width=5, state="disabled")
        self.topBannerVoucherE.place(x=815, y=10)
        self.topBanner2 = Label(self.master, text="R. K. Talreja College", width=110)
        self.topBanner2.place(x=10, y=40)
        self.topBanner3 = Label(self.master, text="Arts, Science and Commerce", width=110)
        self.topBanner3.place(x=10, y=70)
        self.topBanner4 = Label(self.master, text="Ulhasnagar-421003", width=110)
        self.topBanner4.place(x=10, y=100)
        self.topBanner5 = Label(self.master, text="Debit Voucher", width=110)
        self.topBanner5.place(x=10, y=130)

        self.voucherNoL = Label(self.master, text="Voucher No (JC): ")
        self.voucherNoL.place(x=10, y=self.y)
        self.voucherNoE = Entry(self.master, textvariable=self.stringVar_voucherNoS)
        self.voucherNoE.place(x=150, y=self.y)
        self.voucherNoB = Button(self.master, text="Load", command=self.load, width=10, height=1)
        self.voucherNoB.place(x=330, y=self.y-5)
        self.voucherNoB = Button(self.master, text="Load & Print", command=self.loadandprint, width=10, height=1)
        self.voucherNoB.place(x=450, y=self.y-5)

        self.y += self.increment
        
        self.accHeadL = Label(self.master, text="Account Head")
        self.accHeadL.place(x=10, y=self.y)
        # self.accHeadO = OptionMenu(self.master, textvariable=self.stringVar_accHead, *self.accountHeadOptList, command = self.changedetector)
        self.accHeadO = ttk.Combobox(root, textvariable=self.stringVar_accHead, state='readonly', values=self.accountHeadOptList)
        self.accHeadO.place(x=150, y=self.y-5)
        self.accHeadO.bind("<<ComboboxSelected>>", self.changedetector)

        self.accHeadOL = Label(self.master, text="Please Specify")
        self.accHeadOL.place(x=360, y=self.y)
        self.accHeadOE = Entry(self.master, state="disabled", textvariable=self.stringVar_accHeadO)
        self.accHeadOE.place(x=480, y=self.y)

        self.y += self.increment
        
        self.paidToL = Label(self.master, text="Paid To:")
        self.paidToL.place(x=10, y=self.y)
        self.paidToE = Entry(self.master, textvariable=self.stringVar_paidTo)
        self.paidToE.place(x=150, y=self.y)

        self.y += self.increment

        self.rupeesNoL = Label(self.master, text="Rs:")
        self.rupeesNoL.place(x=10, y=self.y)
        self.rupeesNoE = Entry(self.master, textvariable=self.stringVar_rupeesNo)
        self.rupeesNoE.place(x=150, y=self.y)
        self.rupeesNoE.bind("<FocusOut>", self.toText)

        self.rupeesTxtL = Label(self.master, text="in Text")
        self.rupeesTxtL.place(x=330, y=self.y)
        self.rupeesTxtE = Entry(self.master , width=50, textvariable=self.stringVar_rupeesTxt)
        self.rupeesTxtE.place(x=450, y=self.y)

        self.y += self.increment

        self.accountOfL = Label(self.master, text="On Account of")
        self.accountOfL.place(x=10, y=self.y)
        self.accountOfE = Entry(self.master , width=50, textvariable=self.stringVar_accountOf)
        self.accountOfE.place(x=150, y=self.y)

        self.y += self.increment

        self.byCCNoL = Label(self.master, text="Type")
        self.byCCNoL.place(x=10, y=self.y)
        # self.byCCNoE = Entry(self.master, textvariable=self.stringVar_byCCNo)
        self.byCCNoE = ttk.Combobox(self.master, textvariable=self.stringVar_byCCNo, state='readonly', values=self.cashorbank)
        self.byCCNoE.place(x=150, y=self.y)

        self.bankAccNoL = Label(self.master, text="Bank Acc. No")
        self.bankAccNoL.place(x=330, y=self.y)
        self.bankAccNoE = Entry(self.master, textvariable=self.stringVar_bankAccNo)
        self.bankAccNoE.place(x=450, y=self.y)

        self.onDateL = Label(self.master, text="On")
        self.onDateL.place(x=640, y=self.y)
        self.onDateE = Entry(self.master, textvariable=self.stringVar_onDate)
        self.onDateE.place(x=690, y=self.y)
        self.onDateE.insert(0, "Autogenerated")
        self.onDateE.config(state="disabled")

        self.y += self.increment

        self.buttonNew = Button(self.master, text="New", command=self.new, width=10)
        self.buttonNew.place(x=390, y=self.y)
        self.buttonSave = Button(self.master, text="Save", command=self.save, width=10)
        self.buttonSave.place(x=510, y=self.y)
        self.buttonClear = Button(self.master, text="Clear", command=self.clear, width=10)
        self.buttonClear.place(x=630, y=self.y)
        self.buttonSaveAndPrint = Button(self.master, text="Save & Print", command=self.saveandprint, width=10)
        self.buttonSaveAndPrint.place(x=750, y=self.y)

        self.setVoucherNo()

    def loadList(self):
        with open(r'statics/headDept.json', 'r+') as file:
            data = json.load(file)
            self.accountHeadOptList = data['accountHead']
        self.accountHeadOptListO = self.accountHeadOptList
        self.accountHeadOptList.append("Other")

    def getDBStatics(self):
        with open(r'statics/dbStatics.json', 'r+') as file:
            data = json.load(file)
            hostname = data['values']['hostname']
            username = data['values']['username']
            password = data['values']['password']
            database = data['values']['database']
        return (hostname, username, password, database)
    
    def toText(self, event):
        number = self.stringVar_rupeesNo.get()
        self.rupeesTxtE.delete(0, END)
        numText = str(wordGen.say_number(int(number)))
        self.rupeesTxtE.insert(0, numText)

    def changedetector(self, event):
        etc = self.stringVar_accHead.get()
        if etc == "Other":
            self.accHeadOE.config(state="normal")
            self.accHeadOE.focus_set()
        else:
            self.accHeadOE.config(state="disabled")
            self.paidToE.focus_set()

    def getVoucherNo(self):
        dbApp = initialize.RecieptDatabase(self.dbConnStatics[0], self.dbConnStatics[1], self.dbConnStatics[2], self.dbConnStatics[3])
        d = dbApp.getLastVoucher()
        return d

    def setVoucherNo(self):
        voucherNo = int(self.getVoucherNo())
        voucherNo = voucherNo + 1
        self.topBannerVoucherE.config(state="normal")
        self.topBannerVoucherE.delete(0, END)
        self.topBannerVoucherE.insert(0, voucherNo)
        self.topBannerVoucherE.config(state="disabled")
        self.voucherNoE.delete(0, END)
        self.voucherNoE.insert(0, voucherNo)

    def fetchData(self):
        _data_voucherNo = self.stringVar_voucherNoS.get()
        _data_accHeadT = self.stringVar_accHead.get()
        if _data_accHeadT == "Other": 
            _data_accHead = self.stringVar_accHeadO.get();
            listUpdater.update(_data_accHead)
        else: 
            _data_accHead = self.stringVar_accHead.get()
        _data_paidTo = self.stringVar_paidTo.get()
        _data_rupeesNo = self.stringVar_rupeesNo.get()
        _data_rupeesTxt= self.stringVar_rupeesTxt.get()
        _data_accountOf = self.stringVar_accountOf.get()
        _data_byCCNo = self.stringVar_byCCNo.get()
        _data_bankAccNo = self.stringVar_bankAccNo.get()

        return (_data_voucherNo, _data_accHead, _data_paidTo, _data_rupeesNo, _data_rupeesTxt, _data_accountOf, _data_byCCNo, _data_bankAccNo)

    def save(self):
        data = self.fetchData()
        dbApp = initialize.RecieptDatabase(self.dbConnStatics[0], self.dbConnStatics[1], self.dbConnStatics[2], self.dbConnStatics[3])
        self.oldID = data[0]
        result = dbApp._insert(
            data[0],
            data[1],
            data[2],
            data[3],
            data[4],
            data[5],
            data[6],
            data[7]
        )
        
        if result:
            self.clear()
            self.setVoucherNo()
            self.loadList()
        else:
            messagebox.showerror("Insert Error", "Something Went Wrong")


    def clear(self):
        self.topBannerVoucherE.config(state="normal")
        self.topBannerVoucherE.delete(0, END)
        self.topBannerVoucherE.config(state="disabled")
        self.voucherNoE.delete(0, END)
        self.stringVar_accHead.set("Select")
        self.accHeadOE.config(state="normal")
        self.accHeadOE.delete(0, END) 
        self.accHeadOE.config(state="disabled")
        self.paidToE.delete(0, END)
        self.rupeesNoE.delete(0, END)
        self.rupeesTxtE.delete(0, END)
        self.accountOfE.delete(0, END)
        self.byCCNoE.delete(0, END)
        self.bankAccNoE.delete(0, END)
        self.onDateE.config(state="normal")
        self.onDateE.delete(0, END) 
        self.onDateE.config(state="disabled")
        self.setVoucherNo()
        self.loadList()
        

    def load(self, voucherNo=None):
        if voucherNo is None:
            voucherNo = int(self.stringVar_voucherNoS.get())
        # voucherNo = int(self.stringVar_voucherNoS.get())
        dbApp = initialize.RecieptDatabase(self.dbConnStatics[0], self.dbConnStatics[1], self.dbConnStatics[2], self.dbConnStatics[3])
        data = dbApp._fetch(voucherNo)
        self.loadList()

        if data==False:
            messagebox.showerror("Error", "No Data Found")
        else:
            self.clear()
            self.topBannerVoucherE.config(state="normal")
            self.topBannerVoucherE.delete(0, END)
            self.topBannerVoucherE.insert(0, data[1])
            self.topBannerVoucherE.config(state="disabled")
            self.voucherNoE.delete(0, END)
            self.voucherNoE.insert(0, data[1])
            self.stringVar_accHead.set(data[2])
            self.paidToE.insert(0, data[3])
            self.rupeesNoE.insert(0, data[4])
            self.rupeesTxtE.insert(0, data[5])
            self.accountOfE.insert(0, data[6])
            self.byCCNoE.insert(0, data[7])
            self.bankAccNoE.insert(0, data[8])
            self.onDateE.config(state="normal")
            self.onDateE.insert(0, data[9])
            self.onDateE.config(state="disabled")

    def new(self):
        self.loadList()
        self.clear()
        self.setVoucherNo()

    def loadandprint(self):
        self.load()
        _data_voucherNo = self.stringVar_voucherNoS.get()
        _data_accHeadT = self.stringVar_accHead.get()
        if _data_accHeadT == "Other": 
            _data_accHead = self.stringVar_accHeadO.get();
            listUpdater.update(_data_accHead)
        else: 
            _data_accHead = self.stringVar_accHead.get()
        _data_paidTo = self.stringVar_paidTo.get()
        _data_rupeesNo = self.stringVar_rupeesNo.get()
        _data_rupeesTxt= self.stringVar_rupeesTxt.get()
        _data_accountOf = self.stringVar_accountOf.get()
        _data_byCCNo = self.stringVar_byCCNo.get()
        _data_bankAccNo = self.stringVar_bankAccNo.get()
        _data_onDate = self.stringVar_onDate.get()
        printConn = printer.Printer(_data_voucherNo, _data_accHead, _data_paidTo, _data_rupeesNo, _data_rupeesTxt, _data_accountOf, _data_byCCNo, _data_bankAccNo, _data_onDate)
        printConn.startPrinting()

    def saveandprint(self):
        self.save()
        lastVoucher = int(self.getVoucherNo())
        self.load(lastVoucher)
        _data_voucherNo = self.stringVar_voucherNoS.get()
        _data_accHeadT = self.stringVar_accHead.get()
        if _data_accHeadT == "Other": 
            _data_accHead = self.stringVar_accHeadO.get();
            listUpdater.update(_data_accHead)
        else: 
            _data_accHead = self.stringVar_accHead.get()
        _data_paidTo = self.stringVar_paidTo.get()
        _data_rupeesNo = self.stringVar_rupeesNo.get()
        _data_rupeesTxt= self.stringVar_rupeesTxt.get()
        _data_accountOf = self.stringVar_accountOf.get()
        _data_byCCNo = self.stringVar_byCCNo.get()
        _data_bankAccNo = self.stringVar_bankAccNo.get()
        _data_onDate = self.stringVar_onDate.get()
        printConn = printer.Printer(_data_voucherNo, _data_accHead, _data_paidTo, _data_rupeesNo, _data_rupeesTxt, _data_accountOf, _data_byCCNo, _data_bankAccNo, _data_onDate)
        printConn.startPrinting()
        self.new()
    
    def getCurrTime(self):
        now = datetime.datetime.now()
        curr = now.strftime("%d/%m/%Y %H:%M:%S")
        return str(curr)
        

if __name__ == '__main__':
    root = Tk()
    root.title("Voucher Generator JC")
    root.geometry("870x500")
    App(root)
    root.mainloop()
