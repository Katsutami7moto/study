# coding=utf-8


# Пример

# def parse():
#     global regexp, current
#     terms = []
#     term = []
#     while current < len(regexp) and regexp[current] != ')':
#         if regexp[current] == '(':
#             current += 1
#             term.append(parse())
#         elif regexp[current] == '|':
#             terms.append(term)
#             term = []
#         elif regexp[current] == '*' or regexp[current] == '+':
#             term.append(createunode(regexp[current], term.pop()))
#         else:
#             term.append(createleaf(regexp[current]))
#         current += 1
#     terms.append(term)
#     return makeor(terms)


# Test-driven development


tokens = []
current = 0


class Token:
    def __init__(self, t, s=None, v=None):
        self.type = t
        self.subtype = s
        self.value = v


class Node:
    def __init__(self, t, v=None):
        self.type = t
        self.value = v

        self.lchild = None
        self.rchild = None

    def setl(self, obj):
        self.lchild = obj

    def setr(self, obj):
        self.rchild = obj


def create_bi_node(t, leftnode, rightnode):
    nd = Node(t)
    nd.setl(leftnode)
    nd.setr(rightnode)

    return nd


def make_sequence_tree(seq):
    """

    :type seq: list
    :rtype: Node
    """

    pass


def make_ident_node(idtok):
    """

    :type idtok: Token
    :rtype: Node
    """

    pass


def make_data_node(datok):
    """

    :type datok: Token
    :rtype: Node
    """

    pass


def make_inverse_node(somenode):
    """

    :type somenode: Node
    :rtype: Node
    """

    pass


def make_assign_node(term):
    """

    :type term: list
    :rtype: Node
    """

    pass


def make_print_node(term):
    """

    :type term: list
    :rtype: Node
    """

    pass


def parse_all_list():
    """

    :rtype: Node
    """

    global tokens, current
    assert isinstance(tokens, list)
    assert isinstance(current, int)

    if tokens:
        return parse_text()
    else:
        pass


def parse_text():
    """

    :rtype: Node
    """

    global tokens, current
    assert isinstance(tokens, list)
    assert isinstance(current, int)
    seq = []

    while current < len(tokens) and tokens[current].type != 'semicolon':
        seq.append(parse_instructions())
    return make_sequence_tree(seq)


def parse_instructions():
    """

    :rtype: Node
    """

    global tokens, current
    assert isinstance(tokens, list)
    assert isinstance(current, int)

    if tokens[current].type == 'let_op':
        return parse_let()
    elif tokens[current].type == 'print_op':
        return parse_print()
    else:
        pass


def parse_let():
    """

    :rtype: Node
    """

    global tokens, current
    assert isinstance(tokens, list)
    assert isinstance(current, int)

    term = []
    current += 1

    if tokens[current].type == 'ident':
        term.append(make_ident_node(tokens[current]))
        current += 1
        if tokens[current].type == 'equal_sign':
            current += 1
            term.append(parse_param())
            return make_assign_node(term)
        else:
            pass
    else:
        pass


def parse_print():
    """

    :rtype: Node
    """

    global tokens, current
    assert isinstance(tokens, list)
    assert isinstance(current, int)

    term = []
    current += 1

    if tokens[current].type == 'colon':
        current += 1
        term.append(parse_param())
        return make_print_node(term)
    else:
        pass


def parse_param():
    """

    :rtype: Node
    """

    global tokens, current
    assert isinstance(tokens, list)
    assert isinstance(current, int)

    term = []

    while tokens[current].type != 'semicolon':
        if tokens[current].type == 'ident' or tokens[current].type == 'int' or tokens[current].type == 'float' or \
                        tokens[current].type == 'string' or tokens[current].type == 'bool' or tokens[
            current].type == 'math_op' or tokens[current].type == 'log_op' or tokens[current].type == 'lparen' or \
                        tokens[current].type == 'rparen':

            term.append(tokens[current])
            current += 1
        else:
            pass
    current += 1
    return parse_expr(term, 0)


# orexpr    :   andexpr (OR andexpr)*;
#
# andexpr   :   bool (AND bool)*;
#
# bool      :   TRUE | FALSE | boolatom | NOT boolatom;
#
# boolatom  :   ID | LPAREN boolexpr RPAREN;
#
# boolexpr  :   orexpr | typexpr | compare;
#
# typexpr   :   ID QM ID;
#
# compare   :   mathexpr (MORE | LESS | MOREQ | LESEQ | EQ | NEQ) mathexpr;
#
# mathexpr  :	multexpr ((PLUS | MINUS) multexpr)* | MINUS mathexpr;
#
# multexpr  :	mathatom ((MULT | DIV | MOD) mathatom)*;
#
# mathatom  :	INT | FLOAT | ID | LPAREN mathexpr RPAREN;

# Везде, где есть ID (кроме правого операнда typexpr), потом добавятся:
# CALL, METHOD, FIELD, LPAREN LAMBDARET RPAREN, KCALL;

# !	        логическое НЕ	            унарный	    15	справа налево
# * / %	    мультипликативные операции	бинарный	13	слева направо
# + -	    аддитивные операции	        бинарный	12	слева направо
# < > <= >=	отношения	                бинарный	10	слева направо
# = !=	    равенство/неравенство	    бинарный	9	слева направо
# &&	    логическое И	            бинарный	5	слева направо
# ||	    логическое ИЛИ	            бинарный	4	слева направо


def parse_mathexpr(term, curr):
    """

    :type term: list
    :type curr: int
    :rtype: Node
    """

    pass


def parse_bool(term):
    """

    :type term: list
    :rtype: Node
    """

    if len(term) == 1:
        if term[0].type == 'bool':
            return make_data_node(term[0])
        elif term[0].type == 'ident':
            return make_ident_node(term[0])
        else:
            pass
    elif len(term) == 2:
        if term[0].subtype == 'not' and term[1].type == 'ident':
            return make_inverse_node(make_ident_node(term[1]))
        else:
            pass
    else:
        if term[0].subtype == 'not':
            if term[1].type == 'lparen' and term[-1].type == 'rparen':
                return make_inverse_node(parse_boolexpr(term, 1))
            else:
                pass
        elif term[0].type == 'lparen' and term[-1].type == 'rparen':
            return parse_boolexpr(term, 0)


def make_and_node(terms):
    """

    :type terms: list
    :rtype: Node
    """

    result = parse_bool(terms[0])
    for one in range(1, len(terms)):
        result = create_bi_node('and_op', result, parse_bool(terms[one]))
    return result


def parse_and(term):
    """

    :rtype: Node
    :type term: list
    """

    ts = []
    t = []
    curr = 0

    while curr < len(term) and term[curr].type != 'rparen':
        if term[curr].type == 'lparen':
            curr += 1
            t.append(parse_boolexpr(term, curr))
        elif term[curr].subtype == 'and':
            ts.append(t)
            t = []
        else:
            t.append(term[curr])
        curr += 1
    ts.append(t)

    return make_and_node(ts)


def make_or_node(terms):
    """

    :type terms: list
    :rtype: Node
    """

    result = parse_and(terms[0])
    for one in range(1, len(terms)):
        result = create_bi_node('or_op', result, parse_and(terms[one]))
    return result


def parse_or(term, curr):
    """

    :type term: list
    :type curr: int
    :rtype: Node
    """

    ts = []
    t = []

    while curr < len(term) and term[curr].type != 'rparen':
        if term[curr].type == 'lparen':
            curr += 1
            t.append(parse_boolexpr(term, curr))
        elif term[curr].subtype == 'or':
            ts.append(t)
            t = []
        else:
            t.append(term[curr])
        curr += 1
    ts.append(t)
    return make_or_node(ts)


def parse_type(term, curr):
    pass


def parse_compare(term, curr):
    pass


def parse_boolexpr(term, curr):
    """

    :type term: list
    :type curr: int
    :rtype: Node
    """

    o = False
    t = False
    r = False

    while curr < len(term) and term[curr].type != 'rparen':
        if term[curr].type == 'lparen':
            curr += 1
            parse_boolexpr(term, curr)
        elif term[curr].subtype == 'or':
            o = True
            break
        elif term[curr].subtype == 'qm':
            t = True
            break
        elif term[curr].subtype == 'compare':
            r = True
            break
        else:
            pass
    if o:
        return parse_or(term, 0)
    elif t:
        return parse_type(term, 0)
    elif r:
        return parse_compare(term, 0)
    else:
        return parse_bool(term)


def parse_no_ops(term, curr):
    """

    :type term: list
    :type curr: int
    :rtype: Node
    """

    if len(term) == 1:
        if term[curr].type == 'ident':
            return make_ident_node(term[curr])
        elif term[curr].type == 'int' or term[curr].type == 'float' or term[curr].type == 'string' or \
                term[curr].type == 'bool':
            return make_data_node(term[curr])
        else:
            pass
    else:
        pass


def parse_expr(term, curr):
    """

    :type term: list
    :type curr: int
    :rtype: Node
    """

    m = False
    l = False

    while curr < len(term) and term[curr].type != 'rparen':
        if term[curr].type == 'lparen':
            curr += 1
            parse_expr(term, curr)
        elif term[curr].type == 'math_op' and not m:
            m = True
        elif term[curr].type == 'log_op':
            l = True
            break
        else:
            pass
        curr += 1
    if l:
        return parse_boolexpr(term, 0)
    elif m and not l:
        return parse_mathexpr(term, 0)
    elif not m and not l:
        return parse_no_ops(term, 0)
