from rejson import Client, Path
import json
from rply.token import BaseBox
from enum import Enum
class String(BaseBox):
    def __init__(self,value):
        self.value = value
        pass
    def eval(self):
        return value
    pass
class Path(BaseBox):
    def __init__(self,path : String):
        self.path = path
        pass
    def eval(self):
        if (self.path.eval() != 'ROOT'):    
            return Path(self.path.eval())
        else:
            return Path.rootPath()
    pass
class CreateType(Enum):
    DOCUMENT = 1
    TEMPLATE = 2
    BASED = 3
    pass
class Create(BaseBox):
    def __init__(self,client : Client,type : CreateType,path : Path,name : String,value : String):
        self.client = client
        self.type = type
        self.path = path
        self.name = name
        self.value = value
        pass
    def eval(self):
        if self.type == CreateType.DOCUMENT:
            self.client.jsonset(self.name.eval(),self.path.eval(),json.loads(self.value.eval()),nx=True)
        elif self.type == CreateType.TEMPLATE:
            f = open("templates/" + self.name + ".json","w+")
            f.write(self.value)
            f.close()
        elif self.type == CreateType.BASED:
            temp = json.dumps(open("templates/" + self.name + ".json","r").read())
            i = 0
            values =  tuple(self.value.eval().split(';'))
            for key in json.loads(temp):
                temp[key] = values[i]
                pass
            self.client.jsonset(self.name.eval(),self.path.eval(),temp,nx=True)
        else:
            return AssertionError()
        pass
    pass
class Select(BaseBox):
    def __init__(self,client : Client,path : Path, what : String):
        self.client = client
        self.path = path
        self.what = what
        pass
    def eval(self):
        return self.client.jsonget(self.what.eval(),self.path.eval(),no_escape=True)
    pass
class Insert(BaseBox):
    def __init__(self,client : Client,path : Path,name : String,value : String):
        self.client = client
        self.path = path
        self.name = name
        self.value = value
        pass
    def eval(self):
        self.client.jsonset(self.name.eval(),self.path.eval(),json.loads(self.value.eval()),xx=True)
        pass
    pass
