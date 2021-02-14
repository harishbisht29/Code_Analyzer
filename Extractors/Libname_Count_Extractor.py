import re
from SAS_Extractor import SAS_Extractor

class Libname_Count_Extractor(SAS_Extractor):
    def __init__(self):
        self.name= "Libname Counts"
        self.extract_pattern= re.compile("\s*LIBNAME\s+\w+", re.IGNORECASE)

    def extract(self, content):
        count= len(re.findall(self.extract_pattern, content))
        return {
            self.name: count
        }
        
        
if __name__ == "__main__":
    print("-----------------Libname_Count_Extractor.py------------------")
    lce= Libname_Count_Extractor()
    print(lce.extract("LIBNAME harish; LIBNAME neeta;"))
    print("----------------------------------------------")

