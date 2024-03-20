import dictionary as dc
import richWord as rw


class MultiDictionary:

    def __init__(self, dictitalian=None, dictenglish=None, dictspanish=None):
        self._dictitalian = dictitalian
        self._dictenglish = dictenglish
        self._dictspanish = dictspanish

    def printDic(self, language):
        if language == "italian":
            dic = dc.Dictionary("Italian.txt")
            dic.printAll()
        elif language == "english":
            dic = dc.Dictionary("English.txt")
            dic.printAll()
        elif language == "spanish":
            dic = dc.Dictionary("Spanish.txt")
            dic.printAll()

    def searchWord(self, words, language):
        dic = None
        ritorno = None
        if language == "italian":
            dic = dc.Dictionary("Italian.txt")
        # lista=d.loadDictionary(".txt")
        elif language == "english":
            dic = dc.Dictionary("English.txt")
        # lista= d.loadDictionary("English.txt")
        elif language == "spanish":
            dic = dc.Dictionary("Spanish.txt")
            # lista=d.loadDictionary("Spanish.txt")
        parola_corretta = self.replaceChars(words)
        lista = dic.loadDictionary()
        presente = False
        for parole in lista:
            parola_dizionario = self.replaceChars(parole)
            if parola_dizionario.__eq__(parola_corretta):
                presente = True
                ritorno = rw.RichWord(parola_corretta, True)
        if presente is not True:
            ritorno = rw.RichWord(parola_corretta, False)
        return ritorno

    def ricercaDicotomica(self, words, language):
        if language == "italian":
            dic = dc.Dictionary("Italian.txt")
        elif language == "english":
            dic = dc.Dictionary("English.txt")
        elif language == "spanish":
            dic = dc.Dictionary("Spanish.txt")
        parola_corretta = self.replaceChars(words)
        lista = dic.loadDictionary()
        presente = False
        indice = int(len(lista) / 2)
        if (lista[indice] == parola_corretta):
            presente = True

    def replaceChars(self, text):
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
