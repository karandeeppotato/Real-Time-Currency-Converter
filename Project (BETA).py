import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk
#import json

class CurrConv():
    def __init__(self,url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']
        
    def convert(self, from_currency, to_currency, converted_currency):
        initial_amount = converted_currency
        if from_currency != 'USD' :
            converted_currency = converted_currency / self.currencies[from_currency]
            #converted_currency = converted_currency * self.currencies[to_currency]
            #print(converted_currency)
            
        #rounding off the result to 4 decimal places
        converted_currency = round(converted_currency * self.currencies[to_currency], 4)
        return converted_currency
class UI(tk.Tk):
    def __init__(self,application ):
        tk.Tk.__init__(self)
        self.winfo_toplevel().title('Real-time Currency converter') 
        self.currency_converter = application
        self.configure(background = '#4587DB')
        self.geometry("700x400")
    #label
        self.intro_label = Label(self, text = 'Python based Real-time Currency Converter' ,  fg = 'black', relief = tk.RAISED, borderwidth = 6)
        self.intro_label.config(font = ('Comic Sans MS',15,'bold','italic'))
        self.intro_label.place(x = 130 , y= 20)
        self.date_label = Label(self, text = f"1 INR = {self.currency_converter.convert('INR','USD',1)}  USD \n Date : {self.currency_converter.data['date']}", relief = tk.GROOVE, borderwidth = 2)
        self.date_label.place(x = 292, y= 120)
    #Entry box
        valid = (self.register(self.restrictednum), '%d', '%P')
        self.amount_field = Entry(self,bd = 3, relief = tk.RIDGE, justify = tk.CENTER,validate='key', validatecommand=valid)
        self.amount_field.place(x = 120, y = 200)
        self.converted_amount_field_label = Label(self, text = '', fg = 'black', bg = 'white', relief = tk.RIDGE, justify = tk.CENTER, width = 17, borderwidth = 3)
        self.converted_amount_field_label.place(x = 450, y = 200)
   #Dropdown
        self.from_currency_var = StringVar(self)   
        self.from_currency_var.set("USD")
        self.to_currency_var = StringVar(self)
        self.to_currency_var.set("INR")
        
        font = ("Courier", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_var,values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 12, justify = tk.CENTER)
        self.from_currency_dropdown.place(x = 112, y= 230)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_var,values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 12, justify = tk.CENTER)
        self.to_currency_dropdown.place(x = 442, y= 230)
           
    #Convert button
        self.convert_button = Button(self,text = "Press to Convert", fg ="black", command = self.perform)
        self.convert_button.config(font=('Courier' , 10 , 'bold'))
        self.convert_button.place(x = 282 , y=225)
        
    
  
    
    def perform(self):
        converted_currency = float(self.amount_field.get())
        from_curr = self.from_currency_var.get()
        to_curr = self.to_currency_var.get()
            
        converted_amt = self.currency_converter.convert(from_curr,to_curr,converted_currency)
        self.converted_amount_field_label.config(text = str(converted_amt))
             
    def restrictednum(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))
if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    application = CurrConv(url) #CurrConv --> Backend class of the application
   # print(CurrConv(url).convert('INR','USD',1))
    
    UI(application) #App --> Class for managing GUI
    mainloop()