import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
	def __init__(self):
		super(Example,self).__init__()
		self.initUI()

	def initUI(self):

		lcd = QtGui.QLCDNumber(self)
		sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)

		vbox = QtGui.QHBoxLayout()
		vbox.addWidget(lcd)
		vbox.addWidget(sld)

		self.setLayout(vbox)
		sld.valueChanged.connect(lcd.display)

		self.setGeometry(300,300,500,500)

		self.show()




def main():
	app = QtGui.QApplication(sys.argv)
	ex = Example()
	app.exec_()

if __name__ == "__main__":
	main()
