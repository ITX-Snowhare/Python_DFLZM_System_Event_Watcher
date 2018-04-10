# -*- coding: utf-8 -*-




from datetime import datetime

class sf_time_handle:

    def shouhuo_handle(self,shuohuotime,db_stat):
        if shuohuotime == 0 or db_stat == 1:
            return 0,0,0,0
        else:
            now = shuohuotime[1]
            lncl = str((datetime.now() - shuohuotime[0])).split('.')[0]
            lnsh = str((datetime.now() - shuohuotime[1])).split('.')[0]
            yc_second = (datetime.now() - shuohuotime[0]).total_seconds()
            return now,lncl,lnsh,yc_second

    def faliao_handle(self,faliaotime,db_stat):
        if faliaotime == 0 or db_stat == 1:
            return 0,0,0,0
        else:
            now = faliaotime[1]
            lncl = str((datetime.now() - faliaotime[0])).split('.')[0]
            lnfl = str((datetime.now() - faliaotime[1])).split('.')[0]
            yc_second = (datetime.now() - faliaotime[0]).total_seconds()
            return now,lncl,lnfl,yc_second

if __name__=="__main__":
    test = sf_time_handle()
