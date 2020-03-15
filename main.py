from decimal import *
import random
from datetime import datetime
import tkinter as tk

getcontext().rounding=ROUND_HALF_EVEN

def splitIncome(monthlyIncome, daysInMonth, variance):
    random.seed(datetime.now())
    average = Decimal(monthlyIncome)/Decimal(daysInMonth)
    average = average.quantize(Decimal('.01'))
    roundedVariance = Decimal(variance).quantize(Decimal('.01'))
    dailyIncome = []
    for x in range(daysInMonth-1):
        randChange = float(random.randrange(-100 * roundedVariance, 100 * roundedVariance, 1))/100
        buffer = (average + Decimal(randChange)).quantize(Decimal('.01'))
        dailyIncome.append(buffer)

    incomeSum = 0
    for x in dailyIncome:
        incomeSum += x

    lastday = Decimal(monthlyIncome) - Decimal(incomeSum)
    lastday = lastday.quantize(Decimal('.01'))
    dailyIncome.append(lastday)
    return dailyIncome


def splitButton():
    output.delete("1.0",tk.END)
    bufArr = splitIncome(float(e1.get()), int(e2.get()), float(e3.get()))
    bufStr = ""
    for x in bufArr:
        bufStr += str(x) + "\n"

    output.insert(tk.END, bufStr)    
    # e1.delete(0, tk.END)
    # e2.delete(0, tk.END)
    # e3.delete(0, tk.END)
    



window = tk.Tk() 
window.title("Income Splitter")

tk.Label(window, text="Monatseinkommen").grid(row=0)
tk.Label(window, text="Monatstage").grid(row=1)
tk.Label(window, text="Variance").grid(row=2)


e1 = tk.Entry(window)
e2 = tk.Entry(window)
e3 = tk.Entry(window)
output = tk.Text(window, height=40, width=80)
output.pack()


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
output.grid(row=3, column=1)

tk.Button(
    window, 
    text='Show', 
    command=splitButton).grid(row=2, column=2, sticky=tk.W, pady=4)


window.mainloop()



