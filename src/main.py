from PySide2.QtWidgets import (
    QWidget,
    QApplication,
    QVBoxLayout,
    QTabWidget,
    QToolButton
)
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtCore import QUrl, Qt
from webwidgets import WebEngine
from pesquisa import TopoBusca, BuscaUrl
from adicionarabas import Abas
from comecaabas import Comecar
import sys


class Browser(QTabWidget):
    ObjectWidgets = dict() # dicionario com todos os widgets
    CounterTabs = 0 # registrador de abas abertas

    def __init__(self):
        super(Browser, self).__init__()
        self.setTabsClosable(True)
        self.setMovable(True)
        self.more = QToolButton()
        self.more.setText('+')
        self.more.clicked.connect(self.comecar)
        self.more.setStyleSheet(
            '''border: none;
            padding: 5px;
            color: #fff;
            background: teal;'''
        )
        self.setCornerWidget(
            self.more, Qt.Corner.TopLeftCorner
        )
        self.tabCloseRequested.connect(
            self.removeJanela
        )
        self.comecar()

    # inicia as abas ///////////////////////////////////////////////////////////////////

    def comecar(self, url=None):
        self.URL = url
        if not self.URL:
            try:
                self.URL = sys.argv[1].replace('"', '')
            except IndexError:
                self.URL = 'http://www.google.com'
        Comecar(self, self.ObjectWidgets)       

    # busca o que foi digitado na barra de pesquisa depende de <pesquisa>

    def busca(self):
        BuscaUrl(self, self.ObjectWidgets)

    # remove a janela ao pressionar o botão de fechar aba

    def removeJanela(self, index):
        if self.count() > 1:
            self.removeTab(index)
            self.ObjectWidgets['webengine' + str(index)].deleteLater()
            self.CounterTabs -= 1

    # aguarda a pagina terminar de carregar e adiciona a aba solicitada
    # depende do modulo <adicionarabas> -> Abas

    def adicionarAbas(self):
        Abas(self, self.ObjectWidgets)
        self.CounterTabs = self.count()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(QPixmap('img/navegador.png')))
    app.setApplicationName('Python Browser Net')
    app.setApplicationDisplayName('Python Browser')
    tabVar = Browser()
    tabVar.setWindowTitle('Python Simple Browser')
    tabVar.showMaximized()
    tabVar.show()
    sys.exit(app.exec_())
