from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PySide2.QtWidgets import QAction
from json import load
from PySide2.QtCore import QThread
from pesquisa import Search
import os


class WebEngine(QWebEngineView):
    def __init__(self, parent):
        self.master = parent
        QWebEngineView.__init__(self, self.master)

    # // cria novas abas ao clicar com o botão do meio ou solicitar uma nova
    # // aba, tambem serve para criar uma nova janela ////////////////////////

    def createWindow(self, tipo):
        print(tipo)
        if tipo == self.page().WebBrowserBackgroundTab:
            self.master.comecar(self.page().requestedUrl())
        elif tipo == self.page().WebBrowserTab:
            self.master.comecar(self.page().requestedUrl())
        elif tipo == self.page().WebBrowserWindow:
            web = self.page().requestedUrl().toString()
            os.system(f'start pythonw.exe main.py "{web}"')
            
    # // manipula o menu de contexto original ////////////////////////////////

    def contextMenuEvent(self, event):
        self.teste = QAction('teste', self)
        self.menu = self.page().createStandardContextMenu()
        self.menu.addAction(self.teste)

        with open('traducao/traducao.json', 'r', encoding='utf-8') as js:
            arq = load(js)
            translate = self.menu.actions()
            lista = list(arq['contextMenu'].keys())

        for texto in translate:
            try:
                if texto.text() in lista:
                    texto.setText(arq['contextMenu'][texto.text()])
            except KeyError:
                pass
        self.menu.exec_(event.globalPos())
