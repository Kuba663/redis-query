from RedisQuery import Lexer
from RedisQuery import Parser
from RedisQuery import ParserState
import json
class RedisQuery():
    def __init__(self,host = 'localhost',port = 6379):
        self.lexer = Lexer.Lexer().get_lexer()
        self.parser = Parser.Parser(Parser.RedisQuery.AST.Client(encoder=json.JSONEncoder,decoder=json.JSONDecoder,host=host,port=port)).get_parser()
        self.host = host
        self.port = port
        pass
    def query(self,query):
        return self.parser.parse(self.lexer.lex(query),state=ParserState.ParserState(self.host,self.port)).eval()
