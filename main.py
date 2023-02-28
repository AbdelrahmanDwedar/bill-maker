import json
from tkinter import *

count = 1
window = Tk()
window.title("system")
window.geometry("350x200+500+350")
window.configure(background="#f5f5f5")
window.resizable(width=False, height=False)  # unresizable


#! makes a json file that
def create_file():
    window_file = Toplevel(window)
    window_file.title("Create Custom File")
    window_file.geometry("300x300")
    data_file_name = Entry(window_file, width=23)
    data_file_name.place(x=15, y=40)

    # * makes a new json file
    def addFile():
        di = {}
        global text
        text = data_file_name.get()

        with open("%s.json" % text, "w") as write:
            json.dump(di, write)

    # * sets a json file to use
    def setFile():
        global text
        text = data_file_name.get()

        open("%s.json" % text)

    cfile = Button(window_file, text="Creat your own file", command=addFile)
    cfile.place(x=15, y=80)

    sfile = Button(window_file, text="Set this as the working file", command=setFile)
    sfile.place(x=15, y=130)


#! adds a value to the json file
def addWindow():
    adding_window = Toplevel(window)
    adding_window.title("Add Goods")
    adding_window.geometry("700x300+0+0")

    # * Adds a list to the json file
    def addWindow():
        dic = {}

        # ? If you have made a custom json file
        try:
            json_val = json.load(open("%s.json" % text))
            dic = json_val
            dic[key.get()] = [pro.get(), price.get(), num.get()]

            with open("%s.json" % text, "w") as write:
                json.dump(dic, write)

        # ? If you didn't set a custom file, uses 'data.json' as the main json file
        except NameError:
            json_val = json.load(open("data.json"))
            dic = json_val
            dic[key.get()] = [pro.get(), price.get(), num.get()]

            with open("data.json", "w") as write:
                json.dump(dic, write)

        lab = Label(adding_window, text=dic, width=40)
        lab.place(x=15, y=100)

    key_lab = Label(adding_window, text="Enter code")
    global key
    key = Entry(adding_window, width=23)
    key.place(x=15, y=40)
    key_lab.place(x=15, y=20)

    pro_lab = Label(adding_window, text="Name of product")
    global pro
    pro = Entry(adding_window, width=23)
    pro.place(x=170, y=40)
    pro_lab.place(x=170, y=20)

    price_lab = Label(adding_window, text="Enter price")
    global price
    price = Entry(adding_window, width=23)
    price.place(x=330, y=40)
    price_lab.place(x=330, y=20)

    num_lab = Label(adding_window, text="Enter Quantity")
    num = Entry(adding_window, width=23)
    num.place(x=480, y=40)
    num_lab.place(x=480, y=20)

    btn5 = Button(adding_window, text="add", command=addWindow)
    btn5.place(x=15, y=60)


#! gets and calculats the prices and total
def calcWindow():
    calc_window = Toplevel(window)
    calc_window.title("Buying")
    calc_window.geometry("700x300+0+350")
    key_var = StringVar()
    pro_var = StringVar()
    price_var = StringVar()
    num_var = IntVar()

    key_lab = Label(calc_window, text="Enter code")
    key = Entry(calc_window, width=23, textvariable=key_var)
    key.place(x=15, y=40)
    key_lab.place(x=15, y=20)

    pro_lab = Label(calc_window, text="Name of product")
    pro = Entry(calc_window, width=23, textvariable=pro_var)
    pro.place(x=170, y=40)
    pro_lab.place(x=170, y=20)

    price_lab = Label(calc_window, text="price")
    price = Entry(calc_window, width=23, textvariable=price_var)
    price.place(x=330, y=40)
    price_lab.place(x=330, y=20)

    num_lab = Label(calc_window, text="Enter Quantity")
    num = Entry(calc_window, width=23, textvariable=num_var)
    num.place(x=480, y=40)
    num_lab.place(x=480, y=20)

    label1 = Listbox(calc_window)
    label1.place(x=15, y=100)
    label2 = Listbox(calc_window)
    label2.place(x=100, y=100)

    def search():
        dic = {}

        # ? If you have made a custom json file
        try:
            json_val = json.load(open("%s.json" % text))
            dic = json_val
            k = key_var.get()
            for x in dic.keys():
                if x == k:
                    pro_var.set(dic[x][0])
                    price_var.set(dic[x][1])
                    num_var.set(1)
        # ? If you didn't set a custom file, uses 'data.json' as the main json file
        except NameError:
            json_val = json.load(open("data.json"))
            dic = json_val
            k = key_var.get()
            for x in dic.keys():
                if x == k:
                    pro_var.set(dic[x][0])
                    price_var.set(dic[x][1])
                    num_var.set(1)

    def calc():
        global count
        p = float(price_var.get())
        n = float(num_var.get())
        name = pro_var.get()
        t = p * n

        try:
            json_val = json.load(open("%s.json" % text))
        except NameError:
            json_val = json.load(open("data.json"))

        dic = json_val
        number = dic[key_var.get()][2]
        numy = int(number) - int(n)

        if numy >= 0:
            label1.insert(count, name)
            label2.insert(count, t)
            count += 1
            dic = {}

            # ? If you have made a custom json file
            try:
                json_val = json.load(open("%s.json" % text))
                dic = json_val
                dic[key.get()][2] = numy

                with open("%s.json" % text, "w") as write:
                    json.dump(dic, write)
            # ? If you didn't set a custom file, uses 'data.json' as the main json file
            except:
                json_val = json.load(open("data.json"))
                dic = json_val
                dic[key.get()][2] = numy

                with open("data.json", "w") as write:
                    json.dump(dic, write)
        else:
            reject_label = Label(calc_window, text=f"Sorry sir, we're out of {name}.")
            reject_label.place(x=480, y=60)

    def total():
        tot = 0
        for x in range(count - 1):
            y = label2.get(x)
            tot += int(y)
        to = count + 1
        label1.insert(to, "Totally")
        label2.insert(to, y) if y else print("the price is not passed")

    btn5 = Button(calc_window, text="search", command=search)
    btn5.place(x=15, y=60)

    btn6 = Button(calc_window, text="add", command=calc)
    btn6.place(x=100, y=60)

    btn7 = Button(calc_window, text="total", command=total)
    btn7.place(x=150, y=60)


# * system buttons
btn1 = Button(window, text="Buying", width=15, command=calcWindow)
btn1.place(x=110, y=20)

btn2 = Button(window, text="Add goods", width=15, command=addWindow)
btn2.place(x=110, y=70)

btn3 = Button(window, text="Create custom file", width=15, command=create_file)
btn3.place(x=110, y=120)

if __name__ == "__main__":
    window.mainloop()
