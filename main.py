from enum import Enum, auto
from functools import wraps
import pickle

import os
os.environ["PATH"] += os.pathsep + 'C:/Users/Majkic/PycharmProjects/pythonProject/venv/Lib/site-packages/graphviz'
import re
class Class(Enum):
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    FWDSLASH = auto()
    PERCENT = auto()

    OR = auto()
    AND = auto()
    NOT = auto()
    XOR = auto()

    EQ = auto()
    EQSIGN = auto()
    NEQ = auto()
    LT = auto()
    GT = auto()
    LTE = auto()
    GTE = auto()

    LPAREN = auto()
    RPAREN = auto()
    LBRACKET = auto()
    RBRACKET = auto()
    LBRACE = auto()
    RBRACE = auto()

    ASSIGN = auto()
    SEMICOLON = auto()
    COMMA = auto()
    DOT = auto()
    COLON = auto()

    TYPE = auto()
    INT = auto()
    CHAR = auto()
    STRING = auto()
    VAR = auto()
    REAL = auto()
    BOOLEAN = auto()

    IF = auto()
    ELSE = auto()
    WHILE = auto()
    FOR = auto()
    BEGIN = auto()
    END = auto()
    PROCEDURE = auto()
    FUNCTION = auto()
    DO = auto()
    TO = auto()
    DOWNTO = auto()
    PROGRAM = auto()
    ARRAY = auto()
    OF = auto()
    THEN = auto()
    EXIT = auto()
    MOD = auto()
    DIV = auto()
    CASE = auto()
    CONST = auto()
    IN = auto()
    NIL = auto()
    REPEAT = auto()
    UNTIL = auto()
    TRUE = auto()
    FALSE = auto()

    BREAK = auto()
    CONTINUE = auto()
    RETURN = auto()

    ID = auto()
    EOF = auto()


class Token:
    def __init__(self, class_, lexeme):
        self.class_ = class_
        self.lexeme = lexeme

    def __str__(self):
        return "<{} {}>".format(self.class_, self.lexeme)


class Lexer:
    def __init__(self, text):
        self.text = text
        self.len = len(text)
        self.pos = -1

    def read_space(self):
        while self.pos + 1 < self.len and self.text[self.pos + 1].isspace():
            self.next_char()

    def read_int(self):
        lexeme = self.text[self.pos]
        while self.pos + 1 < self.len and self.text[self.pos + 1].isdigit():
            lexeme += self.next_char()

        return int(lexeme)

    def read_real(self):
        lexeme = self.text[self.pos]
        while self.pos + 1 < self.len and self.text[self.pos + 1].isdigit():
            lexeme += self.next_char()
        lexeme += self.next_char()
        while self.pos + 1 < self.len and self.text[self.pos + 1].isdigit():
            lexeme += self.next_char()

        print(lexeme)

        return float(lexeme)

    def read_number(self):
        lexeme = self.text[self.pos]
        while self.pos + 2 < self.len and self.text[self.pos + 1].isdigit():
            lexeme += self.next_char()
        test = self.text[self.pos + 1]
        test1 = self.text[self.pos + 2]
        if test == '.' and test1.isnumeric():
            lexeme += self.next_char()
            while self.pos + 2 < self.len and self.text[self.pos + 1].isdigit():
                lexeme += self.next_char()
            return float(lexeme)
        else:
            return int(lexeme)

    def read_char(self):
        self.pos += 1
        lexeme = self.text[self.pos]
        self.pos += 1
        return lexeme

    def read_string(self):
        lexeme = ''
        while self.pos + 1 < self.len and self.text[self.pos + 1] != '\'':
            lexeme += self.next_char()
        self.pos += 1
        return lexeme

    def read_keyword(self):
        lexeme = self.text[self.pos]
        while self.pos + 1 < self.len and self.text[self.pos + 1].isalnum() or self.text[self.pos + 1] == '_':
            lexeme += self.next_char()
        if lexeme == 'if':
            return Token(Class.IF, lexeme)
        elif lexeme == 'else':
            return Token(Class.ELSE, lexeme)
        elif lexeme == 'while':
            return Token(Class.WHILE, lexeme)
        elif lexeme == 'for':
            return Token(Class.FOR, lexeme)
        elif lexeme == 'break':
            return Token(Class.BREAK, lexeme)
        elif lexeme == 'continue':
            return Token(Class.CONTINUE, lexeme)
        elif lexeme == 'integer' or lexeme == 'char':
            return Token(Class.TYPE, lexeme)
        elif lexeme == 'begin':
            return Token(Class.BEGIN, lexeme)
        elif lexeme == 'end':
            return Token(Class.END, lexeme)
        elif lexeme == 'var':
            return Token(Class.VAR, lexeme)
        elif lexeme == 'procedure':
            return Token(Class.PROCEDURE, lexeme)
        elif lexeme == 'function':
            return Token(Class.FUNCTION, lexeme)
        elif lexeme == 'to':
            return Token(Class.TO, lexeme)
        elif lexeme == 'do':
            return Token(Class.DO, lexeme)
        elif lexeme == 'program':
            return Token(Class.PROGRAM, lexeme)
        elif lexeme == 'array':
            return Token(Class.ARRAY, lexeme)
        elif lexeme == 'of':
            return Token(Class.OF, lexeme)
        elif lexeme == 'then':
            return Token(Class.THEN, lexeme)
        elif lexeme == 'exit':
            return Token(Class.EXIT, lexeme)
        elif lexeme == 'mod':
            return Token(Class.MOD, lexeme)
        elif lexeme == 'div':
            return Token(Class.DIV, lexeme)
        elif lexeme == 'or':
            return Token(Class.OR, lexeme)
        elif lexeme == 'real':
            return Token(Class.TYPE, lexeme)
        elif lexeme == 'const':
            return Token(Class.CONST, lexeme)
        elif lexeme == 'and':
            return Token(Class.AND, lexeme)
        elif lexeme == 'case':
            return Token(Class.CASE, lexeme)
        elif lexeme == 'in':
            return Token(Class.IN, lexeme)
        elif lexeme == 'nil':
            return Token(Class.NIL, lexeme)
        elif lexeme == 'repeat':
            return Token(Class.REPEAT, lexeme)
        elif lexeme == 'until':
            return Token(Class.UNTIL, lexeme)
        elif lexeme == 'boolean':
            return Token(Class.TYPE, lexeme)
        elif lexeme == 'xor':
            return Token(Class.XOR, lexeme)
        elif lexeme == 'string':
            return Token(Class.TYPE, lexeme)
        elif lexeme == 'downto':
            return Token(Class.DOWNTO, lexeme)
        elif lexeme == 'true':
            return Token(Class.TRUE, lexeme)
        elif lexeme == 'false':
            return Token(Class.FALSE, lexeme)
        elif lexeme == 'true' or lexeme == 'false':
            return Token(Class.BOOLEAN, lexeme)

        return Token(Class.ID, lexeme)

    def next_char(self):
        self.pos += 1
        if self.pos >= self.len:
            return None
        return self.text[self.pos]

    def next_token(self):
        self.read_space()
        curr = self.next_char()
        if curr is None:
            return Token(Class.EOF, curr)
        token = None
        if curr.isalpha() or curr == '_':
            token = self.read_keyword()
        elif curr.isdigit():
            number = self.read_number()
            if isinstance(number, int):
                token = Token(Class.INT, number)
            elif isinstance(number, float):
                token = Token(Class.REAL, number)
        elif curr == '\'':
            lexeme = self.read_string()
            if len(lexeme) == 1:
                token = Token(Class.CHAR, lexeme)
            else:
                token = Token(Class.STRING, lexeme)
        elif curr == '+':
            token = Token(Class.PLUS, curr)
        elif curr == '-':
            token = Token(Class.MINUS, curr)
        elif curr == '*':
            token = Token(Class.STAR, curr)
        elif curr == '/':
            token = Token(Class.FWDSLASH, curr)
        elif curr == '%':
            token = Token(Class.PERCENT, curr)
        elif curr == '|':
            curr = self.next_char()
            if curr == '|':
                token = Token(Class.OR, '||')
            else:
                self.die(curr)
        elif curr == '!':
            curr = self.next_char()
            token = Token(Class.NOT, '!')
        elif curr == '=':
            curr = self.next_char()
            if curr == '=':
                token = Token(Class.EQ, '==')
            else:
                token = Token(Class.EQSIGN, '=')
        elif curr == '<':
            curr = self.next_char()
            if curr == '=':
                token = Token(Class.LTE, '<=')
            elif curr == ">":
                token = Token(Class.NEQ, "<>")
            else:
                token = Token(Class.LT, '<')
                self.pos -= 1
        elif curr == '>':
            curr = self.next_char()
            if curr == '=':
                token = Token(Class.GTE, '>=')
            else:
                token = Token(Class.GT, '>')
                self.pos -= 1
        elif curr == '(':
            token = Token(Class.LPAREN, curr)
        elif curr == ')':
            token = Token(Class.RPAREN, curr)
        elif curr == '[':
            token = Token(Class.LBRACKET, curr)
        elif curr == ']':
            token = Token(Class.RBRACKET, curr)
        elif curr == '{':
            token = Token(Class.LBRACE, curr)
        elif curr == '}':
            token = Token(Class.RBRACE, curr)
        elif curr == ';':
            token = Token(Class.SEMICOLON, curr)
        elif curr == ',':
            token = Token(Class.COMMA, curr)
        elif curr == '.':
            token = Token(Class.DOT, curr)
        elif curr == ':':
            token = Token(Class.COLON, curr)
            curr = self.text[self.pos+1]
            if curr == '=':
                token = Token(Class.ASSIGN, ':=')
                self.next_char()
        else:
            self.die(curr)
        return token

    def lex(self):
        tokens = []
        while True:
            curr = self.next_token()
            tokens.append(curr)
            if curr.class_ == Class.EOF:
                break
        return tokens

    def die(self, char):
        raise SystemExit("Unexpected character: {}".format(char))


class Node():
    pass


class Program(Node):
    def __init__(self, nodes):
        self.nodes = nodes


class Decl(Node):
    def __init__(self, type_, id_):
        self.type_ = type_
        self.id_ = id_


class ArrayDecl(Node):
    def __init__(self, type_, id_, low, high, elems):
        self.type_ = type_
        self.id_ = id_
        self.low = low
        self.high = high
        self.elems = elems


class ArrayElem(Node):
    def __init__(self, id_, index):
        self.id_ = id_
        self.index = index


class Assign(Node):
    def __init__(self, id_, expr):
        self.id_ = id_
        self.expr = expr


class If(Node):
    def __init__(self, cond, true, false):
        self.cond = cond
        self.true = true
        self.false = false


class While(Node):
    def __init__(self, cond, block):
        self.cond = cond
        self.block = block


class For(Node):
    def __init__(self, init, cond, block, where):
        self.init = init
        self.cond = cond
        self.block = block
        self.where = where


class RepeatUntil(Node):
    def __init__(self, cond, block):
        self.cond = cond
        self.block = block


class FuncImpl(Node):
    def __init__(self, type_, id_, params, block, var):
        self.type_ = type_
        self.id_ = id_
        self.params = params
        self.block = block
        self.var = var


class FuncProcCall(Node):
    def __init__(self, id_, args):
        self.id_ = id_
        self.args = args


class ProcImpl(Node):
    def __init__(self, id_, params, block, var):
        self.id_ = id_
        self.params = params
        self.block = block
        self.var = var


class Block(Node):
    def __init__(self, nodes):
        self.nodes = nodes


class Params(Node):
    def __init__(self, params):
        self.params = params


class Variables(Node):
    def __init__(self, vars):
        self.vars = vars


class Args(Node):
    def __init__(self, args):
        self.args = args


class Elems(Node):
    def __init__(self, elems):
        self.elems = elems


class Break(Node):
    pass


class Continue(Node):
    pass


class Exit(Node):
    def __init__(self, value):
        self.value = value


class Type(Node):
    def __init__(self, value):
        self.value = value


class TypeString(Node):
    def __init__(self, value, size):
        self.value = value
        self.size = size


class Int(Node):
    def __init__(self, value):
        self.value = value


class Char(Node):
    def __init__(self, value):
        self.value = value


class String(Node):
    def __init__(self, value):
        self.value = value


class Real(Node):
    def __init__(self, value):
        self.value = value


class Boolean(Node):
    def __init__(self, value):
        self.value = value


class Id(Node):
    def __init__(self, value):
        self.value = value


class BinOp(Node):
    def __init__(self, symbol, first, second):
        self.symbol = symbol
        self.first = first
        self.second = second


class UnOp(Node):
    def __init__(self, symbol, first):
        self.symbol = symbol
        self.first = first


class Where(Node):
    def __init__(self, str):
        self.value = str


class BoolValue(Node):
    def __init__(self, str):
        self.value = str

class FormattedArg(Node):
    def __init__(self, args, left, right):
        self.args = args
        self.left = left
        self.right = right

class Visitor():
    def visit(self, parent, node):
        method = 'visit_' + type(node).__name__
        visitor = getattr(self, method, self.die)
        return visitor(parent, node)

    def die(self, parent, node):
        method = 'visit_' + type(node).__name__
        raise SystemExit("Missing method: {}".format(method))

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.curr = tokens.pop(0)
        self.prev = None

    def restorable(call):
        @wraps(call)
        def wrapper(self, *args, **kwargs):
            state = pickle.dumps(self.__dict__)
            result = call(self, *args, **kwargs)
            self.__dict__ = pickle.loads(state)
            return result

        return wrapper

    def eat(self, class_):
        if self.curr.class_ == class_:
            self.prev = self.curr
            self.curr = self.tokens.pop(0)
        else:
            self.die_type(class_.name, self.curr.class_.name)

    def program(self):  # DONE
        nodes = []
        while self.curr.class_ != Class.EOF:
            if self.curr.class_ == Class.PROCEDURE:
                nodes.append(self.proc())
            elif self.curr.class_ == Class.FUNCTION:
                nodes.append(self.func())
            elif self.curr.class_ == Class.VAR:
                self.eat(Class.VAR)
                nodes.append(self.variables())
            elif self.curr.class_ == Class.BEGIN:
                self.eat(Class.BEGIN)
                nodes.append(self.block())
                self.eat(Class.END)
                self.eat(Class.DOT)
            else:
                self.die_deriv(self.program.__name__)
        return Program(nodes)

    def paramsVar(self):
        vars = []
        lista = []
        while self.curr.class_ != Class.RPAREN:
            if (self.curr.class_ == Class.ID):
                lista.append(self.curr.lexeme)
                self.eat(Class.ID)

            elif (self.curr.class_ == Class.COMMA):
                self.eat(Class.COMMA)

            elif (self.curr.class_ == Class.COLON):
                self.eat(Class.COLON)
                tip = self.type_()
                for x in lista:
                    id = Id(x)
                    vars.append(Decl(tip, id))

                lista.clear()

            if self.curr.class_ == Class.SEMICOLON:
                self.eat(Class.SEMICOLON)

        return Params(vars)

    def variables(self):  # DONE
        vars = []
        lista = []
        while self.curr.class_ != Class.BEGIN:
            if (self.curr.class_ == Class.ID):
                lista.append(self.curr.lexeme)
                self.eat(Class.ID)

            elif (self.curr.class_ == Class.COMMA):
                self.eat(Class.COMMA)

            elif (self.curr.class_ == Class.COLON):
                self.eat(Class.COLON)

                if self.curr.class_ == Class.TYPE:
                    tip = self.type_()
                    for x in lista:
                        id = Id(x)
                        vars.append(Decl(tip, id))
                    self.eat(Class.SEMICOLON)

                elif self.curr.class_ == Class.ARRAY:
                    self.eat(Class.ARRAY)
                    self.eat(Class.LBRACKET)
                    low = Int(self.curr.lexeme)
                    self.eat(Class.INT)
                    self.eat(Class.DOT)
                    self.eat(Class.DOT)
                    high = Int(self.curr.lexeme)
                    self.eat(Class.INT)
                    self.eat(Class.RBRACKET)
                    self.eat(Class.OF)
                    tip = self.type_()
                    elems = None
                    if self.curr.class_ == Class.SEMICOLON:
                        vars.append(ArrayDecl(tip, Id(lista[0]), low, high, elems))
                        self.eat(Class.SEMICOLON)
                    elif (self.curr.class_ == Class.EQSIGN):
                        self.eat(Class.EQSIGN)
                        self.eat(Class.LPAREN)
                        elems = self.elems()
                        self.eat(Class.RPAREN)
                        self.eat(Class.SEMICOLON)
                        vars.append(ArrayDecl(tip, Id(lista[0]), low, high, elems))

                lista.clear()

        return Variables(vars)

    def proc(self):  # DONE
        self.eat(Class.PROCEDURE)
        id_ = self.idDefines()
        self.eat(Class.LPAREN)
        params = self.paramsVar()
        self.eat(Class.RPAREN)
        self.eat(Class.SEMICOLON)
        vars = []
        if (self.curr.class_ == Class.VAR):
            self.eat(Class.VAR)
            vars = self.variables()
        if not vars:
            vars = Variables(vars)
        self.eat(Class.BEGIN)
        block = self.block()
        self.eat(Class.END)
        self.eat(Class.SEMICOLON)

        return ProcImpl(id_, params, block, vars)

    def func(self):  # DONE
        self.eat(Class.FUNCTION)
        id_ = self.idDefines()
        self.eat(Class.LPAREN)
        params = self.paramsVar()
        self.eat(Class.RPAREN)
        self.eat(Class.COLON)
        type_ = Type(self.curr.lexeme)
        self.eat(Class.TYPE)
        self.eat(Class.SEMICOLON)
        vars = []
        if (self.curr.class_ == Class.VAR):
            self.eat(Class.VAR)
            vars = self.variables()
        if not vars:
            vars = Variables(vars)
        self.eat(Class.BEGIN)
        block = self.block()
        self.eat(Class.END)
        self.eat(Class.SEMICOLON)
        return FuncImpl(type_, id_, params, block, vars)

    def id_(self):  # TODO
        is_array_elem = self.prev.class_ != Class.TYPE
        id_ = Id(self.curr.lexeme)
        self.eat(Class.ID)
        if self.curr.class_ == Class.LPAREN and self.is_func_call():
            self.eat(Class.LPAREN)
            args = self.args()
            self.eat(Class.RPAREN)
            return FuncProcCall(id_, args)
        elif self.curr.class_ == Class.LBRACKET and is_array_elem:
            self.eat(Class.LBRACKET)
            index = self.logic()
            self.eat(Class.RBRACKET)
            id_ = ArrayElem(id_, index)
        if self.curr.class_ == Class.ASSIGN:
            self.eat(Class.ASSIGN)
            logic = self.logic()
            return Assign(id_, logic)
        else:
            return id_

    def idDefines(self):  # TODO
        is_array_elem = self.prev.class_ != Class.TYPE
        id_ = Id(self.curr.lexeme)
        self.eat(Class.ID)
        return id_

    def if_(self):  # DONE
        self.eat(Class.IF)
        cond = self.logic()
        self.eat(Class.THEN)
        self.eat(Class.BEGIN)
        true = self.block()
        self.eat(Class.END)
        false = None
        if self.curr.class_ == Class.ELSE:
            self.eat(Class.ELSE)
            self.eat(Class.BEGIN)
            false = self.block()
            self.eat(Class.END)
        self.eat(Class.SEMICOLON)
        return If(cond, true, false)

    def while_(self):  # DONE
        self.eat(Class.WHILE)
        cond = self.logic()
        self.eat(Class.DO)
        self.eat(Class.BEGIN)
        block = self.block()
        self.eat(Class.END)
        if (self.curr.class_ == Class.SEMICOLON):
            self.eat(Class.SEMICOLON)
        return While(cond, block)

    def for_(self):  # DONE
        self.eat(Class.FOR)
        init = self.id_()
        where = 'to'
        if self.curr.class_ == Class.TO:
            self.eat(Class.TO)
            where = 'to'
        elif self.curr.class_ == Class.DOWNTO:
            self.eat(Class.DOWNTO)
            where = 'downto'
        logic = self.logic()
        self.eat(Class.DO)
        self.eat(Class.BEGIN)
        block = self.block()
        self.eat(Class.END)
        self.eat(Class.SEMICOLON)
        return For(init, logic, block, Where(where))

    def repeat(self):  # DONE
        self.eat(Class.REPEAT)
        block = self.block()
        self.eat(Class.UNTIL)
        cond = self.logic()
        self.eat(Class.SEMICOLON)
        return RepeatUntil(cond, block)

    def block(self):  # DONE
        nodes = []
        while self.curr.class_ != Class.END:
            if self.curr.class_ == Class.VAR:
                self.eat(Class.VAR)
                nodes.append(self.variables())
            elif self.curr.class_ == Class.IF:
                nodes.append(self.if_())
            elif self.curr.class_ == Class.WHILE:
                nodes.append(self.while_())
            elif self.curr.class_ == Class.FOR:
                nodes.append(self.for_())
            elif self.curr.class_ == Class.BREAK:
                nodes.append(self.break_())
            elif self.curr.class_ == Class.CONTINUE:
                nodes.append(self.continue_())
            elif self.curr.class_ == Class.EXIT:
                nodes.append(self.exit_())
            elif self.curr.class_ == Class.REPEAT:
                nodes.append(self.repeat())
            elif self.curr.class_ == Class.ID:
                nodes.append(self.id_())
                self.eat(Class.SEMICOLON)
            elif self.curr.class_ == Class.UNTIL:
                break
            else:
                self.die_deriv(self.block.__name__)
        return Block(nodes)

    def params(self):
        params = []
        while self.curr.class_ != Class.RPAREN:
            params.append(self.variables)

        return Params(params)

    def args(self):
        args = []
        while self.curr.class_ != Class.RPAREN:
            if len(args) > 0:
                self.eat(Class.COMMA)
            logic = self.logic()

            if (self.curr.class_ == Class.COLON):
                self.eat(Class.COLON)
                left = self.expr()
                self.eat(Class.COLON)
                right = self.expr()
                args.append(FormattedArg(logic, left, right))
            else:
                args.append(logic)

        return Args(args);

    def elems(self):
        elems = []
        while self.curr.class_ != Class.RPAREN:
            if len(elems) > 0:
                self.eat(Class.COMMA)
            elems.append(self.logic())
        return Elems(elems)

    def arrayElems(self, low):
        elems = []
        ctr = 0
        while self.curr.class_ != Class.RBRACE:
            if len(elems) > 0:
                self.eat(Class.COMMA)
            elems.append(ArrayElem(self.logic(), ctr + low))
            ctr += 1
        self.eat(Class.RBRACE)
        return Elems(elems)

    def break_(self):
        self.eat(Class.BREAK)
        self.eat(Class.SEMICOLON)
        return Break()

    def exit_(self):
        self.eat(Class.EXIT)
        value = None
        if self.curr.class_ == Class.LPAREN:
            self.eat(Class.LPAREN)
            value = self.logic()
            self.eat(Class.RPAREN)
        self.eat(Class.SEMICOLON)

        return Exit(value)

    def continue_(self):
        self.eat(Class.CONTINUE)
        self.eat(Class.SEMICOLON)
        return Continue()

    def type_(self):
        if (self.curr.lexeme == 'string'):
            tip = self.curr.lexeme
            self.eat(Class.TYPE)
            if (self.curr.class_ == Class.LBRACKET):
                self.eat(Class.LBRACKET)
                size = self.expr()
                self.eat(Class.RBRACKET)
                type_ = TypeString(tip, size)
            else:
             type_ = TypeString(tip, None)
        else:
            type_ = Type(self.curr.lexeme)
            self.eat(Class.TYPE)
        return type_

    def factor(self):
        if self.curr.class_ == Class.INT:
            value = Int(self.curr.lexeme)
            self.eat(Class.INT)
            return value
        elif self.curr.class_ == Class.CHAR:
            value = Char(self.curr.lexeme)
            self.eat(Class.CHAR)
            return value
        elif self.curr.class_ == Class.STRING:
            value = String(self.curr.lexeme)
            self.eat(Class.STRING)
            return value
        elif self.curr.class_ == Class.BOOLEAN:
            value = Boolean(self.curr.lexeme)
            self.eat(Class.BOOLEAN)
            return value
        elif self.curr.class_ == Class.REAL:
            value = Real(self.curr.lexeme)
            self.eat(Class.REAL)
            return value
        elif self.curr.class_ == Class.ID:
            return self.id_()
        elif self.curr.class_ == Class.TRUE:
            self.eat(Class.TRUE)
            return BoolValue('true')
        elif self.curr.class_ == Class.FALSE:
            self.eat(Class.FALSE)
            return BoolValue('false')
        elif self.curr.class_ in [Class.MINUS, Class.NOT]:
            op = self.curr
            self.eat(self.curr.class_)
            first = None
            if self.curr.class_ == Class.LPAREN:
                self.eat(Class.LPAREN)
                first = self.logic()
                self.eat(Class.RPAREN)
            else:
                first = self.factor()
            return UnOp(op.lexeme, first)
        elif self.curr.class_ == Class.LPAREN:
            self.eat(Class.LPAREN)
            first = self.logic()
            self.eat(Class.RPAREN)
            return first
        elif self.curr.class_ == Class.SEMICOLON:
            return None
        else:
            self.die_deriv(self.factor.__name__)

    def term(self):
        first = self.factor()
        while self.curr.class_ in [Class.STAR, Class.FWDSLASH, Class.PERCENT, Class.MOD, Class.DIV]:
            if self.curr.class_ == Class.STAR:
                op = self.curr.lexeme
                self.eat(Class.STAR)
                second = self.factor()
                first = BinOp(op, first, second)
            elif self.curr.class_ == Class.FWDSLASH:
                op = self.curr.lexeme
                self.eat(Class.FWDSLASH)
                second = self.factor()
                first = BinOp(op, first, second)
            elif self.curr.class_ == Class.PERCENT:
                op = self.curr.lexeme
                self.eat(Class.PERCENT)
                second = self.factor()
                first = BinOp(op, first, second)
            elif self.curr.class_ == Class.MOD:
                op = self.curr.lexeme
                self.eat(Class.MOD)
                second = self.factor()
                first = BinOp(op, first, second)
            elif self.curr.class_ == Class.DIV:
                op = self.curr.lexeme
                self.eat(Class.DIV)
                second = self.factor()
                first = BinOp(op, first, second)

        return first

    def expr(self):
        first = self.term()
        while self.curr.class_ in [Class.PLUS, Class.MINUS]:
            if self.curr.class_ == Class.PLUS:
                op = self.curr.lexeme
                self.eat(Class.PLUS)
                second = self.term()
                first = BinOp(op, first, second)
            elif self.curr.class_ == Class.MINUS:
                op = self.curr.lexeme
                self.eat(Class.MINUS)
                second = self.term()
                first = BinOp(op, first, second)
        return first

    def compare(self):
        first = self.expr()
        if self.curr.class_ == Class.EQSIGN:
            op = self.curr.lexeme
            self.eat(Class.EQSIGN)
            second = self.expr()
            return BinOp(op, first, second)
        elif self.curr.class_ == Class.NEQ:
            op = self.curr.lexeme
            self.eat(Class.NEQ)
            second = self.expr()
            return BinOp(op, first, second)
        elif self.curr.class_ == Class.LT:
            op = self.curr.lexeme
            self.eat(Class.LT)
            second = self.expr()
            return BinOp(op, first, second)
        elif self.curr.class_ == Class.GT:
            op = self.curr.lexeme
            self.eat(Class.GT)
            second = self.expr()
            return BinOp(op, first, second)
        elif self.curr.class_ == Class.LTE:
            op = self.curr.lexeme
            self.eat(Class.LTE)
            second = self.expr()
            return BinOp(op, first, second)
        elif self.curr.class_ == Class.GTE:
            op = self.curr.lexeme
            self.eat(Class.GTE)
            second = self.expr()
            return BinOp(op, first, second)
        else:
            return first

    def logic(self):
        first = self.compare()
        if self.curr.class_ == Class.AND:
            op = self.curr.lexeme
            self.eat(Class.AND)
            second = self.compare()
            return BinOp(op, first, second)
        elif self.curr.class_ == Class.OR:
            op = self.curr.lexeme
            self.eat(Class.OR)
            second = self.compare()
            if (self.curr.class_ == Class.AND):
                op2 = self.curr.lexeme
                self.eat(Class.AND)
                third = self.compare()
                return BinOp(op2, BinOp(op, first, second), third)
            return BinOp(op, first, second)
        elif self.curr.class_ == Class.XOR:
            op = self.curr.lexeme
            self.eat(Class.XOR)
            second = self.compare()
            return BinOp(op, first, second)
        else:
            return first




    @restorable
    def is_func_call(self):
        try:
            self.eat(Class.LPAREN)
            self.args()
            self.eat(Class.RPAREN)
            if self.curr.class_ == Class.SEMICOLON:
                self.eat(Class.SEMICOLON)
                return self.curr.class_ != Class.BEGIN
            else:
                return True

        except:
            return True

    def parse(self):
        return self.program()

    def die(self, text):
        raise SystemExit(text)

    def die_deriv(self, fun):
        self.die("Derivation error: {}".format(fun))

    def die_type(self, expected, found):
        self.die("Expected: {}, Found: {}".format(expected, found))

from graphviz import Digraph, Source
from IPython.display import Image

class Grapher(Visitor):
    def __init__(self, ast):
        self.ast = ast
        self._count = 1
        self.dot = Digraph()
        self.dot.node_attr['shape'] = 'box'
        self.dot.node_attr['height'] = '0.1'
        self.dot.edge_attr['arrowsize'] = '0.5'

    def add_node(self, parent, node, name=None):
        node._index = self._count
        self._count += 1
        caption = type(node).__name__
        if name is not None:
            caption = '{} : {}'.format(caption, name)
        self.dot.node('node{}'.format(node._index), caption)
        if parent is not None:
            self.add_edge(parent, node)

    def add_edge(self, parent, node):
        src, dest = parent._index, node._index
        self.dot.edge('node{}'.format(src), 'node{}'.format(dest))

    def visit_Program(self, parent, node):
        self.add_node(parent, node)
        for n in node.nodes:
            self.visit(node, n)

    def visit_Variables(self, parent, node):
        self.add_node(parent, node)
        for n in node.vars:
            self.visit(node, n)

    def visit_FuncImpl(self, parent, node):
        self.add_node(parent, node)
        self.visit(node, node.type_)
        self.visit(node, node.id_)
        self.visit(node, node.params)
        self.visit(node, node.block)
        self.visit(node, node.var)

    def visit_ProcImpl(self, parent, node):
        self.add_node(parent, node)
        self.visit(node, node.id_)
        self.visit(node, node.params)
        self.visit(node, node.block)
        self.visit(node, node.var)

    def visit_Decl(self, parent, node):
        self.add_node(parent, node)
        self.visit(node, node.type_)
        self.visit(node, node.id_)

    def visit_ArrayDecl(self, parent, node):
        self.add_node(parent, node)
        self.visit(node, node.type_)
        self.visit(node, node.id_)
        self.visit(node, node.low)
        self.visit(node, node.high)
        if node.elems is not None:
            self.visit(node, node.elems)

    def visit_RepeatUntil(self, parent, node):
        self.add_node(parent, node)
        self.visit(node, node.cond)
        self.visit(node, node.block)

    def visit_ArrayElem(self, parent, node):
        self.add_node(parent, node)
        self.visit(node, node.id_)
        self.visit(node, node.index)

    def visit_Assign(self, parent, node):
        self.add_node(parent, node)
        self.visit(node, node.id_)
        self.visit(node, node.expr)

    def visit_If(self, parent, node):
        self.add_node(parent, node)
        self.visit(node, node.cond)
        self.visit(node, node.true)
        if node.false is not None:
            self.visit(node, node.false)

    def visit_While(self, parent, node):
        self.add_node(parent, node)
        self.visit(node, node.cond)
        self.visit(node, node.block)

    def visit_For(self, parent, node):
        self.add_node(parent, node)
        self.visit(node, node.init)
        self.visit(node, node.cond)
        self.visit(node, node.block)
        self.visit(node, node.where)

    def visit_FuncProcCall(self, parent, node):
        self.add_node(parent, node)
        self.visit(node, node.id_)
        self.visit(node, node.args)

    def visit_Block(self, parent, node):
        self.add_node(parent, node)
        for n in node.nodes:
            self.visit(node, n)

    def visit_Params(self, parent, node):
        self.add_node(parent, node)
        for p in node.params:
            self.visit(node, p)

    def visit_Args(self, parent, node):
        self.add_node(parent, node)
        for a in node.args:
            self.visit(node, a)

    def visit_Elems(self, parent, node):
        self.add_node(parent, node)
        for e in node.elems:
            self.visit(node, e)

    def visit_Break(self, parent, node):
        self.add_node(parent, node)

    def visit_Continue(self, parent, node):
        self.add_node(parent, node)

    def visit_Exit(self, parent, node):
        self.add_node(parent, node)
        if node.value is not None:
            self.visit(node, node.value)

    def visit_Return(self, parent, node):
        self.add_node(parent, node)
        if node.expr is not None:
            self.visit(node, node.expr)

    def visit_Type(self, parent, node):
        name = node.value
        self.add_node(parent, node, name)

    def visit_TypeString(self, parent, node):
        name = node.value
        self.add_node(parent, node, name)
        if node.size is not None:
            self.visit(node, node.size)

    def visit_Int(self, parent, node):
        name = node.value
        self.add_node(parent, node, name)

    def visit_Char(self, parent, node):
        name = node.value
        self.add_node(parent, node, name)

    def visit_String(self, parent, node):
        name = node.value
        self.add_node(parent, node, name)

    def visit_Real(self, parent, node):
        name = node.value
        self.add_node(parent, node, name)

    def visit_Boolean(self, parent, node):
        name = node.value
        self.add_node(parent, node, name)

    def visit_Id(self, parent, node):
        name = node.value
        self.add_node(parent, node, name)

    def visit_BinOp(self, parent, node):
        name = node.symbol
        self.add_node(parent, node, name)
        self.visit(node, node.first)
        self.visit(node, node.second)

    def visit_UnOp(self, parent, node):
        name = node.symbol
        self.add_node(parent, node, name)
        self.visit(node, node.first)

    def visit_Where(self, parent, node):
        name = node.value
        self.add_node(parent, node, name)

    def visit_BoolValue(self, parent, node):
        name = node.value
        self.add_node(parent, node, name)

    def visit_FormattedArg(self, parent, node):
        self.add_node(parent, node)
        self.visit(node, node.args)
        self.visit(node, node.left)
        self.visit(node, node.right)





    def graph(self):
        self.visit(None, self.ast)
        s = Source(self.dot.source, filename='graph', format='png')
        return s.view()

class Symbol:
    def __init__(self, id_, type_, scope):
        self.id_ = id_
        self.type_ = type_
        self.scope = scope

    def __str__(self):
        return "<{} {} {}>".format(self.id_, self.type_, self.scope)

    def copy(self):
        return Symbol(self.id_, self.type_, self.scope)

class Symbols:
    def __init__(self):
        self.symbols = {}

    def put(self, id_, type_, scope):
        self.symbols[id_] = Symbol(id_, type_, scope)

    def get(self, id_):
        return self.symbols[id_]

    def contains(self, id_):
        return id_ in self.symbols

    def remove(self, id_):
        del self.symbols[id_]

    def __len__(self):
        return len(self.symbols)

    def __str__(self):
        out = ""
        for _, value in self.symbols.items():
            if len(out) > 0:
                out += "\n"
            out += str(value)
        return out

    def __iter__(self):
        return iter(self.symbols.values())

    def __next__(self):
        return next(self.symbols.values())

class Symbolizer(Visitor):
    def __init__(self, ast):
        self.ast = ast

    def visit_Program(self, parent, node):
        node.symbols = Symbols()
        for n in node.nodes:
            self.visit(node, n)

    def visit_Decl(self, parent, node):
        parent.symbols.put(node.id_.value, node.type_.value, id(parent))

    def visit_ArrayDecl(self, parent, node):
        node.symbols = Symbols()
        parent.symbols.put(node.id_.value, node.type_.value + ' array', id(parent))

    def visit_ArrayElem(self, parent, node):
        pass

    def visit_Assign(self, parent, node):
        pass

    def visit_If(self, parent, node):
        self.visit(node, node.true)
        if node.false is not None:
            self.visit(node, node.false)

    def visit_While(self, parent, node):
        self.visit(node, node.block)

    def visit_For(self, parent, node):
        self.visit(node, node.block)

    def visit_RepeatUntil(self, parent, node):
        self.visit(node, node.block)

    def visit_FuncImpl(self, parent, node):
        node.symbols = Symbols()
        parent.symbols.put(node.id_.value, node.type_.value, id(parent))
        node.symbols.put(node.id_.value, node.type_.value, id(parent))
        self.visit(node, node.var)
        self.visit(node, node.block)
        self.visit(node, node.params)

    def visit_ProcImpl(self, parent, node):
        node.symbols = Symbols()
        parent.symbols.put(node.id_.value, 'void', id(parent))
        node.symbols.put(node.id_.value, 'void', id(parent))
        self.visit(node, node.var)
        self.visit(node, node.block)
        self.visit(node, node.params)

    def visit_FuncProcCall(self, parent, node):
        pass

    def visit_Block(self, parent, node):
        node.symbols = Symbols()
        for n in node.nodes:
            self.visit(parent, n)

    def visit_Params(self, parent, node):

        for p in node.params:
            self.visit(parent, p)

    def visit_Variables(self, parent, node):

        for p in node.vars:
            self.visit(parent, p)


    def visit_Args(self, parent, node):
        pass

    def visit_Elems(self, parent, node):
        pass

    def visit_Break(self, parent, node):
        pass

    def visit_Continue(self, parent, node):
        pass

    def visit_Exit(self, parent, node):
        pass

    def visit_TypeString(self, parent, node):
        pass

    def visit_Type(self, parent, node):
        pass

    def visit_Int(self, parent, node):
        pass

    def visit_Char(self, parent, node):
        pass

    def visit_String(self, parent, node):
        pass

    def visit_Real(self, parent, node):
        pass

    def visit_Boolean(self, parent, node):
        pass

    def visit_Id(self, parent, node):
        pass

    def visit_BinOp(self, parent, node):
        pass

    def visit_UnOp(self, parent, node):
        pass

    def visit_Where(self, parent, node):
        pass

    def visit_BoolValue(self, parent, node):
        pass

    def visit_FormattedArg(self, parent, node):
        pass

    def symbolize(self):
        self.visit(None, self.ast)

class Generator(Visitor):
    def __init__(self, ast):
        self.ast = ast
        self.py = ""
        self.level = 0

    def append(self, text):
        self.py += str(text)

    def newline(self):
        self.append('\n')


    def visit_Program(self, parent, node):
        self.append('int main(){')
        self.newline()
        for n in node.nodes:
            if isinstance(n,Variables):
                self.visit(node, n)
            if isinstance(n, Block):
                self.visit(node, n)

        self.newline()
        self.append('}')
        self.newline()

        for n in node.nodes:
            if isinstance(n,ProcImpl):
                self.visit(node, n)
            if isinstance(n, FuncImpl):
                self.visit(node, n)

        pass

    def visit_Decl(self, parent, node):
        self.visit(node, node.type_)
        self.visit(node, node.id_)


    def visit_ArrayDecl(self, parent, node):
        self.visit(node, node.type_)
        self.append('[')
        self.visit(node, node.high)
        self.append( '-' )
        self.visit(node, node.low)
        self.append('] ')
        self.visit(node, node.id_)
        if node.elems is not None:
            self.append(' = {')
            self.visit(node, node.elems)
            self.append('}')

    def visit_ArrayElem(self, parent, node):
        self.visit(node,node.id_)
        self.append('[')
        self.visit(node, node.index)
        self.append(']')

    def visit_Assign(self, parent, node):
        self.visit(node, node.id_)
        self.append(' = ')
        self.visit(node,node.expr)


    def visit_If(self, parent, node):
        self.append('if ')
        self.append('(')
        self.visit(node, node.cond)
        self.append(')')
        self.append('{')
        self.newline()
        self.visit(node, node.true)
        self.append('}')
        if node.false is not None:
            self.append('else{')
            self.newline()
            self.visit(node, node.false)
            self.append('}')


    def visit_While(self, parent, node):
        self.append('while ')
        self.append('(')
        self.visit(node, node.cond)
        self.append(')')
        self.append('{')
        self.newline()
        self.visit(node, node.block)
        self.append('}')
        self.newline()



    def visit_For(self, parent, node):
        self.append('for (')
        self.visit(node,node.init)
        self.append(';')
        if (node.where.value == 'to'):
            value = node.init.id_.value
            self.append(value)
            self.append('<')
            self.visit(node, node.cond)
            self.append(';')
            self.append(value)
            self.append('++){')
            self.newline()
            self.visit(node, node.block)
        else:
            value = node.init.id_.value
            self.append(value)
            self.append('>')
            self.visit(node, node.cond)
            self.append(';')
            self.append(value)
            self.append('--){')
            self.newline()
            self.visit(node, node.block)

        self.append('}')

    def visit_RepeatUntil(self, parent, node):
        self.append('do')
        self.append('{')
        self.newline()
        self.visit(node, node.block)
        self.append('}')
        self.newline()
        self.append('while (')
        self.visit(node, node.cond)
        self.append(')')
        self.newline()

    def visit_FuncImpl(self, parent, node):
        self.visit(node, node.type_)
        self.append(' ')
        self.visit(node,node.id_)
        self.append('(')
        self.visit(node,node.params)
        self.append('){')
        self.newline()
        self.visit(node, node.var)
        self.visit(node, node.block)
        self.newline()
        self.append('}')

    def visit_ProcImpl(self, parent, node):
        self.append('void' + '')
        self.visit(node,node.id_)
        self.append('(')
        self.visit(node, node.params)
        self.append('){')
        self.newline()
        self.visit(node,node.var)
        self.visit(node,node.block)
        self.newline()
        self.append('}')

    def visit_FuncProcCall(self, parent, node):
        self.visit(node, node.id_)
        self.append('(')
        self.visit(node, node.args)
        self.append(')')

    def visit_Block(self, parent, node):

        for n in node.nodes:
            self.visit(node, n)
            if isinstance(n, If):
                pass
            elif isinstance(n, For):
                pass

            else:
                self.append(';')
            self.newline()


    def visit_Params(self, parent, node):
        for i, p in enumerate(node.params):
            if i > 0:
                self.append(', ')
            self.visit(node, p)

    def visit_Variables(self, parent, node):
        for n in node.vars:
            self.visit(node,n)
            self.append(';')
            self.newline()


    def visit_Args(self, parent, node):
        for i, a in enumerate(node.args):
            if i > 0:
                self.append(', ')
            self.visit(node, a)

    def visit_Elems(self, parent, node):
        for i, e in enumerate(node.elems):
            if i > 0:
                self.append(', ')
            self.visit(node, e)

    def visit_Break(self, parent, node):
        self.append('break')

    def visit_Continue(self, parent, node):
        self.append('continue')

    def visit_Exit(self, parent, node):
        self.append('return')
        if node.value is not None:
            self.append('(')
            self.visit(node,node.value)
            self.append(')')

    def visit_TypeString(self, parent, node):
        self.append('char[] ')

    def visit_Type(self, parent, node):
        if node.value == 'real' :
            self.append('double ')
        if node.value == 'integer':
            self.append('int ')
        if node.value == 'boolean':
            self.append('int ')
        if node.value == 'string':
            self.append('char[] ')
        if node.value == 'char':
            self.append('char ')


    def visit_Int(self, parent, node):
        self.append(node.value)

    def visit_Char(self, parent, node):
        self.append("'" + node.value+ "'" )

    def visit_String(self, parent, node):
        self.append(node.value)

    def visit_Real(self, parent, node):
        self.append(node.value)

    def visit_Boolean(self, parent, node):
        if node.value == 'true':
            self.append('1')
        else:
            self.append('0')

    def visit_Id(self, parent, node):
        self.append(node.value)

    def visit_BinOp(self, parent, node):
        self.append('(')
        self.visit(node, node.first)
        if node.symbol == 'mod':
            self.append(' % ')
        elif node.symbol == 'div':
            self.append(' / ')
        elif node.symbol == '/':
            self.append('/')
        elif node.symbol == 'and':
            self.append(' && ')
        elif node.symbol == 'or':
            self.append(' || ')
        elif node.symbol == '<>':
            self.append(' != ')
        else:
            self.append(node.symbol)
        self.visit(node, node.second)
        self.append(')')

    def visit_UnOp(self, parent, node):
        if node.symbol == '-':
            self.append('-')
        elif node.symbol != '&':
            self.append(node.symbol)
        self.visit(node, node.first)

    def visit_Where(self, parent, node):
        pass

    def visit_BoolValue(self, parent, node):
        if node.value == 'true':
            self.append('1')
        else:
            self.append('0')

    def visit_FormattedArg(self, parent, node):
        pass

    def generate(self, path):
        self.visit(None, self.ast)
        self.py = re.sub('\n\s*\n', '\n', self.py)
        with open(path, 'w') as source:
            source.write(self.py)
        return path



DEBUG = True  # OBAVEZNO: Postaviti na False pre slanja projekta

if DEBUG:

    test_id = '15'  # Redni broj test primera [01-15]
    path_root = 'Druga faza/'
    args = {}
    args['src'] = f'{path_root}{test_id}/src.pas'  # Izvorna PAS datoteka
    args['gen'] = f'{path_root}{test_id}/gen.c'  # Generisana C datoteka
else:
    import argparse

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('src')  # Izvorna PAS datoteka
    arg_parser.add_argument('gen')  # Generisana C datoteka
    args = vars(arg_parser.parse_args())

with open(args['src'], 'r') as source:
    text = source.read()
    lexer = Lexer(text)
    tokens = lexer.lex()
    # for t in tokens:
    # print(t)
    parser = Parser(tokens)
    ast = parser.parse()
    # symbolizer = Symbolizer(ast)
    # symbolizer.symbolize()
    print(ast)
    grapher = Grapher(ast)
    img = grapher.graph()
    Image(img)
    symbolizer = Symbolizer(ast)
    symbolizer.symbolize()
    print(ast)
    generator = Generator(ast)
    code = generator.generate('main1.py')

# generator = Generator(ast)
# generator.generate(args['gen'])
# runner = Runner(ast)
# runner.run()

# ACINONYX - END
