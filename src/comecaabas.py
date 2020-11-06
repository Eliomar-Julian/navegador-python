from PySide2.QtWidgets import QWidget, QVBoxLayout
from PySide2.QtCore import Qt
from webwidgets import WebEngine
from pesquisa import TopoBusca

class Comecar:
    def __init__(self, master, objeto):
        self.master = master
        self.ObjectWidgets = objeto
        self.ObjectWidgets[
            'qwidgets' + str(self.master.CounterTabs)
            ] = QWidget()

        self.ObjectWidgets[
            'webengine' + str(self.master.CounterTabs)
            ] = WebEngine(self.master)

        self.ObjectWidgets[
            'webengine' + str(self.master.CounterTabs)
            ].setUrl(self.master.URL)

        self.ObjectWidgets[  # barra de navegação
            'pesquisa' + str(self.master.CounterTabs)
            ] = TopoBusca()

        self.ObjectWidgets[  # voltar a pagina anterior
            'pesquisa' + str(self.master.CounterTabs)
            ].voltar.clicked.connect(
            self.ObjectWidgets['webengine' + str(self.master.CounterTabs)].back)

        self.ObjectWidgets[  # avançar
            'pesquisa' + str(self.master.CounterTabs)
            ].avancar.clicked.connect(
            self.ObjectWidgets['webengine' + str(self.master.CounterTabs)].forward)

        self.ObjectWidgets[  # recarrega a pagina
            'pesquisa' + str(self.master.CounterTabs)
            ].reload.clicked.connect(
            self.ObjectWidgets['webengine' + str(self.master.CounterTabs)].reload)

        self.ObjectWidgets[
            'pesquisa' + str(self.master.CounterTabs)
            ].busca.returnPressed.connect(self.master.busca)

        self.ObjectWidgets[
            'position' + str(self.master.CounterTabs)
            ] = QVBoxLayout(self.ObjectWidgets['qwidgets' + str(self.master.CounterTabs)])

        self.ObjectWidgets[
            'position' + str(self.master.CounterTabs)
            ].setContentsMargins(0, 0, 0, 0)

        self.ObjectWidgets[
            'position' + str(self.master.CounterTabs)
            ].addWidget(
            self.ObjectWidgets[
                'pesquisa' + str(self.master.CounterTabs)], Qt.AlignCenter
        )

        self.ObjectWidgets[
            'position' + str(self.master.CounterTabs)
            ].addWidget(
            self.ObjectWidgets['webengine' + str(self.master.CounterTabs)]
        )
        print(self.ObjectWidgets.keys(), self.master.CounterTabs)
        self.ObjectWidgets[
            'webengine' + str(self.master.CounterTabs)
            ].show()
        self.ObjectWidgets[
            'webengine' + str(self.master.CounterTabs)
            ].loadFinished.connect(self.master.adicionarAbas)