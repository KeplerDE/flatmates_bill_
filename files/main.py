import webbrowser

from fpdf import FPDF
from flat import Bill, Flatmate


class PdfReport:
    """
    Create PDF File that contains data about
    the flatmates such as their names, their due amounts
    and the period of the bill

    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):  # pip ins. fpdf

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', )  # CTRL + Q - Fetch docus
        pdf.add_page()

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align="C", ln=1)

        # Insert Period label and value
        pdf.cell(w=100, h=40, txt="Period", border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=40, txt=flatmate1_pay, border=1, ln=1)

        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=40, txt=flatmate2_pay, border=1, ln=1)

        # Add img
        pdf.image("house.png", w=30, h=30)
        # Change pdf Font
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        pdf.output(self.filename)




amount = float(input("Привет пользователь,введи количество дней: "))
period = input("За какой период рассчитать коммунальные услуги? ")

name1 = input("Введите ваше имя: ")
days_in_house1 = int(input(f"Сколько дней Вы {name1} оставались дома? "))

name2 = input("Введите ваше имя: ")
days_in_house2 = int(input(f"Сколько дней Вы {name2} оставались дома? "))

the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{flatmate1.name} pays: ", flatmate1.pays(the_bill, flatmate2))
print(f"{flatmate2.name} pays: ", flatmate2.pays(the_bill, flatmate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)

# в итоге можно сделать интерфейс: десктоп, веб, консоль
