from tkinter import *
from tkinter import ttk

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-do-list')
        self.root.geometry('650x410+300+150')
        self.label = Label(self.root, text='To-Do-list-App',
                           font='arial 25 bold', width=10, bd=5, bg='pink', fg='blue')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add Task',
                           font='arial 18 bold', width=10, bd=5, bg='light green', fg='maroon')
        self.label2.place(x=440, y=54)

        self.label3 = Label(self.root, text='Tasks',
                           font='arial 18 bold', width=10, bd=5, bg='light green', fg='maroon')
        self.label3.place(x=900, y=54)

        self.main_text=Listbox(self.root,width=30,height=20,bd=5,fg="grey",font="arial 20 italic bold")
        self.main_text.place(x=900,y=100)

        self.main_text2=Text(self.root,width=30,height=5,fg="grey",font="arial 20 italic bold")
        self.main_text2.place(x=180,y=100)
        #-------------add task------------
        def add():
            content=self.main_text2.get(1.0,END)
            self.main_text.insert(END,content)
            with open('data.txt','a') as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.main_text2.delete(1.0,END)

        def delete():
            delete_=self.main_text.curselection()
            look=self.main_text.get(delete_)
            with open('data.txt','r+') as f:
                new_f=f.readlines()
                f.seek(0)
                for line in new_f:
                    item=str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)
        with open('data.txt','r') as file:
            read=file.readlines()
            for i in read:
                ready=i.split()
                self.main_text.insert(END,ready)
            file.close()

        self.button=Button(self.root,text="Add",font='arial, 20 bold italic',width=10,bd=5,bg='pink',fg='blue',command=add)
        self.button.place(x=240,y=300)
        self.button2=Button(self.root,text="Delete",font='arial, 20 bold italic',width=10,bd=5,bg='pink',fg='blue',command=delete)
        self.button2.place(x=240,y=600)

def main():
    root = Tk()
    ui = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
