import apicalls

class DataDictionary():
    def __init__(self):
        self.races = apicalls.getRaceData()

    def getRaceData(self):
        return self.races