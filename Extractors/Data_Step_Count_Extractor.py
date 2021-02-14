import re
from SAS_Extractor import SAS_Extractor

class Data_Step_Count_Extractor(SAS_Extractor):
    def __init__(self):
        self.name= "Datastep Counts"
        self.extract_pattern= re.compile(r"\s*Data\s+(\w+)", re.IGNORECASE)

    def extract(self, content):
        data_stmts= re.findall(self.extract_pattern, content)
        total_count= len(data_stmts)
        null_count= 0
        for d in data_stmts:
            if d.upper() == "_NULL_":
                null_count +=1

        return {
            self.name: {"total":total_count,
            "null_count":null_count
            }
        }
        
        
if __name__ == "__main__":
    print("-----------------Data_Step_Count_Extractor.py------------------")
    lce= Data_Step_Count_Extractor()
    print(lce.extract("Data harish; Data neeta; Data _NULL_;"))
    print("----------------------------------------------")

