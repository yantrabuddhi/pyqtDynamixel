__author__ = 'mandeep'

# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui
from UI_zeno_rec import Ui_zeno_rec


class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_zeno_rec()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    #app.processEvents()
    sys.exit(app.exec_())