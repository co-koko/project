from dbUtil import dbUtil
import pygame

class MyServer():
    def __init__(self):
        """
        初始化MyServer类的实例。

        该方法初始化了一个MyServer对象，并将其user属性设置为None。
        """
        # 将user属性初始化为None
        self.user=None
    def log(self, uname, password):
        """
        验证用户登录信息。

        :param uname: 用户名。
        :param password: 密码。
        :return: 如果用户名和密码匹配，返回True；否则返回False。
        """
        # 构造查询用户的SQL语句
        sql = 'select * from t_user where uname=%s and password=%s'
        # 调用dbUtil的query_one方法查询用户
        user = dbUtil().query_one(sql, uname, password)
        # 如果查询到用户
        if user:
            # 将查询到的用户信息赋值给当前对象的user属性
            self.user = user
            # 返回True表示登录成功
            return True
        else:
            # 返回False表示登录失败
            return False
    def add_music(self, files):
        """
        添加音乐到数据库。

        :param files: 音乐文件路径列表。
        """
        # 遍历音乐文件路径列表
        for f in files:
            # 获取音乐文件名
            start = f.rfind('/')
            end = f.rfind('.mp3')
            music_name = f[start:end]
            # 构造查询音乐的SQL语句
            sql3 = 'select * from t_music where music_name=%s'
            # 调用dbUtil的query_one方法查询音乐
            music = dbUtil().query_one(sql3, music_name)
            # 如果音乐已存在
            if music:
                # 构造查询音乐列表的SQL语句
                sql = 'select * from t_list where mid=%s and uid=%s'
                # 调用dbUtil()的query_one方法查询音乐列表
                t_list = dbUtil().query_one(sql, music[0], self.user[0])
                # 如果音乐列表中不存在该音乐
                if not t_list:
                    # 构造插入音乐列表的SQL语句
                    sql4 = 'insert into t_list(mid,uid) values(%s,%s)'
                    # 调用dbUtil的exeDML方法插入音乐列表
                    dbUtil().exeDML(sql4, music[0], self.user[0])
            else:
                # 构造插入音乐的SQL语句
                sql = 'insert into  t_music(music_name,path) values(%s,%s)'
                # 调用dbUtil的exeDML方法插入音乐
                mid = dbUtil().exeDML(sql, music_name, f)
                # 构造插入音乐列表的SQL语句
                sql2 = 'insert into t_list(mid,uid) values(%s,%s)'
                # 调用dbUtil的exeDML方法插入音乐列表
                dbUtil().exeDML(sql2, mid, self.user[0])
    def findListByUser(self):
        """
        根据用户ID查询音乐列表。

        :return: 音乐列表。
        """
        # 构造查询音乐列表的SQL语句
        sql = 'SELECT t_music.music_name from t_list t JOIN t_music on t.mid=t_music.id where t.uid=%s'
        # 调用dbUtil的query_all方法查询音乐列表
        return dbUtil().query_all(sql, self.user[0])
    def delet_music(self, music_name):
        """
        删除音乐。

        :param music_name: 音乐名称。
        """
        # 构造查询音乐ID的SQL语句
        sql2 = 'select id from from t_music where music_name=%s'
        # 调用dbUtil的query_one方法查询音乐ID
        mid = dbUtil().query_one(sql2, music_name)
        # 构造删除音乐列表的SQL语句
        sql = 'delete from t_list where uid=%s and mid=%s'
        # 调用dbUtil的exeDML方法删除音乐列表
        dbUtil().exeDML(sql, self.user[0], mid)
    def playMusic(self, music_name):
        """
        播放音乐。

        :param music_name: 音乐名称。
        """
        # 构造查询音乐路径的SQL语句
        sql = 'select path from t_music where music_name=%s'
        # 调用dbUtil的query_one方法查询音乐路径
        path = dbUtil().query_one(sql, music_name)
        # 初始化pygame的mixer模块
        pygame.mixer.init()
        # 加载音乐文件
        pygame.mixer.music.load(path[0])
        # 播放音乐
        pygame.mixer.music.play()