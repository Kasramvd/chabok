
#threading.Timer(1.0, self.print_paste,args=(curr,paste())).start()
from PySide import QtGui
from PySide import QtCore
import sqlite3 as lite
import sys
import re
from PySide.QtGui import QFrame, QPalette
from PySide.QtGui import QTableWidget, QTableWidgetItem, QColor, QPixmap

dic1={}
con = lite.connect('Generic_English_Persian.m2')
with con:    
    cur = con.cursor()    
    cur.execute("SELECT * FROM word")
    rows = cur.fetchall()
    for row in rows:
         dic1[row[1]]=row[2]



class UpdateStatsThread(QtCore.QThread,QtGui.QWidget):

    def __init__(self, parent=None):
        super(UpdateStatsThread, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent)
        self._running = False
        self.curr=None
        self.mess=QtGui.QMessageBox(self)
        self.cb = QtGui.QApplication.clipboard()
    def run(self):
        self._running = True
        while self._running:
            self.print_paste()
            self.msleep(1000)

    def stop(self, wait=False):
        self._running = False
        if wait:
            self.wait()

    def print_paste(self):
        print 'hi'
        if self.cb.text() != self.curr :
          try:

            print dic1[self.cb.text()].encode('utf-8')
            self.mess.information(self,'paste',"past text : {}".format(dic1[self.cb.text()].encode('utf-8')).decode('utf-8'))
          except KeyError:
            self.mess.information(self,'paste',"<font color=red><b>{}</b></font>".format('--------').encode('utf-8'))
          self.curr=self.cb.text()

app = QtGui.QApplication(sys.argv)
icon = UpdateStatsThread()
icon.run()
app.exec_()