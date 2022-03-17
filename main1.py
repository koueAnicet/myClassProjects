import sys 
from PyQt5.QWidgets import QApplication, QLabel

app =QApplication(sys.argv)
label = QLabel("hello world")
label.show()
app.exec_()