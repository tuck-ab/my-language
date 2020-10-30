######################################
##  Tokens
######################################

TT_INTLIT = "INTLIT"      ## Integer Literal
TT_ID     = "ID"          ## Identifier
TT_EOF    = "EOF"         ## End of File
TT_BOOLOP = "BOOLOP"      ## Boolean Opperation
TT_BINOP  = "BINOP"       ## Binary Opperation
TT_EOL    = ";"           ## End of Line

TT_if     = "if"          ## 'if' keyword
TT_while  = "while"       ## 'while' keyword
TT_return = "return"      ## 'return' keyword
TT_var    = "var"         ## 'var' keyword
TT_assign = "="           ## assigning variables

## -- Boolean operations
# TT_eq  = "=="
# TT_gt  = ">"
# TT_lt  = "<"
# TT_gte = ">="
# TT_lte = "<="
#
# TT_and = "&"
# TT_or  = "|"

TT_LB  = "("
TT_RB  = ")"
TT_LCB = "{"
TT_RCB = "}"
TT_LSB = "["
TT_RSB = "]"

## -- Binary operations
# TT_PLUS = "+"
# TT_MINUS = "-"
# TT_MULT = "*"
# TT_DIV = "/"


## -- Token object
class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __str__(self):
        if self.value:
            return "{" + str(self.type) + ":" + str(self.value) + "}"
        else:
            return "{" + str(self.type) + "}"
