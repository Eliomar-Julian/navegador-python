from PySide2.QtWidgets import (
    QWidget, QApplication, QVBoxLayout,
    QTabWidget, QToolButton
)
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtCore import QUrl, Qt
from webwidgets import WebEngine
from pesquisa import Search
import sys


print(sys.argv[:])

class Browser(QTabWidget):
    ObjectWidgets = dict()
    CounterTabs = 0

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

        self.ObjectWidgets[
            'qwidgets' + str(self.CounterTabs)
            ] = QWidget()

        self.ObjectWidgets[
            'webengine' + str(self.CounterTabs)
            ] = WebEngine(self)

        self.ObjectWidgets[
            'webengine' + str(self.CounterTabs)
            ].setUrl(self.URL)

        self.ObjectWidgets[  # barra de navegação
            'pesquisa' + str(self.CounterTabs)
            ] = Search()

        self.ObjectWidgets[  # voltar a pagina anterior
            'pesquisa' + str(self.CounterTabs)
            ].voltar.clicked.connect(
            self.ObjectWidgets['webengine' + str(self.CounterTabs)].back)

        self.ObjectWidgets[  # avançar
            'pesquisa' + str(self.CounterTabs)
            ].avancar.clicked.connect(
            self.ObjectWidgets['webengine' + str(self.CounterTabs)].forward)

        self.ObjectWidgets[  # recarrega a pagina
            'pesquisa' + str(self.CounterTabs)
            ].reload.clicked.connect(
            self.ObjectWidgets['webengine' + str(self.CounterTabs)].reload)

        self.ObjectWidgets[
            'pesquisa' + str(self.CounterTabs)
            ].busca.returnPressed.connect(self.busca)

        self.ObjectWidgets[
            'position' + str(self.CounterTabs)
            ] = QVBoxLayout(self.ObjectWidgets['qwidgets' + str(self.CounterTabs)])

        self.ObjectWidgets[
            'position' + str(self.CounterTabs)
            ].setContentsMargins(0, 0, 0, 0)

        self.ObjectWidgets[
            'position' + str(self.CounterTabs)
            ].addWidget(
            self.ObjectWidgets[
                'pesquisa' + str(self.CounterTabs)], Qt.AlignCenter
        )

        self.ObjectWidgets[
            'position' + str(self.CounterTabs)
            ].addWidget(
            self.ObjectWidgets['webengine' + str(self.CounterTabs)]
        )
        print(self.ObjectWidgets.keys(), self.CounterTabs)
        self.ObjectWidgets[
            'webengine' + str(self.CounterTabs)
            ].show()
        self.ObjectWidgets[
            'webengine' + str(self.CounterTabs)
            ].loadFinished.connect(self.finished)
       

    # busca o que foi digitado na barra de pesquisa

    def busca(self):
        url = self.ObjectWidgets[
            'pesquisa' + str(self.CounterTabs)
            ].retorna_url()
        if '.' in url and len(url) > 3:
            if 'http' not in url:
                self.ObjectWidgets[
                    'webengine' + str(self.CounterTabs)
                    ].setUrl(f'http://{url}')
            else:
                self.ObjectWidgets[
                    'webengine' + str(self.CounterTabs)
                    ].setUrl(url)
        else:
            self.ObjectWidgets[
                'webengine' + str(self.CounterTabs)
                ].setUrl(f'https://www.google.com/search?q={url}')

    # remove a janela ao pressionar o botão de fechar aba

    def removeJanela(self, index):
        if self.count() > 1:
            self.removeTab(index)
            self.ObjectWidgets['webengine' + str(index)].deleteLater()
            self.CounterTabs -= 1

    # aguarda a pagina terminar de carregar //////////////////////////////////

    def finished(self):
        
        self.addTab(
            self.ObjectWidgets['qwidgets' + str(self.CounterTabs)],
            self.ObjectWidgets[
                'webengine' + str(self.CounterTabs)
                ].icon(),
            self.ObjectWidgets[
                'webengine' + str(self.CounterTabs)
                ].title()[:20])

        self.setTabToolTip(
            self.currentIndex(),
            self.ObjectWidgets[
                'webengine' + str(self.CounterTabs)
                ].url().toString().upper())

        self.ObjectWidgets[
            'pesquisa' + str(self.CounterTabs)
            ].busca.clear()

        self.ObjectWidgets[
            'pesquisa' + str(self.CounterTabs)
            ].busca.insert(self.ObjectWidgets[
                               'webengine' + str(self.CounterTabs)
                               ].url().toString())

        self.ObjectWidgets[
            'pesquisa' + str(self.CounterTabs)
            ].busca.setCursorPosition(0)

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
