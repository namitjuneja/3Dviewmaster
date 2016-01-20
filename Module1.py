import sys, os
from PyQt4 import QtGui, QtCore

class Example(QtGui.QMainWindow):

	def __init__(self):
		super(Example,self).__init__()
		self.initUI()

	def initUI(self):

		self.setToolTip("Hello!!")

		palette	= QtGui.QPalette()
		palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(QtGui.QPixmap("RH.png")))
    
		self.setPalette(palette)

		btn = QtGui.QPushButton("Hello Button", self)
		btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		btn.setToolTip("this is hello button")
		btn.resize(btn.sizeHint())
		btn.move(20,10)

		layout = QtGui.QVBoxLayout()
		layout.addWidget(btn)
		# layout.setStyleSheet("background-image: /RH.png")

		mainWidget = QtGui.QWidget()
		mainWidget.setLayout(layout)


		scrollWidget = QtGui.QScrollArea()
		scrollWidget.setWidget(mainWidget)
		scrollWidget.setWidgetResizable(True) # <---------------
		scrollWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		scrollWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)


		self.setCentralWidget(scrollWidget)


		self.setGeometry(0, 0, 500, 500)
		self.setWindowTitle("fORtHEwIN")
		self.setWindowIcon(QtGui.QIcon('comfortable.png'))

		

		

		self.center()

		self.show()

	def center(self):

		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topRight())
	
	# def wheelEvent(self,event):

	# 	vector = (event.delta() // 120 and event.delta() // 120 // abs(event.delta() // 120))

	# 	self.x =self.x + vector
    	# print self.x
    	# self.label.setText("Total Steps: "+QString.number(self.x))



	def closeEvent(self, event):

		reply = QtGui.QMessageBox.question(self,"Hey There!", "Wanna quit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)

		print type(reply)

		if reply == QtGui.QMessageBox.Yes:
			event.accept()
		else:
			print type(self.x)
			event.ignore()

def main():
	app = QtGui.QApplication(sys.argv)
	ex = Example()
	app.exec_()



if __name__ == '__main__':
	main()