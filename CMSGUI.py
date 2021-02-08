import CMSusingOops
from tkinter import *
from tkinter import messagebox


def btnAddCust_Click():
    ob = CMSusingOops.Customer()
    ob.id = varID.get()
    ob.name = varName.get()
    ob.age = varAge.get()
    ob.addCustomer()
    messagebox.showinfo("CMS", "Customer Added Successfully")
    varID.set("")
    varName.set("")
    varAge.set("")

def btnSearch_Click():
    ob =CMSusingOops.Customer()
    ob.id=varID.get()
    ob.searchCustomer()
   # varName.set(ob.name)
    #varAge.set(ob.age)

    root2=Tk()
    lblID3=Label(root2,text="Customer ID",bg="teal",font=1,width=20)
    lblID3.grid(row=0,column=0)

    lblName3 = Label(root2, text="Customer Name", bg="teal", font=1, width=20)
    lblName3.grid(row=1, column=0)

    lblAge3 = Label(root2, text="Customer Age", bg="teal", font=1, width=20)
    lblAge3.grid(row=2, column=0)

    lblID4=Label(root2,text=f"{ob.id}",bg="silver",font=1,width=20)
    lblID4.grid(row=0,column=1)

    lblName4 = Label(root2, text=f"{ob.name}", bg="silver", font=1, width=20)
    lblName4.grid(row=1, column=1)

    lblAge4 = Label(root2, text=f"{ob.age}", bg="silver", font=1, width=20)
    lblAge4.grid(row=2, column=1)

    varID.set("")


def btnDelete_Click():
    ob = CMSusingOops.Customer()
    ob.id=varID.get()
    ob.deleteCustomer()
    messagebox.showinfo("CMS","Customer Deleted Successfully")
    varID.set("")
    varName.set("")
    varAge.set("")


def btnModify_Click():
    ob = CMSusingOops.Customer()
    ob.id=varID.get()
    ob.name=varName.get()
    ob.age = varAge.get()
    ob.modifyCustomer()
    varID.set("")
    varName.set("")
    varAge.set("")

def btnDisplay_Click():
    root1=Tk()
    ldlId1=Label(root1,text="Customer ID",bg="teal",font=1,width=20)
    ldlId1.grid(row=0,column=0)

    ldlName1=Label(root1,text="Customer Name",bg="teal",font=1,width=20)
    ldlName1.grid(row=0,column=1)

    ldlAge1=Label(root1,text="Customer Age",bg="teal",font=1,width=20)
    ldlAge1.grid(row=0,column=2)
    i=1
    for e in CMSusingOops.Customer.cus:
        ldlId2 = Label(root1, text=f"{e.id}", bg="silver", font=1, width=20)
        ldlId2.grid(row=i, column=0)

        ldlName2 = Label(root1, text=f"{e.name}", bg="silver", font=1, width=20)
        ldlName2.grid(row=i, column=1)

        ldlAge2 = Label(root1, text=f"{e.age}", bg="silver", font=1, width=20)
        ldlAge2.grid(row=i, column=2)
        i+=1

def btnSave_Click():
    CMSusingOops.Customer.save()
    messagebox.showinfo("Save","DATA SAVED")

def btnLoad_Click():
    CMSusingOops.Customer.load()
    messagebox.showinfo("Load","DATA LOADED")

def btnExit_Click():
    exit()






root = Tk()
root.geometry("500x400")
root.title("CMS")
lblID = Label(root, text="Enter Customer Id", font=1)
lblID.grid(row=0, column=0)

lblName = Label(root, text="Enter Customer Name", font=1)
lblName.grid(row=1, column=0)

lblAge = Label(root, text="Enter Customer Age", font=1)
lblAge.grid(row=2, column=0)

varID = StringVar()
entrID = Entry(root, textvariable=varID,font=1)
entrID.grid(row=0, column=1)

varName = StringVar()
entrName = Entry(root, textvariable=varName , font=1)
entrName.grid(row=1, column=1)

varAge = StringVar()
entrAge = Entry(root, textvariable=varAge , font=1)
entrAge.grid(row=2, column=1)

btnAddCust = Button(root, text="Add Customer" , font=1, command=btnAddCust_Click, width=20)
btnAddCust.grid(row=4, column=0)

btnSearch = Button(root, text="Search", font=1,command=btnSearch_Click, width=20)
btnSearch.grid(row=4, column=1)

btnDelete = Button(root, text="Delete", font=1,command=btnDelete_Click, width=20)
btnDelete.grid(row=5, column=0)

btnModify = Button(root, text="Modify", font=1,command=btnModify_Click, width=20)
btnModify.grid(row=5, column=1)

btnDisplay=Button(root,text="Display All",command=btnDisplay_Click,width=20,font=1)
btnDisplay.grid(row=6,column=0)

btnSave=Button(root,text="Save",command=btnSave_Click,width=20,font=1)
btnSave.grid(row=6,column=1)

btnLoad=Button(root,text="Load",command=btnLoad_Click,width=20,font=1)
btnLoad.grid(row=7,column=0)

btnExit = Button(root,text="Exit",command=btnExit_Click,width=20,font=1)
btnExit.grid(row=7,column=1)




root.mainloop()
