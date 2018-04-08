# -*- coding: utf-8 -*-

sh = str(gotshouhuo()).split('.')[0]
cl = str(gotchuli()).split('.')[0]
fl = str(gotfaliao()).split('.')[0]
fcl = str(gotfchuli()).split('.')[0]

t = gotchulis()  # 秒级比较
f = gotfaliaos()  # 秒级比较

self.label_2.setText(str(sh))
self.label_17.setText(str(fcl))
self.label_7.setText(str(shouhuoTime[3]))
self.label_12.setText(str(faliaoTime[1]))
# self.textBrowser.setText(str(gotcsv()))
# self.textBrowser_2.setText(str(gotjjk()))

if t >= 600 or f >= 600:  # 报警声音播放
    if song == 0:
        play = threading.Thread(self.waring())
        play.setDaemon(True)
        play.start()