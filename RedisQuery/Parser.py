from rply import ParserGenerator
import RedisQuery
class Parser(object):
    """description of class"""
    pg = ParserGenerator(["STRING","ID","SELECT","FROM","OPEN_CLAUSE","CLOSE_CLAUSE","CITE","INSERT","INTO","CREATE","DOCUMENT","AT"])
    def __init__(self,client: Client):
        self.client = client
        pass
    @pg.production('expression: CITE STRING CITE')
    def expression_string(p):
        return RedisQuery.AST.String(p[1].getstr())
    @pg.production('expression: PATH OPEN_CLAUSE expression CLOSE_CLAUSE')
    def expression_path(p):
        return RedisQuery.AST.Path(p[2])
    @pg.production('statement: CREATE DOCUMENT expression OPEN_CLAUSE expression CLOSE_CLAUSE AT expression')
    def statement_create(p):
        return RedisQuery.AST.Create(self.client,p[7],p[2],p[4])
    @pg.production('statement: SELECT expression FROM expression')
    def statement_select(p):
        return RedisQuery.AST.Select(self.client,p[3],p[1])
    @pg.production('statement: INSERT expression INTO expression')
    def statement_insert(p):
        return RedisQuery.AST.Insert(self.client,p[3],p[1])
    def get_parser(self):
        return self.pg.build()
