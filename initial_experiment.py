import clingo
from clingo.symbol import Number
from clingo.control import Control

def on_model(m):
    print(m)

program1 = r"""
parent(ol, ja).
parent(ol, sv).
parent(ge, ol).
parent(ge, ga).
sibling(A,B) :- parent(C,A), parent(C,B), A != B.
father(A) :- parent(A,B).
"""

program2 = r"""
pos(a;b;c;d;e;f).
n(a,b).
n(b,c).
n(c,d).
n(d,e).
n(e,f).

{ on(A) : pos(A) }.

:- on(A), on(B), n(A,B).

#maximize { 1@1, A : on(A) }.
"""

ctl = Control()
ctl.configuration.solve.models = 0
ctl.add("base", [], program1)
ctl.ground([("base", [])])
ctl.solve(on_model=on_model)
