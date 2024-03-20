class Dictionary:
    def _init_(self, nomeFile):
        self.nomeFile = nomeFile


    def loadDictionary(self):
        lista = []
        with open(self.nomeFile, 'r') as f:
            lines = f.readlines()
        for l in lines:
            lista.append(l.splitlines()[0])
        return lista

    def printAll(self):
        for parola in self.dict:
            return parola


    @property
    def dict(self):
        return self.loadDictionary()