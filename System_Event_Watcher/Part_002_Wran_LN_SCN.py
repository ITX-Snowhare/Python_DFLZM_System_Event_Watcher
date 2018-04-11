# -*- coding: utf-8 -*-


class ln_scn_handle:

    def get_ln_scn(self,scn,row,db_stat):
        #if db_stat == 1
        scn_list = []
        for r in range(row):
            for d in range(4):
                scn_list.append(scn[r][d])
                #print(scn[r][d])
            #print(scn[r])
        return scn_list