'''这是一个音乐播放器的简单构造程序，
该程序利用GUI编程以及数据库编程综合完成，
实现了音乐播放器的导入音乐，删除音乐，播放音乐

以下是播放器的主线程序'''
from Myserver import MyServer
import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilenames
from tkinter.messagebox import *

class PlayWindow():
    """
    PlayWindow类用于创建一个音乐播放器的窗口界面。

    该类提供了导入音乐、播放音乐和删除音乐的功能，并通过GUI界面与用户进行交互。
    """
    
    def __init__(self, myServer):
        """
        初始化PlayWindow类的实例。

        :param myServer: 一个MyServer类的实例，用于处理音乐播放相关的数据库操作。
        """
        # 将传入的myServer实例赋值给当前对象的myServer属性，以便在类的其他方法中使用
        self.myServer = myServer
        
    def impMusic(self,even):
        """
        处理导入音乐的事件。

        :param even: 触发事件的对象。
        """
        #print('导入音乐')
        # 打开磁盘选择音乐
        files = askopenfilenames(filetypes=(['mp3', "*.mp3"],))
        self.myServer.add_music(files)
        self.flash_list()
    def playMusic(self,even):
        """
        处理播放音乐的事件。

        :param even: 触发事件的对象。
        """
        #print('播放音乐')
        # 获取当前选中的音乐索引
        index=self.listbox.curselection()
        # 获取当前选中的音乐名称
        music_name=self.listbox.get(index)
        # 调用myServer的playMusic方法播放音乐
        self.myServer.playMusic(music_name)
        
    def delMusic(self,even):
        """
        处理删除音乐的事件。

        :param even: 触发事件的对象。
        """
        #print('删除音乐')
        # 获取当前选中的音乐索引
        index=self.listbox.curselection()
        # 获取当前选中的音乐名称
        music_name=self.listbox.get(index)
        # 调用myServer的delet_music方法删除音乐
        self.myServer.delet_music(music_name)
        # 刷新音乐列表
        self.flash_list()
    def flash_list(self):
        """
        刷新音乐列表。
        """
        #清空列表
        self.listbox.delete(0,tkinter.END)
        music_list=self.myServer.findListByUser()
        #查询该用户的所有音乐列表
        if music_list:
            for m in music_list:
                self.listbox.insert(tkinter.END,m)
    def showWindow(self):
        """
        显示音乐播放器窗口。

        该方法创建并显示一个包含播放、导入音乐和删除按钮以及音乐列表的窗口。
        """
        # 显示窗口
        top=tkinter.Tk()
        #top.geometry('200x300')
        # 添加按钮
        play_button=tkinter.Button(top,text='播放')
        imp_button=tkinter.Button(top,text='导入音乐')
        delete_button=tkinter.Button(top,text='删除')
        play_button.grid(row=0,column=0,padx=5,pady=5)
        imp_button.grid(row=0,column=2,padx=5,pady=5)
        delete_button.grid(row=0,column=4,padx=5,pady=5)
        # 添加列表
        self.listbox=tkinter.Listbox(top)
        self.listbox.grid(row=2,column=0,padx=5,pady=5,columnspan=9)
        # 给按钮添加点击事件
        imp_button.bind('<ButtonRelease-1>',self.impMusic)
        play_button.bind('<ButtonRelease-1>',self.playMusic)
        delete_button.bind('<ButtonRelease-1>',self.delMusic)
        self.flash_list()
        top.mainloop()

class logWay(Frame):
    def __init__(self, master = None):
        """
        初始化logWay类的实例。

        :param master: 父窗口对象，默认为None。
        """
        # 调用父类的构造函数，初始化父类的属性
        super().__init__(master)
        # 将传入的master实例赋值给当前对象的master属性，以便在类的其他方法中使用
        self.master=master
        # 将当前对象添加到父窗口中
        self.pack()
        # 调用createWidth方法创建窗口部件
        self.createWidth()
    def createWidth(self):
        """
        创建窗口部件。

        该方法用于创建并布局窗口中的各个部件，如标签、输入框和按钮。
        """
        # 创建用户名标签
        self.Lobel101=Label(self,text='用户名')
        # 将用户名标签添加到窗口中
        self.Lobel101.pack()
        # 创建用户名输入框
        v1=StringVar()
        self.entry01=Entry(self,textvariable=v1)
        # 将用户名输入框添加到窗口中
        self.entry01.pack()
        # 设置用户名输入框的默认值
        v1.set('admin')
        # 创建密码标签
        self.Lobel102=Label(self,text='密码')
        # 将密码标签添加到窗口中
        self.Lobel102.pack()
        # 创建密码输入框
        v2=StringVar()
        self.entry02=Entry(self,textvariable=v2,show='*')
        # 将密码输入框添加到窗口中
        self.entry02.pack()
        # 设置密码输入框的默认值
        v2.set('密码')
        # 创建登录按钮
        Button(self,text='登录',command=self.login).pack()

    def login(self):
        """
        处理登录按钮的点击事件。

        该方法获取用户名和密码输入框中的值，并调用close方法关闭窗口。
        """
        # 获取用户名输入框中的值
        self.username=self.entry01.get()
        # 获取密码输入框中的值
        self.password=self.entry02.get()
        # 调用close方法关闭窗口
        self.close()

    def close(self):
        """
        关闭窗口。

        该方法销毁当前窗口。
        """
        # 销毁当前窗口
        self.master.destroy()
    
class CreateTk():
    def creattk(self):
        """
        创建主窗口。

        该方法创建并显示一个包含登录界面的主窗口。
        """
        # 创建主窗口
        root=Tk() 
        # 设置主窗口的大小
        root.geometry('300x400')
        # 创建logWay类的实例
        app=logWay(master=root)
        # 进入主窗口的事件循环
        root.mainloop() 
        # 获取用户名
        self.username=app.username
        # 获取密码
        self.password=app.password      
    def win_screen(self):
        """
        显示登录成功的提示信息。

        该方法弹出一个提示框，显示登录成功的信息。
        """
        # 弹出提示框，显示登录成功的信息
        showinfo(title='登录成功',message='登录成功')
    def wrong_screen(self):
        """
        显示登录失败的提示信息。

        该方法弹出一个提示框，显示登录失败的信息。
        """
        # 弹出提示框，显示登录失败的信息
        a1=showinfo(title='登录失败',message='登录失败')
if __name__=='__main__':
    try:
        while True:
            # 创建CreateTk类的实例
            createtk=CreateTk()
            # 调用creattk方法创建主窗口
            createtk.creattk()
            # 获取用户名
            uname=createtk.username
            # 获取密码
            passward=createtk.password
            # 创建MyServer类的实例
            myserver=MyServer()
            # 调用log方法验证用户名和密码
            if myserver.log(uname,passward):
                # 打印登录成功的信息
                print('登录成功')
                # 调用win_screen方法显示登录成功的提示信息
                createtk.win_screen()
                # 创建PlayWindow类的实例
                playWindow=PlayWindow(myserver)
                # 调用showWindow方法显示音乐播放器
                playWindow.showWindow()
                break
            else:
                # 打印登录失败的信息
                print('登录失败')
                # 调用wrong_screen方法显示登录失败的提示信息
                createtk.wrong_screen()
                
    except Exception as e:
        print(e)
        with open('log.txt','a') as f:
            f.write(str(e))
            f.write('\n')
        
        
        
    

