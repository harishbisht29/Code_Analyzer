from SAS_Code import SAS_Code
from Extractors import Extractor_Engine

class SAS_Analyzer:
    def __init__(self, scode):
        self.sas_code= scode
        self.extractor = Extractor_Engine(self.sas_code.getCleanCode())

    def analyze(self):
        self.extractor.start()
if __name__ == "__main__":
    print("-----------------SAS_Analyzer.py------------------")
    scode= SAS_Code("program", "Program.sas")
    analyzer= SAS_Analyzer(scode)
    analyzer.analyze()
    print("----------------------------------------------")
