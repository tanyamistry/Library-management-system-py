from tkinter import *
class LibraryManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")


        lbltitle=Label(self.root,text="Library Management System",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)




if __name__ == "__main__":
    root= Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()