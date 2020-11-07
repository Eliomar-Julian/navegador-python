class Abas:
    def __init__(self, master, objeto):
        self.ObjectWidgets = objeto
        self.master = master
        try:
            self.master.addTab(
                self.ObjectWidgets['qwidgets' + str(
                    self.master.CounterTabs)],self.ObjectWidgets['webengine' + str(
                    self.master.CounterTabs)].icon(),self.ObjectWidgets['webengine' + str(
                    self.master.CounterTabs)].title()[:20]
            )            
        except KeyError:
            if self.master.CounterTabs != 0:
                self.ObjectWidgets['pesquisa' + str(
                    self.master.CounterTabs - 1)].busca.clear(

                )
                self.ObjectWidgets['pesquisa' + str(
                    self.master.CounterTabs - 1)].busca.insert(
                    self.ObjectWidgets['webengine' + str(
                    self.master.CounterTabs - 1)].url().toString()
                )
                self.ObjectWidgets['pesquisa' + str(
                    self.master.CounterTabs - 1)].busca.setCursorPosition(0
                )
                self.master.setTabToolTip(
                    self.master.currentIndex(),self.ObjectWidgets['webengine' + str(
                    self.master.CounterTabs - 1)].title().upper()
                )                
            else:
                self.ObjectWidgets['pesquisa0'].busca.clear()
                self.ObjectWidgets['pesquisa0'].busca.insert(
                    self.ObjectWidgets['webengine0'].url().toString()
                )
                self.ObjectWidgets['pesquisa0'].busca.setCursorPosition(0)
                self.master.setTabToolTip(
                    self.master.currentIndex(),self.ObjectWidgets['webengine0'].title().upper()
                )
                
                