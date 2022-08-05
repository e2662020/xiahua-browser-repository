from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys
 
 
class WebView(QWebEngineView):
	def __init__(self, parent):
		super().__init__(parent)
	def createWindow(self, webWindowType):
		return main_demo.browser
 
 
class MainDemo(QMainWindow):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setWindowTitle('浏览器')
		self.setWindowIcon(QIcon('icons/penguin.png'))
		self.resize(1600,1000)
		self.show()
		# URL地址栏
		self.urlbar = QLineEdit()
		self.urlbar.returnPressed.connect(self.navigate_to_url)
		# 标签栏
		self.tabs = QTabWidget()
		self.tabs.setDocumentMode(True)
		self.tabs.tabBarDoubleClicked.connect(self.tab_open)
		self.tabs.currentChanged.connect(self.current_tab_changed)
		self.tabs.setTabsClosable(True)
		self.tabs.tabCloseRequested.connect(self.close_current_tab)
		self.add_new_tab(QUrl('http://xiahuaos.top/homepage'), '虾滑主页')
		self.setCentralWidget(self.tabs)
		new_tab_action = QAction(QIcon('icons/add_page.png'), '新标签页', self)
		new_tab_action.triggered.connect(self.add_new_tab)
		# 导航栏
		navigation_bar = QToolBar('Navigation')
		navigation_bar.setIconSize(QSize(16, 16))
		self.addToolBar(navigation_bar)
		back_button = QAction(QIcon('icons/back.png'), '后退', self)
		forward_button = QAction(QIcon('icons/forward.png'), '前进', self)
		stop_button = QAction(QIcon('icons/stop.png'), '停止加载', self)
		reload_button = QAction(QIcon('icons/renew.png'), '刷新', self)
		back_button.triggered.connect(self.tabs.currentWidget().back)
		forward_button.triggered.connect(self.tabs.currentWidget().forward)
		stop_button.triggered.connect(self.tabs.currentWidget().stop)
		reload_button.triggered.connect(self.tabs.currentWidget().reload)
		navigation_bar.addAction(back_button)
		navigation_bar.addAction(forward_button)
		navigation_bar.addAction(stop_button)
		navigation_bar.addAction(reload_button)
		navigation_bar.addSeparator()
		navigation_bar.addWidget(self.urlbar)
 
	def navigate_to_url(self):
		current_url = QUrl(self.urlbar.text())
		if current_url.scheme() == '':
			current_url.setScheme('http')
		self.tabs.currentWidget().load(current_url)
 
	def renew_urlbar(self, url, browser=None):
		if browser != self.tabs.currentWidget():
			return
		self.urlbar.setText(url.toString())
		self.urlbar.setCursorPosition(0)
 
 
	# 添加新的标签页
	def add_new_tab(self, qurl=QUrl(''), label='Blank'):
		self.browser = WebView(self)
		self.browser.load(qurl)
		i = self.tabs.addTab(self.browser, label)
		self.tabs.setCurrentIndex(i)
		self.browser.urlChanged.connect(lambda qurl, browser=self.browser: self.renew_urlbar(qurl, self.browser))
		self.browser.loadFinished.connect(lambda _, i=i, browser=self.browser: self.tabs.setTabText(i, self.browser.page().title()))

	def tab_open(self, i):
		if i == -1:
			self.add_new_tab()
	def current_tab_changed(self, i):
		qurl = self.tabs.currentWidget().url()
		self.renew_urlbar(qurl, self.tabs.currentWidget())
	def close_current_tab(self, i):
		if self.tabs.count() < 2:
			return
		self.tabs.removeTab(i)
 
 
 
if __name__ == '__main__':
	my_application = QApplication(sys.argv) 
	main_demo = MainDemo()
	main_demo.show()
	my_application.exec_()