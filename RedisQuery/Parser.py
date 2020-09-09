from rply import ParserGenerator
import RedisQuery
class Parser(object):
    """description of class"""
    pg = ParserGenerator(["STRING","ID","SELECT","FROM","OPEN_CLAUSE","CLOSE_CLAUSE","CITE","INSERT","INTO","CREATE","DOCUMENT","AT","WHERE","IS","COMMA","TEMPLATE"])
    def __init__(self,client: Client):
        self.client = client
        pass
    @pg.production('expression: CITE STRING CITE')
    def expression_string(p):
        return RedisQuery.AST.String(p[1].getstr())
    @pg.production('expression: PATH OPEN_CLAUSE expression CLOSE_CLAUSE')
    def expression_path(p):
        return RedisQuery.AST.Path(p[2])
    @pg.production('statement: CREATE TEMPLATE expression OPEN_CLAUSE expression CLOSE_CLAUSE')
    @pg.production('statement: CREATE DOCUMENT expression OPEN_CLAUSE expression CLOSE_CLAUSE AT expression')
    @pg.production('statement: CREATE DOCUMENT expression FROM expression AT expression WHERE expression')
    def statement_create(p):
        if p[1].gettokentype() == 'DOCUMENT':
            if p[3].gettokentype() == 'FROM':
                return RedisQuery.AST.Create(self.client,RedisQuery.AST.CreateType.BASED,p[6],p[2],p[8])
            else:
                return RedisQuery.AST.Create(self.client,RedisQuery.AST.CreateType.DOCUMENT,p[7],p[2],p[4])
        elif p[1].gettokentype() == 'TEMPLATE':
            return RedisQuery.AST.Create(self.client,RedisQuery.AST.CreateType.TEMPLATE,p[7],p[2],p[4])
        else:
            return AssertionError()
    @pg.production('statement: SELECT expression FROM expression')
    def statement_select(p):
        return RedisQuery.AST.Select(self.client,p[3],p[1])
    @pg.production('statement: INSERT expression INTO expression')
    def statement_insert(p):
        return RedisQuery.AST.Insert(self.client,p[3],p[1])
    def get_parser(self):
        return self.pg.build()
