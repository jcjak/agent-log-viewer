from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

# Every QT GUI needs to be initialized with QApplication
class Application(QApplication):
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.app.setStyle('Fusion')
        self.app.setApplicationName('JumpCloud Log Viewer')
        self.app.setOrganizationName('JumpCloud')

# Instantiating the syntax highlighter module to color the text
class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent):
        super(Highlighter, self).__init__(parent)
        self.sectionFormat = QTextCharFormat()
        self.sectionFormat.setForeground(QColor(0,0,255))
        self.errorFormat = QTextCharFormat()
        self.errorFormat.setForeground(QColor(255,0,0))

# Defining error levels
    def highlightBlock(self, text):
        if '[ERROR]' in text:
            self.setFormat(0, len(text), self.errorFormat)    
        elif '[INFO]' in text:
            self.setFormat(0, len(text), self.sectionFormat)

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.editor = QTextEdit(self)
        self.editor.setMinimumSize(400, 300)
        self.editor.setAcceptDrops(True)
        self.editor.setReadOnly(True)
        self.editor.setText('Test')

        self.button_OpenDialog = QPushButton('Open Log File', self)
        self.button_OpenDialog.clicked.connect(self.on_button_click)

        # Order of layout widgets determines their presentation.
        layout = QVBoxLayout(self)
        layout.addWidget(self.editor)
        layout.addWidget(self.button_OpenDialog)
        self.setLayout(layout)

    def on_button_click(self):
        path = QFileDialog.getOpenFileName(None, 'Open Log', '/', 'Log Files (*.log)')

        if path[0]:
            file = QFile(path[0])
            if file.open(QIODevice.ReadOnly):
                stream = QTextStream(file)
                text = stream.readAll()
                #info = QtCore.QFileInfo(path)
                self.editor.setPlainText(text)
                self.highlighter = Highlighter(self.editor.document())
                file.close()

                
        
        #Window().editor.setText(data)
    #button.clicked.connect(on_button_click)
    
    # Runs the above function on button click.
    

    # this code works but it colors the entire widget.
    # trying to figure out how to get it to color a single line only
    # if '[ERROR]' in data:
    #     editor.setStyleSheet('color: red')
    #     data.setStyleSheet('color: red')


# Execute the app indefinitely, until user terminates process/app.

if __name__ == '__main__':
    import sys
    app = Application()
    window = Window()
    window.show()
    app.exec_()