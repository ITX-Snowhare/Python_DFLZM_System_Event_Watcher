# -*- coding: utf-8 -*-

import os



class fileCount:


    def count(self,sys):

        lnPathu = '//172.16.0.214/csv/upfile_backup'
        cpPathu = '//172.15.1.60/csv/upfile_backup'
        mesPathu = '//172.20.0.34/d$/PVLDMES/CSV/upfile_backup'

        lnPathd = '//172.16.0.214/csv/downfile/backup'
        cpPathd = ''
        mesPathd = '//172.20.0.34/d$/PVLDMES/CSV/downfile/backup'

        if sys == 'lnu':
            path = lnPathu
        elif sys == 'cpu':
            path = cpPathu
        elif sys == 'mesu':
            path = mesPathu
        elif sys == 'lnd':
            path = lnPathd
        elif sys == 'cpd':
            path = cpPathd
        elif sys == 'mesd':
            path = mesPathd
        else:
            raise ValueError('输入的系统不存在！')

        count = 0
        for filesName in os.listdir(path):
            count = count + 1

        return count

    def userLink(self):

        os.system('net use \\172.16.0.214\csv /user:baan "lqit-ln@ld"')
        #os.system('net use \\172.15.1.60\csv /user:guest "guest"')
        os.system('net use \\172.20.0.34\d$\PVLDMES /user:administrator "lqit-#4"')

if __name__=="__main__":
    test = fileCount()
    test.userLink()
    a = test.count('lnu')
    print(a)