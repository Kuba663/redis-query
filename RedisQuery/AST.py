from rejson import Client, Path
import json
from rply.token import BaseBox
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
class Create(BaseBox):
    def __init__(self,client : Client,path : Path,name : String,value : String):
        self.client = client
        self.path = path
        self.name = name
        self.value = value
        pass
    def eval(self):
        self.client.jsonset(self.name.eval(),self.path.eval(),json.loads(self.value.eval()),nx=True)
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