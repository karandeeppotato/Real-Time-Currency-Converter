
# A REAL TIME CURRENCY CONVERTER GUI PYTHON APP
# Made by Karandeep Singh Sehgal (First year Btech CSE student at Amity University Gurugram)
# and Aayush Chhikara (First year Btech CSE student at Amity University Gurugram)


# Importing all the required libraries 
# Requests --> For acquiring data from https servers
# tkinter --> For the GUI

import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk

# A class which contains the backend of our "REAL TIME CURRENCY CONVERTER"

class CurrConv():
    def __init__(self,url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']
        
    # USD is taken as base currency
    
    def convert(self, from_currency, to_currency, converted_currency):
        initial_amount = converted_currency
        if from_currency != 'USD' :
            converted_currency = converted_currency / self.currencies[from_currency]
           
            
        #rounding off the result to 4 decimal places
        converted_currency = round(converted_currency * self.currencies[to_currency], 4)
        return converted_currency

# A class which contain the Graphical code for our "REAL TIME CURRENCY CONVERTER"

class UI(tk.Tk):
    def __init__(self,application ):
        tk.Tk.__init__(self)
        
        # Setting up the title , size , icon and a beautiful background for our "REAL TIME CURRENCY CONVERTER" window
        
        self.winfo_toplevel().title('Real-time Currency converter') 
        self.currency_converter = application
        self.configure(background = '#012674')
        self.geometry("705x405")
        self.iconbitmap('icon/black_icon.ico')
        self.bg_image = PhotoImage(file="bgimage2.png")
        self.x = Label (image = self.bg_image)
        self.x.grid(row = 20, column = 20)
        
 
    # Setting and placing up the introduction label
       
        self.intro_label = Label(self, text = 'Python based Real-time Currency Converter' ,  fg = 'black', relief = tk.RAISED, borderwidth = 6)
        self.intro_label.config(font = ('Roboto',15,'bold','italic'))
        self.intro_label.place(x = 130 , y= 20)
        
    # Setting and placing up the label which shows the current updated date
        
        self.date_label = Label(self, text = f"1 INR = {self.currency_converter.convert('INR','USD',1)}  USD \n Date : {self.currency_converter.data['date']}", relief = tk.GROOVE, borderwidth = 1)
        self.date_label.place(x = 295, y= 120)
    
    # Creating an entry field and a label
    # Entry field --> in which the user will enter the amount which is to be converted
    # Label --> use to show the converted amount or the result of the conversion
     
        valid = (self.register(self.restrictednum), '%d', '%P')
        self.amount_field = Entry(self,bd = 3, relief = tk.RIDGE, justify = tk.CENTER,validate='key', validatecommand=valid)
        self.amount_field.place(x = 120, y = 200)
        self.converted_amount_field_label = Label(self, text = '', fg = 'black', bg = 'white', relief = tk.RIDGE, justify = tk.CENTER, width = 17, borderwidth = 3)
        self.converted_amount_field_label.place(x = 450, y = 200)
        
   # Creating a Dropdown Menu which shows all the currencies 
   
        self.from_currency_var = StringVar(self)   
        self.from_currency_var.set("USD")
        self.to_currency_var = StringVar(self)
        self.to_currency_var.set("INR")
        
        font = ("Helvetica", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_var,values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 12, justify = tk.CENTER)
        self.from_currency_dropdown.place(x = 117.6, y= 230)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_var,values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 12, justify = tk.CENTER)
        self.to_currency_dropdown.place(x = 448, y= 230)
           
    # Creating a button which when pressed calls out the dothetask method
        
        self.convert_button = Button(self,text = "Press to Convert", fg ="black", command = self.dothetask)
        self.convert_button.config(font=('Courier' , 10 , 'bold'))
        self.convert_button.place(x = 282 , y=199)
        
    # Creating a swapit button which when pressed calls out the swapit method
        
        self.swapit_button = Button(self,text= "Swap Currencies",fg="black",command = self.swapit)
        self.swapit_button.config(font=('Courier' , 10 , 'bold'))
        self.swapit_button.place(x = 285.5 , y=230)
    
    # Swapit method which swaps "from_currency" and "to_currency" 
    
    def swapit(self):
        
        from_temp_swap = self.from_currency_var.get()
        to_temp_swap = self.to_currency_var.get()
        self.from_currency_var.set(to_temp_swap)
        self.to_currency_var.set(from_temp_swap)
        # #debug  pass
    
   # dothetask method which calls out the convert method and prints out the result in the "converted_amount_field_label" 
    
    def dothetask(self):
        converted_currency = float(self.amount_field.get())
        from_curr = self.from_currency_var.get()
        to_curr = self.to_currency_var.get()
            
        converted_amt = self.currency_converter.convert(from_curr,to_curr,converted_currency)
        self.converted_amount_field_label.config(text = str(converted_amt))
             
   # restrictednum method restricts the input of any character which is not a number so as to avoid unexpected errors 
    
    def restrictednum(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))

# Main function

if __name__ == '__main__':
    
   # from which this app gets the updated exchange data
    
   url = 'https://api.exchangerate-api.com/v4/latest/USD' # from which this app gets the updated exchange data
   
   # application here is an instance of CurrConv class
   
   application = CurrConv(url) #CurrConv --> Backend class of the application
   # #debug print(CurrConv(url).convert('INR','USD',1))
    
   UI(application) #App --> Class for managing GUI
   
   mainloop()
   
   # End of the Code
   
   