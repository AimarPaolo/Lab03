class Dictionary:
    def __init__(self, nomeFile):
        self.nomeFile = nomeFile

    def loadDictionary(self):
        lista = []
        with open(self.nomeFile, 'r') as f:
            lines = f.readlines()
        for li in lines:
            lista.append(li.splitlines()[0])
        return lista

    def printAll(self):
        for parola in self.dict:
            return parola

    @property
    def dict(self):
        return self.loadDictionary()
