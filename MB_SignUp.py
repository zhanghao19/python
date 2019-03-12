import pymysql,random,hashlib,pymongo
from MyBank import MB_sqlcode as sql


db_config = {
    'host': '127.0.0.1',  # 连接的ip
    'port': 3306,  # mysql默认端口3306
    'user': 'root',  # 用户名
    'password': 'qwe123',  # 密码
    'db': 'python3',  # 进入到的数据库名
    'charset': 'utf8'  # 编码方式
}

class MyBank:

    def __init__(self):
        self.conn = pymysql.connect (**db_config)  # 将db_config里的内容解包到connect中，**表示解包
        self.cur = self.conn.cursor ()  # 创建光标

    # 创建/删除客户表
    def create_tb(self,drop = 0):   #如果需要删除则传入任意数字即可
        try:
            if drop:
                self.cur.execute (sql.drop_tb)
            else:
                self.cur.execute (sql.create_tb)
            return self.cur.fetchall ()

        except Exception as e:
            print(e)
            self.conn.rollback()

        finally:
            self.conn.commit()      #提交修改

    # 自动生成银行卡号，密码加密，写入数据库；删除用户
    def create_user(self,u_name,phone_nb,passwd):
        self.id_card = '62143568' + str (random.randint (100000, 999999))

        try:
            self.cur.execute(sql.sign_up.format(self.id_card,u_name,phone_nb,passwd))  # 执行sql语句
            print('创建成功，您的卡号为: %s'%self.id_card)
            return self.cur.fetchall()

        except Exception as e:
            print(e)
            self.conn.rollback()    #遇到错误回滚

        finally:
            self.conn.commit()      #提交修改
    
    # 用户登录
    def sign_in(self,id_card,passwd):

        try:
            while True:
                u_name = self.cur.execute (sql.sign_in.format (id_card, passwd))
                if u_name == 0:
                    passwd = md5(input('密码有误，请重新输入:'))
                    continue
                else:
                    break
            print ('欢迎光临！%s' % self.cur.fetchall ()[0][0])
        except Exception as e:
            print (e)
            self.conn.rollback ()  # 遇到错误回滚

    # 输入银行卡号和密码查询余额
    def balance(self,id_card):
        try:
            # 条件查询,查询余额
            self.cur.execute (sql.find_money.format(id_card))  # 执行sql
            money = self.cur.fetchall()[0][0]
            print('账户余额:\t{}元'.format(money))   #int
        except Exception as e:
            print(e)
            self.conn.rollback()    #遇到错误回滚

    # 存取钱
    def m_money(self,id_card,money):
        try:
            self.cur.execute (sql.find_money.format(id_card))  # 执行sql
            add_money = self.cur.fetchall()[0][0] + money
            self.cur.execute(sql.change_money.format(add_money,id_card))
            self.balance(id_card)
        except Exception as e:
            print (e)
            self.conn.rollback ()  # 遇到错误回滚

        finally:
            self.conn.commit ()  # 提交修改
    
    #修改密码
    def change_passwd(self,id_card,new_passwd,old_passwd):
        try:
            while True:
                u_name = self.cur.execute(sql.change_passwd.format(new_passwd,id_card,old_passwd))
                if new_passwd == old_passwd:
                    new_passwd = md5(input ('新密码不能与旧密码相同，请重新输入:'))
                    continue
                elif u_name == 0:
                    old_passwd = md5(input ('原密码密码有误，请重新输入:'))
                    continue
                else:
                    print('密码修改成功！')
                    break

        except Exception as e:
            print(e)
            print('原密码输入错误！')
            self.conn.rollback()
        finally:
            self.conn.commit()

    # 注销银行卡
    def drop_user(self,id_card,passwd):
        try:
            self.cur.execute(sql.drop_user.format(id_card,passwd))  # 执行sql语句
            print('用户%s已被删除'%id_card)
            return self.cur.fetchall()

        except Exception as e:
            print(e)
            self.conn.rollback()    #遇到错误回滚

        finally:
            self.conn.commit()      #提交修改


    # 析构，在类调用量为0时，执行关闭数据库连接和光标
    def __del__(self):
        self.cur.close ()  # 关闭游标.
        self.conn.close ()  # 关闭conn.

# 加密密码的方法
def md5(passwd):
    a = bytes(int(passwd))
    m = hashlib.md5()
    m.update(a)
    return m.hexdigest()

# 主要服务系统
def service():
    print('------------欢迎进入银行系统------------')
    while True:
        print('1.申请一张银行卡\n2.用户登陆\n3.注销银行卡\n其他任意数字退出')
        select_1 = input('请通过数字选择您想办理的业务：')
        if select_1 == '1':
            u_name = input('请输入您的名字:')
            phone_nb = input('请输入您的手机号:')
            passwd = input('请设置密码:')
            p.create_user(u_name,passwd,phone_nb)
            continue
        elif select_1 == '2':
            print ('------------用户登陆------------')
            id_card = input('请输入您的银行卡号:')
            passwd= md5(input('请输入您的登陆密码:'))
            p.sign_in(id_card,passwd)
            menu(id_card)
            break
        elif select_1 == '3':
            print ('------------注销银行卡------------')
            id_card = input('请输入您的银行卡号:')
            passwd= md5(input('请输入您的登陆密码:'))
            p.drop_user(id_card,passwd)
            continue
        else:
            print('感谢您的使用，再见！')
            break
            
# 登录后用户菜单
def menu(id_card):
    while True:
        print ('------------菜单------------\n1.查询余额\n2.存款\n3.取款\n4.更改密码\n其他任意数字退出')
        select_2 = input ('请通过数字选择您想办理的业务：')
        if select_2 == '1':
            p.balance (id_card)
            continue
        elif select_2 == '2':
            money = int(input ('请输入存入金额：'))
            p.m_money(id_card,money)
        elif select_2 == '3':
            money = int(input ('请输入取出金额：'))
            p.m_money(id_card,money*-1)
        elif select_2 == '4':
            id_card = input('请输入您的银行卡号:')
            old_passwd= md5(input('请输入旧密码:'))
            new_passwd= md5(input('请输入新密码:'))
            p.change_passwd(id_card,new_passwd,old_passwd)
        else:
            print ('感谢您的使用，再见！')
            break

if __name__ == '__main__':
    p = MyBank()
    service()




