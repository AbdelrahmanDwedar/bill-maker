import json
from tkinter import *

count = 1
window = Tk()
window.title("system")
window.geometry("350x200+500+350")
window.configure(background="#f5f5f5")
window.resizable(width=False, height=False)  # unresizable


#! makes a json file that
class create_file:
    def __init__(self):
        self.window_file = Toplevel(window)
        self.window_file.title("Create Custom File")
        self.window_file.geometry("300x300")
        self.data_file_name = Entry(self.window_file, width=23)
        self.data_file_name.place(x=15, y=40)

        self.cfile = Button(self.window_file, text="Creat your own file", command=self.addFile)
        self.cfile.place(x=15, y=80)

        self.sfile = Button(self.window_file, text="Set this as the working file", command=self.setFile)
        self.sfile.place(x=15, y=130)

    # * makes a new json file
    def addFile(self):
        di = {}
        global text
        text = self.data_file_name.get()

        with open("%s.json" % text, "w") as write: # type: ignore
            json.dump(di, write)

    # * sets a json file to use
    def setFile(self):
        global text
        text = self.data_file_name.get()

        open("%s.json" % text)



#! adds a value to the json file
class addWindow:
    def __init__(self):
        self.adding_window = Toplevel(window)
        self.adding_window.title("Add Goods")
        self.adding_window.geometry("700x300+0+0")

        self.key_lab = Label(self.adding_window, text="Enter code")
        self.key = Entry(self.adding_window, width=23)
        self.key.place(x=15, y=40)
        self.key_lab.place(x=15, y=20)

        self.pro_lab = Label(self.adding_window, text="Name of product")
        self.pro = Entry(self.adding_window, width=23)
        self.pro.place(x=170, y=40)
        self.pro_lab.place(x=170, y=20)

        self.price_lab = Label(self.adding_window, text="Enter price")
        self.price = Entry(self.adding_window, width=23)
        self.price.place(x=330, y=40)
        self.price_lab.place(x=330, y=20)

        self.num_lab = Label(self.adding_window, text="Enter Quantity")
        self.num = Entry(self.adding_window, width=23)
        self.num.place(x=480, y=40)
        self.num_lab.place(x=480, y=20)

        self.btn5 = Button(self.adding_window, text="add", command=self.addWindow)
        self.btn5.place(x=15, y=60)

    # * Adds a list to the json file
    def addWindow(self):
        dic = {}

        # ? If you have made a custom json file
        try:
            json_val = json.load(open("%s.json" % text, "r"))
            dic = json_val
            dic[self.key.get()] = [self.pro.get(), self.price.get(), self.num.get()]

            with open("%s.json" % text, "w") as write:
                json.dump(dic, write)

        # ? If you didn't set a custom file, uses 'data.json' as the main json file
        except NameError:
            json_val = json.load(open("data.json", "r"))
            dic = json_val
            dic[self.key.get()] = [self.pro.get(), self.price.get(), self.num.get()]

            with open("data.json", "w") as write:
                json.dump(dic, write)

        self.lab = Label(self.adding_window, text=dic, width=40)
        self.lab.place(x=15, y=100)



#! gets and calculats the prices and total
class calcWindow:
    def __init__(self):
        self.calc_window = Toplevel(window)
        self.calc_window.title("Buying")
        self.calc_window.geometry("700x300+0+350")
        self.key_var = StringVar()
        self.pro_var = StringVar()
        self.price_var = StringVar()
        self.num_var = IntVar()

        self.key_lab = Label(self.calc_window, text="Enter code")
        self.key = Entry(self.calc_window, width=23, textvariable=self.key_var)
        self.key.place(x=15, y=40)
        self.key_lab.place(x=15, y=20)

        self.pro_lab = Label(self.calc_window, text="Name of product")
        self.pro = Entry(self.calc_window, width=23, textvariable=self.pro_var)
        self.pro.place(x=170, y=40)
        self.pro_lab.place(x=170, y=20)

        self.price_lab = Label(self.calc_window, text="price")
        self.price = Entry(self.calc_window, width=23, textvariable=self.price_var)
        self.price.place(x=330, y=40)
        self.price_lab.place(x=330, y=20)

        self.num_lab = Label(self.calc_window, text="Enter Quantity")
        self.num = Entry(self.calc_window, width=23, textvariable=self.num_var)
        self.num.place(x=480, y=40)
        self.num_lab.place(x=480, y=20)

        self.label1 = Listbox(self.calc_window)
        self.label1.place(x=15, y=100)
        self.label2 = Listbox(self.calc_window)
        self.label2.place(x=100, y=100)

        btn5 = Button(self.calc_window, text="search", command=self.search)
        btn5.place(x=15, y=60)

        btn6 = Button(self.calc_window, text="add", command=self.calc)
        btn6.place(x=100, y=60)

        btn7 = Button(self.calc_window, text="total", command=self.total)
        btn7.place(x=150, y=60)


    def search(self):
        dic = {}

        # ? If you have made a custom json file
        try:
            json_val = json.load(open("%s.json" % text))
            dic = json_val
            k = self.key_var.get()
            for x in dic.keys():
                if x == k:
                    self.pro_var.set(dic[x][0])
                    self.price_var.set(dic[x][1])
                    self.num_var.set(1)
        # ? If you didn't set a custom file, uses 'data.json' as the main json file
        except NameError:
            json_val = json.load(open("data.json"))
            dic = json_val
            k = self.key_var.get()
            for x in dic.keys():
                if x == k:
                    self.pro_var.set(dic[x][0])
                    self.price_var.set(dic[x][1])
                    self.num_var.set(1)

    def calc(self):
        global count
        p = float(self.price_var.get())
        n = float(self.num_var.get())
        name = self.pro_var.get()
        t = p * n

        try:
            json_val = json.load(open("%s.json" % text))
        except NameError:
            json_val = json.load(open("data.json"))

        dic = json_val
        number = dic[self.key_var.get()][2]
        numy = int(number) - int(n)

        if numy >= 0:
            self.label1.insert(count, name)
            self.label2.insert(count, t)
            count += 1
            dic = {}

            # ? If you have made a custom json file
            try:
                json_val = json.load(open("%s.json" % text))
                dic = json_val
                dic[self.key.get()][2] = numy

                with open("%s.json" % text, "w") as write:
                    json.dump(dic, write)
            # ? If you didn't set a custom file, uses 'data.json' as the main json file
            except:
                json_val = json.load(open("data.json"))
                dic = json_val
                dic[self.key.get()][2] = numy

                with open("data.json", "w") as write:
                    json.dump(dic, write)
        else:
            reject_label = Label(self.calc_window, text=f"Sorry sir, we're out of {name}.")
            reject_label.place(x=480, y=60)

    def total(self):
        tot = 0
        y = 0
        for x in range(count - 1):
            y = self.label2.get(x)
            tot += int(y)
        to = count + 1
        self.label1.insert(to, "Totally")
        self.label2.insert(to, y) if y else print("the price is not passed")


# * system buttons
btn1 = Button(window, text="Buying", width=15, command=calcWindow)
btn1.place(x=110, y=20)

btn2 = Button(window, text="Add goods", width=15, command=addWindow)
btn2.place(x=110, y=70)

btn3 = Button(window, text="Create custom file", width=15, command=create_file)
btn3.place(x=110, y=120)

if __name__ == "__main__":
    window.mainloop()
