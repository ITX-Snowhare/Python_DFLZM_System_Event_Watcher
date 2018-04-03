# -*- coding: utf-8 -*-

"""

用于连接数据库并定义了获取数据的函数
作者:韦俊杰
最后编辑:

"""


import cx_Oracle


class Db_Contro:
    """
    连接数据库,并对数据库进行操作
    """

    def get_dbimg(self,db_name):
        """
        连接数据库
        :returns
        收货： LN处理时间，CP扫描时间
        发料： LN处理时间，发料时间
        数据库连接状态：0 ：成功 1：失败

        """

        no_conn = 0  #检测数据库连接

        if db_name == 'ln':
            db_conn = 'baan/baan@172.16.0.106:1521/ldlndb'
            # 添加其他数据库
        try:
            dbc = cx_Oracle.connect(db_conn)
            print('数据库已连接！')
        except:
            print('连接数据库异常！')
            no_conn = 1
            #assert 0

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
        else:
            shouhuo = (0,0)
            faliao = (0,0)

        return shouhuo,faliao,no_conn


if __name__=="__main__":
    test = Db_Contro()
    a,b,c = test.get_dbimg('ln')
    print(a)
    print(b)
    print(c)
