from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor

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
    fname = dialog.getOpenFileName(None, 'Open Log', '/')
    color = QColorDialog.getColor(255, 0, 0)

    if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                editor.setText(data)
                
                #num_lines = sum(1 for line in output)
                #line_count = f.readline(num_lines)

                if '[ERROR]' in data:
                        editor.setTextColor(color)


# Execute the app indefinitely, until user terminates process/app.
button.clicked.connect(on_button_click)
app.exec_()

