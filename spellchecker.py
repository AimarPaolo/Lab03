import time
import multiDictionary as mdict
mdic = mdict.MultiDictionary()
class SpellChecker:

    def _init_(self):
        self.parole=[]


    def handleSentence(self, txtIn, language):
        lista = []
        listaErrate=[]
        self.parole = txtIn.split(" ")
        for parola in self.parole:
            lista.append(md.searchWord(parola, language))
        for r in lista:
            if r.corretta == False:
                listaErrate.append(r.parola)
        if listaErrate.__len__() != 0:
            print(f"Le parole errate sono")
            for par in listaErrate:
                print(par)
        if listaErrate._len_()==0:
            print(f"Tutte le parole sono corrette")
        print ( time.process_time())

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


def replaceChars(text):
    chars = "\\`*{}[]()>#+-.!$%^;,=~"
    for c in chars:
        text = text.replace(c, "")
    text = text.lower()
    text = text.replace("à", "a")
    text = text.replace("ì", "i")
    text = text.replace("è", "e")
    text = text.replace("é", "e")
    text = text.replace("ù", "u")
    text = text.replace("ò", "o")
    return text