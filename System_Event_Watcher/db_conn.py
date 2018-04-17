# -*- coding: utf-8 -*-

"""

用于连接数据库并定义了获取数据的函数
作者:韦俊杰
最后编辑:

"""


import cx_Oracle

db_conn = 0
no_conn = 0  # 检测数据库连接


class Db_Contro:
    """
    对数据库进行操作
    连接测试
    执行语句,取得结果返回元组
    """

    def conn(self,db_name):
        """
        数据可库选择和连接测试
        :param db_name: ln
        :return:
        """
        global no_conn
        global db_conn
        if db_name == 'ln':
            db_conn = 'baan/baan@172.16.0.106:1521/ldlndb'
            # 添加其他数据库
        else:
            no_conn = 1

    def get_sfimg(self,error):
        """
        连接数据库
        :returns
        收货： LN处理时间，CP扫描时间
        发料： LN处理时间，发料时间
        数据库连接状态：0 ：成功 1：失败

        """

        global no_conn
        global db_conn

        if error == 0:
            try:
                dbc = cx_Oracle.connect(db_conn)
                #print('数据库已连接！')
                no_conn = 0
            except:
                #print('网络或数据库异常！')
                no_conn = 1
                #sys.exit(1)

        try:
            if no_conn == 0:

                cursor = dbc.cursor()
                cursor.execute(
                    'SELECT t$ddt+1/3,TO_DATE( substr(TRIM(t$dsca),-18,14) ,\'yyyy/mm/dd hh24:mi:ss\') '
                    'FROM ttiliu039302 '
                    'WHERE t$ddt+1/3 >(sysdate-15) '
                    'ORDER BY t$ddt  DESC')
                shouhuo = cursor.fetchone()

                cursor.execute('SELECT t$cdate+1/3,t$date+1/3 '
                               'FROM ttiliu056302 '
                               'WHERE t$cdate+1/3 >(sysdate-15)'
                               'ORDER BY t$cdate DESC')
                faliao = cursor.fetchone()

                cursor.close()
                dbc.close()

            else:
                shouhuo = (0,0)
                faliao = (0,0)
        except:
            no_conn = 1
            shouhuo = (0, 0)
            faliao = (0, 0)

        return shouhuo,faliao,no_conn

    def get_lnscn(self,error):

        global no_conn
        global db_conn

        if error == 0:
            try:
                dbc = cx_Oracle.connect(db_conn)
                #print('数据库已连接！')
                no_conn = 0
            except:
                #print('网络或数据库异常！')
                no_conn = 1
                #sys.exit(1)

        if no_conn == 0:

            cursor = dbc.cursor()
            cursor.execute(
                'SELECT t$nrgr,t$seri,t$ffno,t$dsca\
                FROM ttcmcs050302\
                WHERE t$blck != 1 AND t$ffno > 900000 AND t$seri != \'WPV\'\
                ORDER BY t$nrgr,t$seri')
            lnscn = cursor.fetchall()
            rows = cursor.rowcount

            cursor.close()
            dbc.close()

            if rows == 0:
                rows = 1
                lnscn = [('无数据', '无数据', '无数据', '无数据')]

        else:
            rows = 1
            lnscn = [('网络异常', '网络异常', '网络异常', '网络异常')]

        return lnscn,rows,no_conn


if __name__=="__main__":
    test = Db_Contro()
    test.conn('ln')
    a,b,c = test.get_lnscn(0)
    print(a)
    print(b)
    print(c)
