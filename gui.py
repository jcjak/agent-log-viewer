from PyQt5.QtWidgets import *

#class JCLogView():
    
# Every QT GUI needs to be initialized with QApplication
app = QApplication([])
app.setStyle('Fusion')
app.setApplicationName('JumpCloud Log Viewer')
app.setOrganizationName('JumpCloud')

# Code to display log files after import
editor = QTextEdit()
editor.setAcceptDrops(True)

editor.setReadOnly(True)
editor.setText('Test')

# Some test code
window = QWidget()
layout = QVBoxLayout()
button = QPushButton('Add Log File')

layout.addWidget(button)

# Log text display output
layout.addWidget(editor)

window.setLayout(layout)
window.show()

def on_button_click(self):
    dialog = QFileDialog()
    dialog.getOpenFileName(self, 'Open Log', 'C:', 'Log Files (*.log *.txt)')
    alert.exec_()

# Execute the app indefinitely, until user terminates process/app.
button.clicked.connect(on_button_click)
app.exec_()

