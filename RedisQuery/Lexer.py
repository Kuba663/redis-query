from rply import LexerGenerator
class Lexer(object):
    """description of class"""
    def __init__(self):
        self.lexer = LexerGenerator()
        pass
    def _add_tokens(self):
        self.lexer.add("CHAR",r'\w')
        self.lexer.add("NUMBER",r'\d+')
        self.lexer.add("STRING",r'\w*')
        self.lexer.add("ID",r'\w+')
        self.lexer.add("SELECT",r'SELECT')
        self.lexer.add("ASTERISK",r'\*')
        self.lexer.add("FROM",r'FROM')
        self.lexer.add("WHERE",r'WHERE')
        self.lexer.add("PATH",r'PATH')
        self.lexer.add("OPEN_CLAUSE",r'\(')
        self.lexer.add("CLOSE_CLAUSE",r'\)')
        self.lexer.add("CITE",r'\'')
        self.lexer.add("INSERT",r'INSERT')
        self.lexer.add("INTO",r'INTO')
        self.lexer.add("CREATE",r'CREATE')
        self.lexer.add("DOCUMENT",r'DOCUMENT')
        self.lexer.add("AT",r'AT')
        self.lexer.ignore('\s+')
        pass
    def get_lexer(self):
        _add_tokens()
        return self.lexer.build()