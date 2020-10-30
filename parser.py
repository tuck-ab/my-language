import token as t

DIGITS = set([str(i) for i in range(10)])

class Parser:
    def __init__(self,text):
        self.text = text
        self.pos = -1
        self.current_char = None

        self.tokens = []

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_word(self):
        pass

    def make_number(self):
        pass
