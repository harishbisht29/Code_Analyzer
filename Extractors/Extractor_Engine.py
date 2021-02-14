from . import Libname_Count_Extractor
from . import Proc_Count_Extractor

class Extractor_Engine:
    def __init__(self, content):
        # Register all the extractors here.
        self.content= content
        self.extractors= [
            Libname_Count_Extractor(),
            Proc_Count_Extractor()
        ]
    def start(self):
        for e in self.extractors:
            print(e.extract(self.content))

if __name__ == "__main__":
    print("-----------------Extractor_Engine.py------------------")
    engine= Extractor_Engine("LIBNAME harish; Proc harish;")
    engine.start()
    print("----------------------------------------------")
