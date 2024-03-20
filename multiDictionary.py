import dictionary as dc
import richWord as rw
import spellchecker as s

class MultiDictionary:

    def _init_(self, dictitalian =[], dictenglish=[], dictspanish=[]):
        self._dictitalian = dictitalian
        self._dictenglish = dictenglish
        self._dictspanish = dictspanish


    def printDic(self, language):
        if language=="italian":
            dic= dc.Dictionary("Italian.txt")
            dic.printAll()
        elif language == "english":
            dic = dc.Dictionary("English.txt")
            dic.printAll()
        elif language == "spanish":
            dic = dc.Dictionary("Spanish.txt")
            dic.printAll()




    def searchWord(self, words, language):
        dic=None
        if language == "italian":
            dic = dc.Dictionary("Italian.txt")
           # lista=d.loadDictionary(".txt")
        elif language == "english":
            dic= dc.Dictionary("English.txt")
           # lista= d.loadDictionary("English.txt")
        elif language == "spanish":
            dic= dc.Dictionary("Spanish.txt")
            # lista=d.loadDictionary("Spanish.txt")
        words = s.replaceChars(words)
        lista = dic.loadDictionary()
        presente = False
        for parole in lista:
            parole = s.replaceChars(parole)
            if parole.__eq__(words):
                presente = True
                ritorno = rw.RichWord(words, presente)
        if presente is not True:
            ritorno = rw.RichWord(words, presente)
        return ritorno