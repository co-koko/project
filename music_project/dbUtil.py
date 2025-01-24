import pymysql
class dbUtil():
    """
    dbUtil类用于管理与MySQL数据库的连接和操作。

    该类提供了执行DML语句、查询单条记录、查询多条记录以及关闭数据库连接的方法。
    """
    
    # 定义数据库连接配置
    __config={'host':'localhost',
            'user':'root','password':'1234','db':'play_music','charset':'utf8'
            }
    
    def __init__(self):
        """
        初始化dbUtil类的实例。

        该方法创建一个数据库连接和一个游标对象。
        """
        # 创建一个数据库连接
        self.connection=pymysql.connect(**dbUtil.__config)
        # 创建一个游标对象
        self.cursor=self.connection.cursor()
    
    def close(self):
        """
        关闭数据库连接和游标对象。

        该方法关闭当前对象的数据库连接和游标对象。
        """
        # 如果游标对象存在
        if self.cursor:
            # 关闭游标对象
            self.cursor.close()
        # 如果数据库连接存在
        if self.connection:
            # 关闭数据库连接
            self.connection.close()
    
    def exeDML(self,sql,*agrs):
        """
        执行DML语句（插入、更新、删除）。

        :param sql: 要执行的SQL语句。
        :param agrs: SQL语句中的参数。
        :return: 插入操作生成的自增ID，如果没有则返回None。
        """
        try:
            # 执行SQL语句
            count=self.cursor.execute(sql,agrs)
            # 获取插入操作生成的自增ID
            id = self.connection.insert_id()
            # 提交事务
            self.connection.commit()
            # 返回自增ID
            return id
        except Exception as e:
            # 打印异常信息
            print(e)
            # 如果数据库连接存在
            if self.connection:
                # 回滚事务
                self.connection.rollback()
        finally:
            # 关闭数据库连接和游标对象
            self.close()
    
    def query_one(self,sql,*agrs):
        """
        执行查询语句并返回单条记录。

        :param sql: 要执行的SQL语句。
        :param agrs: SQL语句中的参数。
        :return: 查询结果的单条记录，如果没有则返回None。
        """
        try:
            # 执行SQL语句
            self.cursor.execute(sql,agrs)
            # 返回查询结果的单条记录
            return self.cursor.fetchone()
        except Exception as e:
            # 打印异常信息
            print(e)
        finally:
            # 关闭数据库连接和游标对象
            self.close()
    
    def query_all(self,sql,*agrs):
        """
        执行查询语句并返回所有记录。

        :param sql: 要执行的SQL语句。
        :param agrs: SQL语句中的参数。
        :return: 查询结果的所有记录，如果没有则返回空列表。
        """
        try:
            # 执行SQL语句
            self.cursor.execute(sql,agrs)
            # 返回查询结果的所有记录
            return self.cursor.fetchall()
        except Exception as e:
            # 打印异常信息
            print(e)
        finally:
            # 关闭数据库连接和游标对象
            self.close()

if __name__=="__main__":
    """
    主程序入口。

    该部分代码用于测试dbUtil类的功能。
    """
    # 创建dbUtil类的实例
    DbUtil=dbUtil()
    # 定义查询语句
    sql='select * from emp'
    # 调用query_all方法查询所有记录
    emps=DbUtil.query_all(sql)
    # 遍历查询结果并打印
    for e in emps:
        print(e)
