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
        self.app.setWindowIcon(QIcon('logo-2018-copy.ico'))

# Instantiating the syntax highlighter module to color the text
class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent):
        super(Highlighter, self).__init__(parent)
        self.warnFormat = QTextCharFormat()
        self.warnFormat.setBackground(QColor(255,255,0))
        self.errorFormat = QTextCharFormat()
        self.errorFormat.setForeground(QColor(255,255,0))
        self.errorFormat.setBackground(QColor(255,0,0))
        self.versFormat = QTextCharFormat()
        self.versFormat.setForeground(QColor(90,25,255))
        self.versFormat.setBackground(QColor(0,255,0))

# Defining error levels
    def highlightBlock(self, text):
        if '[ERROR]' in text:
            self.setFormat(0, len(text), self.errorFormat)    
        elif '[WARN]' in text:
            self.setFormat(0, len(text), self.warnFormat)
        elif 'AgentVersion' in text:
            self.setFormat(0, len(text), self.versFormat)

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.editor = QTextEdit(self)
        self.editor.setMinimumSize(400, 300)
        self.editor.setAcceptDrops(True)
        self.editor.setReadOnly(True)
        self.editor.setText('Awaiting Log File')

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

# Execute the app indefinitely, until user terminates process/app.

if __name__ == '__main__':
    import sys
    app = Application()
    window = Window()
    window.show()
    app.exec_()