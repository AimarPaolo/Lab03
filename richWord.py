class RichWord:
    def _init_(self, parola,corretta):
        self.parola = parola
        self._corretta = corretta #this is a bool

    @property
    def corretta(self):
        return self._corretta

    @corretta.setter
    def corretta(self, boolValue):
        self._corretta = boolValue

    def _str_(self):
        return self._parola