from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QGridLayout, QMenuBar,\
    QPlainTextEdit, QAction, QFileDialog, QShortcut
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
import sys


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.title = 'WebBrowser'
        self.width = 1280
        self.height = 720
        self.left = self.height // 2
        self.top = 200

        self.webview()
        self.show_window()
        self.menu_bar()


    def show_window(self):


        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon('icons/images.png'))
        self.show()

    def load_page(self):

        with open('html/window.html', 'r') as file:
            html = file.read()
            self.webEngineView.setHtml(html)


    def webview(self):
        webview = QVBoxLayout(self)

        self.webEngineView = QWebEngineView()
        self.webEngineView.setUrl(QUrl('https://www.google.com'))
        webview.addWidget(self.webEngineView)
        

        self.setLayout(webview)

    def menu_bar(self):
        menubar = QMenuBar()
        self.layout.addWidget(menubar, 0, 0)

        shortcut_exit = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_W), self)
        shortcut_open = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_Q), self)

        file_menu = menubar.addMenu('File')
        file_edit = menubar.addMenu('Edit')
        file_help = menubar.addMenu('Help')

        action_open = QAction('Open', self)
        action_exit = QAction('Exit', self)

        action_open.triggered.connect(self.open_file)
        action_exit.triggered.connect(self.close)
        shortcut_exit.activated.connect(self.close)
        shortcut_open.activated.connect(self.open_file)

        file_menu.addAction(action_exit)
        file_menu.addAction(action_open)

        text_box = QPlainTextEdit()
        self.layout.addWidget(text_box, 1, 0)

    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)",
                                                   options=options)

        try:
            with open(file_name, 'r') as f:
                file_content = f.read()
                print(file_content)

        except Exception as ex:
            print(f'There was an exception: {ex}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())