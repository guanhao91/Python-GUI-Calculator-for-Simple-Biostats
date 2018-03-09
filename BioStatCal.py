# We need to install python module 'tkinter', 'pandas', and 'scipy' first.
from tkinter import *
from tkinter import messagebox as tkMB
import pandas as pd
from scipy import stats
from statsmodels.formula.api import ols

def calc():
    try:

        # Pearson's correlation
        if oper.get() == 'Pearson' or oper.get() == 'P':
            try:
                df = pd.read_csv(file.get())
                dff = df[[num1.get(), num2.get()]]
                cov = dff.corr()
                value = cov[num1.get()][num2.get()]
                answer = Label(app, text='Pearson Correlation is:')
                answer.grid(row=7, column=0, sticky=SW)
                answer2 = Label(app, text=value)
                answer2.grid(row=8, column=0, sticky=S)
            except:
                tkMB.showerror("Pearson Correlation Error!", 'Something went wrong! Maybe invalid entries')

        # Spearman's correlation
        if oper.get() == 'Spearman' or oper.get() == 'S':
            try:
                df = pd.read_csv(file.get())
                dff = df[[num1.get(), num2.get()]]
                cov = dff.corr(method='spearman')
                value = cov[num1.get()][num2.get()]
                answer = Label(app, text='Spearman Correlation is:')
                answer.grid(row=9, column=0, sticky=SW)
                answer2 = Label(app, text=value)
                answer2.grid(row=10, column=0, sticky=S)
            except:
                tkMB.showerror("Spearman Correlation Error!", 'Something went wrong! Maybe invalid entries')

        # Two sample T test for mean difference
        if oper.get() == 'T test' or oper.get() == 'T':
            try:
                df = pd.read_csv(file.get())
                t,p = stats.ttest_ind(df[num1.get()], df[num2.get()])
                t1 = "{0:.3f}".format(t)
                p1 = "{0:.3f}".format(p)
                answer = Label(app, text='T test result is:')
                answer.grid(row=11, column=0, sticky=SW)
                answer2 = Label(app, text='{0} = {1}, {2} = {3}'.format('T stat', t1, 'P-value', p1))
                answer2.grid(row=12, column=0, sticky=S)

            except:
                tkMB.showerror("T test Error!", 'Something went wrong! Maybe invalid entries')

        # Two sample Wilcoxon Mann Whitney test
        if oper.get() == 'Wilcoxon' or oper.get() == 'W':
            try:
                df = pd.read_csv(file.get())
                w, p = stats.mannwhitneyu(df[num1.get()], df[num2.get()])
                w1 = "{0:.3f}".format(w)
                p1 = "{0:.3f}".format(p)
                answer = Label(app, text='Wilcoxon Mann-Whitney test result is:')
                answer.grid(row=13, column=0, sticky=SW)
                answer2 = Label(app, text='{0} = {1}, {2} = {3}'.format('MW-U stat', w1, 'P-value', p1))
                answer2.grid(row=14, column=0, sticky=S)
            except:
                tkMB.showerror("Wilcoxon test Error!", 'Something went wrong! Maybe invalid entries')

        # Multivariate Linear Regression Model
        if oper.get() == 'Regression' or oper.get() == 'R':
            try:
                df = pd.read_csv(file.get())
                y = df[num3.get()]
                s = str.split(num4.get(), ',')
                x = df[s]
                model = ols("y ~ x", df).fit()
                para = model.params
                func = num3.get() + '=' + "{0:.3f}".format(para[0])
                for i in range(len(para)-1):
                    temp = float("{0:.3f}".format(para[i+1]))
                    if temp > 0:
                        func = func + '+' + str(temp) + s[i]
                    else:
                        func = func + str(temp) + s[i]
                answer = Label(app, text='OLS Regression Model is:')
                answer.grid(row=15, column=0, sticky=SW)
                answer2 = Label(app, text=func)
                answer2.grid(row=16, column=0, sticky=S)
            except:
                tkMB.showerror("Regression Error!", 'Something went wrong! Maybe invalid entries')

        str(file)
        str(oper)
        str(num1)
        str(num2)
        str(num3)
        str(num4)

    except:
        tkMB.showerror("Error!", 'Something went wrong! Maybe invalid entries')


global value
value = 0

# Modify window
root = Tk()
root.title('BioStatCalculator by Guanhao Wei')
root.geometry('500x420')
root.resizable(0, 0)

# creating frame
app = Frame(root)
app.pack()

# window attributes below
label1 = Label(app, text='Enter Filename -->')
label1.grid(row=0, column=0, sticky=NW)

label2 = Label(app, text='Enter Procedure -->')
label2.grid(row=1, column=0, sticky=W)

label3 = Label(app, text='Enter variable 1 -->')
label3.grid(row=2, column=0, sticky=W)

label4 = Label(app, text='Enter variable 2 -->')
label4.grid(row=3, column=0, sticky=W)

label5 = Label(app, text='Response variable -->')
label5.grid(row=4, column=0, sticky=W)

label6 = Label(app, text='Predict variables -->')
label6.grid(row=5, column=0, sticky=W)

global file
file = StringVar()
filename = Entry(app, textvariable=file)
filename.grid(row=0, column=1, sticky=NE)

global oper
oper = StringVar()
operator = Entry(app, textvariable=oper)
operator.grid(row=1, column=1, sticky=E)

global num1
num1 = StringVar()
number1 = Entry(app, textvariable=num1)
number1.grid(row=2, column=1, sticky=E)

global num2
num2 = StringVar()
number2 = Entry(app, textvariable=num2)
number2.grid(row=3, column=1, sticky=E)

global num3
num3 = StringVar()
number3 = Entry(app, textvariable=num3)
number3.grid(row=4, column=1, sticky=E)

global num4
num4 = StringVar()
number4 = Entry(app, textvariable=num4)
number4.grid(row=5, column=1, sticky=E)

button = Button(app, text='Calculate', command=calc)
button.grid(row=7, column=1, sticky=SE)

# start main loop
root.mainloop()