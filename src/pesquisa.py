from PySide2.QtWidgets import (
    QPushButton, QFrame,
    QLineEdit, QHBoxLayout
)
from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon


class TopoBusca(QFrame):
    def __init__(self, parent=None):
        self.mae = parent
        QFrame.__init__(self, self.mae)
        self.setMaximumHeight(25)
        self.setStyleSheet(
            '''
            QFrame {
                background-color: #ffffff;
                margin-left: 20px;
                margin-right: 20px;
                margin-top: 0px;    
            }
            QPushButton {
                width: 20px;
                height: 20px;
                border-radius: 10px;
                background-color: #ffffff;
            }
            ''')
        self.voltar = QPushButton()
        self.voltar.setIcon(QIcon('./img/voltar.svg'))
        self.voltar.setToolTip('voltar')

        self.avancar = QPushButton()
        self.avancar.setIcon(QIcon('./img/avancar.svg'))
        self.avancar.setToolTip('avançar')

        self.reload = QPushButton()
        self.reload.setIcon(QIcon('./img/reload.svg'))
        self.reload.setToolTip('Recarregar')

        self.home = QPushButton()
        self.home.setIcon(QIcon('./img/casa.svg'))
        self.home.setToolTip('Inicio')

        self.menu = QPushButton()
        self.menu.setIcon(QIcon('./img/cardapio.svg'))
        self.menu.setToolTip('Opções')

        self.busca = QLineEdit()
        self.busca.setStyleSheet(
            '''border-radius: 10px;
            padding: 5px;
            font: 100 12pt "Arial";
            background-color: #f2f2f2;
            text-align: left;
            color: #00000f;
            '''
        )
        self.grade = QHBoxLayout(self)
        self.grade.setContentsMargins(0, 0, 0, 0)
        self.grade.addWidget(self.voltar, Qt.AlignLeft)
        self.grade.addWidget(self.avancar, Qt.AlignLeft)
        self.grade.addWidget(self.reload, Qt.AlignLeft)
        self.grade.addWidget(self.busca, Qt.AlignCenter)
        self.grade.addWidget(self.home, Qt.AlignRight)
        self.grade.addWidget(self.menu, Qt.AlignRight)

    def retorna_url(self):
        return self.busca.text()


class BuscaUrl:
    def __init__(self, master, objeto):
        self.ObjectWidgets = objeto
        self.master = master
        url = self.ObjectWidgets['pesquisa' + str(
            self.master.CounterTabs - 1)].retorna_url(
        )
        if '.' in url and len(url) > 3:
            if 'http' not in url:
                self.ObjectWidgets[
                    'webengine' + str(self.master.CounterTabs - 1)
                    ].setUrl(f'http://{url}')
            else:
                self.ObjectWidgets[
                    'webengine' + str(self.master.CounterTabs - 1)
                    ].setUrl(url)
        else:
            self.ObjectWidgets[
                'webengine' + str(self.master.CounterTabs - 1)
                ].setUrl(f'https://www.google.com/search?q={url}')