# import module sys to get the type of exception.
import sys
import re
class SAS_Code:
    def __init__(self,name="",location=""):
        try:
            with open(location) as c:
                self.contents= c.read()
            self.number_of_lines= self.contents.count("\n")+1
            self.name= name
            self.location= location
        except :
            print("Oops!", sys.exc_info()[0], "occured.")
            sys.exit(1)
            
    def getCleanCode(self):
        c_code= re.sub(re.compile("/\*.*?\*/", re.DOTALL), "", self.contents)
        c_code= re.sub(re.compile("\s+"), " ", c_code)
        c_code= re.sub(re.compile(";"), ";\n", c_code)
        return c_code

    def createCleanCodeFile(self, fname):
        c_code= self.getCleanCode()
        with open(fname,"w") as c:
            c.write(c_code)

    def __str__(self):
        return self.__dict__.__str__()

if __name__ == "__main__":
    print("-----------------SAS_Code.py------------------")
    code= SAS_Code("program", "Program.sas")
    code.createCleanCodeFile("clean_code.sas")
    # print(code.__dict__)
    print("----------------------------------------------")