from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

#class JCLogView():
    
# Every QT GUI needs to be initialized with QApplication

# Code to display log files after import
#editor = QTextEdit()

# Log text display output 

#app = QApplication([])
app = QApplication(sys.argv)
app.setStyle('Fusion')
app.setApplicationName('JumpCloud Log Viewer')
app.setOrganizationName('JumpCloud')

button = QPushButton('Add Log File')

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.editor = QTextEdit(self)
        self.editor.setMinimumSize(400, 300)
        self.editor.setAcceptDrops(True)
        self.editor.setReadOnly(True)
        self.editor.setText('Test')

        layout = QVBoxLayout(self)
        layout.addWidget(button)
        layout.addWidget(self.editor)
        self.setLayout(layout)

    def on_button_click(self):
        dialog = QFileDialog()
        fname = dialog.getOpenFileName(None, 'Open Log', '/', 'Log Files (*.log)')

        #if fname[0]:
        f = open(fname[0], 'r')

        #with f:
        data = f.read()

        # Instantiating the syntax highlighter module to color the text
        class Highlighter(QSyntaxHighlighter):
            def __init__(self, parent):
                super(Highlighter, self).__init__(parent)
                self.sectionFormat = QTextCharFormat()
                self.sectionFormat.setForeground(Qt.blue)
                self.errorFormat = QTextCharFormat()
                self.errorFormat.setForeground(Qt.red)

        # Defining error levels
            def highlightBlock(self, text):
                if text.startswith('[ERROR]'):
                    self.setFormat(0, len(text), self.errorFormat)    
                elif text.startswith('[INFO]'):
                    self.setFormat(0, len(text), self.sectionFormat)
        
        Window().editor.setText(data)
    button.clicked.connect(on_button_click)
    
    # Runs the above function on button click.
    

    # this code works but it colors the entire widget.
    # trying to figure out how to get it to color a single line only
    # if '[ERROR]' in data:
    #     editor.setStyleSheet('color: red')
    #     data.setStyleSheet('color: red')


# Execute the app indefinitely, until user terminates process/app.

if __name__ == '__main__':
    import sys
    window = Window()
    window.show()
    #button.clicked.connect(on_button_click)
    app.exec_()