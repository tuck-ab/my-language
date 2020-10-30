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
            elif self.current_char in BIN_OPS:
                self.tokens.append(t.Token(t.TT_BINOP,self.current_char))
            elif self.current_char == "(":
                self.tokens.append(t.Token(t.TT_LB))
            elif self.current_char == ")":
                self.tokens.append(t.Token(t.TT_RB))
            elif self.current_char == "{":
                self.tokens.append(t.Token(t.TT_LCB))
            elif self.current_char == "}":
                self.tokens.append(t.Token(t.TT_RCB))
            elif self.current_char == "[":
                self.tokens.append(t.Token(t.TT_LSB))
            elif self.current_char == "]":
                self.tokens.append(t.Token(t.TT_RSB))

            self.advance()

    def make_word(self):
        pass

    def make_number(self):
        current_num = ""

        while self.current_char in DIGITS:
            current_num += self.current_char
            self.advance()

        return t.Token(t.TT_INTLIT,current_num)
