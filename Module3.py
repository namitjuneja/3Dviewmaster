import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):

	def __init__(self):
		super(Example,self).__init__()
		self.initUI()

	def initUI(self):


		okbtn = QtGui.QPushButton("Okhay")
		cbtn = QtGui.QPushButton("Cancel")

		

		self.setGeometry(300,300,500,500)
		self.setWindowTitle("Namit Juneja")
		self.show()


def main():

	app = QtGui.QApplication(sys.argv)
	ex = Example()
	app.exec_()


if __name__ == "__main__":
	main()