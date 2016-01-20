from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class Helloworld(QDialog):
	def __init__(self):
		QDialog.__init__(self)


		layout = QVBoxLayout()

		url = QLineEdit()
		self.save = QLineEdit()
		progress = QProgressBar()
		button = QPushButton("Download")
		browse = QPushButton("Browse")


		url.setPlaceholderText("URL")
		self.save.setPlaceholderText("Save Location")

		progress.setValue(85)
		progress.setAlignment(Qt.AlignRight)

		layout.addWidget(url)
		layout.addWidget(self.save)
		layout.addWidget(browse)
		layout.addWidget(progress)
		layout.addWidget(button)
		

		self.setLayout(layout)

		self.setWindowTitle("Hey Yo!")
		self.setFocus()

		browse.clicked.connect(self.browse_press)

	def labelEdit(self, text="Fuck You!"):
		self.label.setText(str(text))

	def browse_press(self):
		save_file = QFileDialog.getSaveFileName(self, caption="Namit Juneja", directory=".", filter="All Files (*.*)")
		self.save.setText(QDir.toNativeSeparators(save_file))
		print save_file
		print QDir.toNativeSeparators(save_file)

app = QApplication(sys.argv)
dialog = Helloworld()
dialog.show()
app.exec_()