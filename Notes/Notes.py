from PyQt5.QtWidgets import QApplication
import sys

from Components.Main import Notes


app = QApplication(sys.argv)

w = Notes()
w.show()

sys.exit(app.exec_())
