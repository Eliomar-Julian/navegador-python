class Abas:
    def __init__(self, master, objeto):
        self.ObjectWidgets = objeto
        self.master = master
        print(self.master.CounterTabs)
        self.master.addTab(
            self.ObjectWidgets['qwidgets' + str(self.master.CounterTabs)],
            self.ObjectWidgets[
                'webengine' + str(self.master.CounterTabs)
                ].icon(),
            self.ObjectWidgets[
                'webengine' + str(self.master.CounterTabs)
                ].title()[:20])

        self.master.setTabToolTip(
            self.master.currentIndex(),
            self.ObjectWidgets[
                'webengine' + str(self.master.CounterTabs)
                ].url().toString().upper())

        self.ObjectWidgets[
            'pesquisa' + str(self.master.CounterTabs)
            ].busca.clear()

        self.ObjectWidgets[
            'pesquisa' + str(self.master.CounterTabs)
            ].busca.insert(self.ObjectWidgets[
                               'webengine' + str(self.master.CounterTabs)
                               ].url().toString())

        self.ObjectWidgets[
            'pesquisa' + str(self.master.CounterTabs)
            ].busca.setCursorPosition(0)