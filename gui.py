from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import re

#class JCLogView():
    
# Every QT GUI needs to be initialized with QApplication
app = QApplication([])
app.setStyle('Fusion')
app.setApplicationName('JumpCloud Log Viewer')
app.setOrganizationName('JumpCloud')

# Code to display log files after import
editor = QTextEdit()
editor.setMinimumSize(800, 600)
editor.setAcceptDrops(True)
editor.setReadOnly(True)
editor.setText('Test')

lineeditor = QLineEdit()

# Sets the window, layout, and button.
window = QWidget()
layout = QVBoxLayout()
button = QPushButton('Add Log File')

layout.addWidget(button)

# Instantiating the syntax highlighter module to color the text
highlighter = QTextCharFormat()

# Log text display output 
layout.addWidget(editor)

window.setLayout(layout)
window.show()

def on_button_click(self):
    dialog = QFileDialog()
    fname = dialog.getOpenFileName(None, 'Open Log', '/')
    color = QColor(255,0,0)

    if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                editor.setText(data)

                # this code works but it colors the entire log.
                # trying to figure out how to get it to color a single line only
                if '[ERROR]' in data:
                        editor.setStyleSheet('color: red')


# Execute the app indefinitely, until user terminates process/app.
button.clicked.connect(on_button_click)
app.exec_()