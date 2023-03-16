from PyQt5.QtWidgets import QApplication, QAction, QToolBar, QMainWindow, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
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

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.home_page)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_url)
        go_btn = QAction('Go', self)
        go_btn.triggered.connect(lambda: self.load_url(self.url_bar.text()))

        self.browser.urlChanged.connect(self.update_url)

        navbar.addAction(back_btn)
        navbar.addAction(forward_btn)
        navbar.addAction(reload_btn)
        navbar.addAction(home_btn)
        navbar.addWidget(self.url_bar)
        navbar.addAction(go_btn)


    def load_url(self, url):
        return self.browser.setUrl(QUrl(url))

    def navigate_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))


    def home_page(self):
        url = QUrl('http://google.com')
        self.browser.load(url)

    def update_url(self, url):
        self.url_bar.setText(url.toString())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName('Hoogle')
    app.setWindowIcon(QIcon('icons/images.png'))
    window = Window()
    sys.exit(app.exec_())