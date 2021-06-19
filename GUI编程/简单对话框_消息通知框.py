"""简单对话框"""

from tkinter.simpledialog import *
root = Tk()
root.geometry("400x100")


def test1():
    a = askinteger(title="输入年龄", prompt="请输入年龄", initialvalue=18, minvalue=1, maxvalue=150)
    # askstring, sakfloat框使用方式一样
    show["text"] = a


Button(root, text="老唐你多大了？请输入", command=test1).pack()


show = Label(root, width=40, height=3, bg="green")
show.pack()

root.mainloop()
