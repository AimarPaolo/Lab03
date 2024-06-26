import time
import multiDictionary as md
mdic = md.MultiDictionary()
class SpellChecker:

    def __init__(self, parole=None, time_passed = 0):
        self.parole = parole
        self.time_passed = time_passed

    def handleSentence(self, txtIn, language):
        lista = []
        listaErrate = []
        self.parole = txtIn.split(" ")
        for parola in self.parole:
            lista.append(mdic.searchWord(parola, language))
        for r in lista:
            if r.corretta is not True:
                listaErrate.append(r._parola)
        if listaErrate.__len__() != 0:
            print(f"Le parole errate sono")
            for par in listaErrate:
                print(par)
        if listaErrate.__len__() == 0:
            print(f"Tutte le parole sono corrette")
        print(time.process_time())
        #self.time_elapsed(time.process_time())

    def time_elapsed(self, time_calc):
        time_passed = time_calc
    def handleSentenceWithDichotomic(self, txtIn, language):
        lista = []
        listaErrate = []
        self.parole = txtIn.split(" ")
        for parola in self.parole:
            lista.append(mdic.searchWordDichotomic(parola, language))
        for r in lista:
            if r.corretta is not True:
                listaErrate.append(r._parola)
        if listaErrate.__len__() != 0:
            print(f"Le parole errate sono")
            for par in listaErrate:
                print(par)
        if listaErrate.__len__() == 0:
            print(f"Tutte le parole sono corrette")
            print(time.process_time())
      #  print(time.process_time()-self.time_passed)

    def printMenu(self):
        print("__________\n" +
              "      SpellChecker 101\n"+
              "__________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "__________\n")


