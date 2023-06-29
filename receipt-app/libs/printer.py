from fpdf import FPDF
import os
import datetime

class Printer():
    def __init__(self, _data_voucherNo, _data_accHead, _data_paidTo, _data_rupeesNo, _data_rupeesTxt, _data_accountOf, _data_byCCNo, _data_bankAccNo, _data_onTime):
        self._voucherNo = _data_voucherNo
        self._accHead = _data_accHead
        self._paidTo = _data_paidTo
        self._rupeesNo = _data_rupeesNo
        self._rupeesTxt = _data_rupeesTxt
        self._accountOf = _data_accountOf
        self._byCCNo = _data_byCCNo
        self._bankAccNo = _data_bankAccNo
        self._onTime = _data_onTime
    
    def startPrinting(self):
        pdf = FPDF('P', 'mm', 'A4')
        pdf.add_page()
        pdf.set_font('Arial', '', 10)
        pdf.cell(w = 190, h = 1, txt="", fill=True, align="C")
        pdf.ln(2)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w = 40, h = 8, txt="Tel : 2545897")
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(w = 110, h = 8, txt="Seva Sadan's", align="C")
        pdf.set_font('Arial', '', 10)
        pdf.cell(w = 40, h = 8, txt=f"Voucher No JC:  {self._voucherNo}")
        pdf.ln(7)
        pdf.set_font('Arial', 'B', 22)
        pdf.cell(w = 190, h = 10, txt="R. K. Talreja College", align="C")
        pdf.ln(8)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w = 190, h = 8, txt="of Arts, Science and Commerce", align="C")
        pdf.ln(5)
        pdf.cell(w = 190, h = 8, txt="ULHASNAGAR - 421 003", align="C")
        pdf.ln(5)
        pdf.set_font('Arial', 'BU', 10)
        pdf.cell(w = 190, h = 8, txt="DEBIT VOUCHER", align="C")

        # Body
        pdf.ln(7)
        pdf.cell(w = 190, h = 1, txt="", fill=True, align="C")
        pdf.set_font('Arial', '', 10)
        pdf.ln(1)
        pdf.set_font('Arial', '', 10)
        pdf.cell(w = 150, h = 8, txt="Date: ", align="R")
        pdf.cell(w = 40, h = 8, txt=self.getCurrentTime(), align="R")
        pdf.ln(7)
        pdf.cell(w = 60, h = 7, txt="Account Head ", border=1)
        pdf.cell(w = 130, h = 7, txt=self._accHead, border=1)

        pdf.ln(7)
        pdf.cell(w = 60, h = 7, txt="Paid To", border=1)
        pdf.cell(w = 130, h = 7, txt=self._paidTo, border=1)

        pdf.ln(7)
        pdf.cell(w = 60, h = 7, txt="Rs (In Number)", border=1)
        pdf.cell(w = 130, h = 7, txt=self._rupeesNo, border=1)

        pdf.ln(7)
        pdf.cell(w = 60, h = 7, txt="Rs (in Text)", border=1)
        pdf.cell(w = 130, h = 7, txt=self._rupeesTxt, border=1)

        pdf.ln(7)
        pdf.cell(w = 60, h = 7, txt="On Account Of", border=1)
        pdf.cell(w = 130, h = 7, txt=self._accountOf, border=1)

        pdf.ln(7)
        pdf.cell(w = 60, h = 7, txt="Type", border=1)
        pdf.cell(w = 130, h = 7, txt=self._byCCNo, border=1)

        pdf.ln(7)
        pdf.cell(w = 60, h = 7, txt="Bank Acc No", border=1)
        pdf.cell(w = 130, h = 7, txt=self._bankAccNo, border=1)

        pdf.ln(7)
        pdf.cell(w = 60, h = 7, txt="Transaction Date", border=1)
        pdf.cell(w = 130, h = 7, txt=self._onTime, border=1)

        # Footer

        pdf.ln(10)
        pdf.cell(w = 190, h = 1, txt="", fill=True, align="C")

        pdf.ln(3)
        pdf.cell(w = 45, h = 8, txt="Sanctioned By", align="C")
        pdf.cell(w = 50, h = 8, txt="Prepared By", align="C")
        pdf.cell(w = 45, h = 8, txt="Checked By", align="C")
        pdf.cell(w = 50, h = 8, txt="Recievers Signature", align="C")

        pdf.ln(3)
        pdf.cell(w = 60, h = 8, txt="", align="C")
        pdf.cell(w = 70, h = 8, txt="", align="C")
        pdf.cell(w = 60, h = 8, txt="", align="C")

        pdf.ln(8)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(w = 45, h = 8, txt="Principal", align="C")
        pdf.set_font('Arial', 'BU', 10)
        pdf.cell(w = 50, h = 8, txt="                                 ", align="C")
        pdf.cell(w = 45, h = 8, txt="                                 ", align="C")
        pdf.cell(w = 50, h = 8, txt="                                 ", align="C")

        pdf.ln(10)
        pdf.cell(w = 190, h = 1, txt="", fill=True, align="C")

        filename = f"{self._voucherNo}.pdf" 
        pdf.output(f'./pdfs/{filename}', 'F')
        # print(os.getcwd())
        filepath = str(os.getcwd()) + str(f"\pdfs\{filename}")
        os.startfile(filepath, "Print")

        # print(self._voucherNo, self._accHead, self._paidTo, self._rupeesNo, self._rupeesTxt, self._accountOf, self._byCCNo, self._bankAccNo, self._onTime)

    def getCurrentTime(self):
        now = datetime.datetime.now()
        curr = now.strftime("%d/%m/%Y %H:%M:%S")
        return str(curr)
