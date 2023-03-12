from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import sys


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'WebBrowser'
        self.width = 1280
        self.height = 720
        self.left = self.height // 2
        self.top = 200

        self.webview()
        self.show_window()



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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())