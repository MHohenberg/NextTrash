
class AbfallTyp:
        name = ""
        datum = arrow.utcnow().shift(years = 1)
        everChanged = False

        def __init__(self, name):
                self.name = name

        def neuesDatum(self, datum):
            if datum < self.datum:
                self.everChanged = True
                self.datum = datum
                                                                            
