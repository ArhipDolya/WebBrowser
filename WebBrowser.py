from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QGridLayout, QMenuBar,\
    QPlainTextEdit, QAction, QFileDialog, QShortcut, QToolButton, QToolBar, QMainWindow
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
import sys


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.browser_window()
        self.showMaximized()
        self.navbar()


    def browser_window(self):
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)


    def navbar(self):
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)

        navbar.addAction(back_btn)
        navbar.addAction(forward_btn)
        navbar.addAction(reload_btn)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName('Hoogle')

    window = Window()
    sys.exit(app.exec_())