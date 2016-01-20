import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):

	def __init__(self):
		super(Example,self).__init__()

		self.initUI()

	def initUI(self):

		exitAction = QtGui.QAction(QtGui.QIcon("comfortable.png"),'&Exit', self)
		exitAction.setShortcut("Ctrl+Q")
		exitAction.setStatusTip("Exit Application")

		exitAction.triggered.connect(QtGui.qApp.quit)

		textEdit = QtGui.QTextEdit()
		self.setCentralWidget(textEdit)

		self.toolbar = self.addToolBar('Exit')
		self.toolbar.addAction(exitAction)

		menubar = self.menuBar()
		fileMenu = menubar.addMenu("&Namit")
		fileMenu.addAction(exitAction)

		self.setGeometry(300, 300, 500, 500)
		self.setWindowTitle("Hey Baby!")
		self.setWindowIcon(QtGui.QIcon('comfortable.png'))

		self.show()















def main():
	app = QtGui.QApplication(sys.argv)
	ex = Example()
	app.exec_()


if __name__ == "__main__":
	main()