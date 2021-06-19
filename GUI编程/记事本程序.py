# coding=
"""��дһ�����±�����"""


from tkinter.filedialog import *
from tkinter import *


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)            # super()������Ǹ���Ķ�������Ǹ������
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # �������˵���
        menuber = Menu(root)

        # �����Ӳ˵�
        menuFlie = Menu(menuber)
        menuEdit = Menu(menuber)
        menuHelp = Menu(menuber)

        # ���Ӳ˵����뵽���˵���
        menuber.add_cascade(label="�ļ�(F)", menu=menuFlie)
        menuber.add_cascade(label="�༭(E)", menu=menuEdit)
        menuber.add_cascade(label="����(H)", menu=menuHelp)

        # ��Ӳ˵���
        menuFlie.add_command(label="�½�", accelerator="ctrl+n", command=self.test)
        menuFlie.add_command(label="��", accelerator="ctrl+o", command=self.openfile)
        menuFlie.add_command(label="����", accelerator="ctrl+s", command=self.savefile)
        menuFlie.add_separator()    # ��ӷָ���
        menuFlie.add_command(label="�˳�", accelerator="ctrl+q", command=self.exit)

        # �����˵����ӵ�������
        root["menu"] = menuber

        # �ı��༭��
        self.textpad = Text(root, width=50, height=30)
        self.textpad.pack()

        # �������²˵�
        self.contextMenu = Menu(root)
        self.contextMenu.add_command(label="������ɫ", command=self.test)

        # Ϊ�Ҽ����¼�
        root.bind("<Button-3>", self.createContextMenu)

    def openfile(self):
        self.textpad.delete("1.0", "end")       # ��text�ؼ������е��������
        with askopenfile(title="���ı��ļ�") as f:
            # print(f.read())
            self.textpad.insert(INSERT, f.read())
            self.filename = f.name

    def savefile(self):
        with open(self.filename, "W") as f:
            c = self.textpad(1.0, END)
            f.write(c)

    def exit(self):
        root.quit()

    def test(self):
        pass

    def createContextMenu(self, event):
        # �˵�������Ҽ����������괦��ʾ
        self.contextMenu.post(event.x_root, event.y_root)


if __name__ == "__main__":
    root = Tk()
    root.title("���±�")
    root.geometry("400x300+200+300")
    app = Application(master=root)
    root.mainloop()

















