import my_token as t

IGNORE = {" ","\n","\t"}
DIGITS = {"0","1","2","3","4","5","6","7","8","9"}
BIN_OPS = {"+","-","*","/"}

class Parser:
    def __init__(self,text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def generate_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in IGNORE:
                self.advance()
            elif self.current_char in DIGITS:
                self.tokens.append(self.make_number())
                self.advance()
            elif self.current_char in BIN_OPS:
                self.tokens.append(t.Token(t.TT_BINOP,self.current_char))
                self.advance()

    def make_word(self):
        pass

    def make_number(self):
        pass
