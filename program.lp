pos(1..1000).
n(A,B) :- pos(A), pos(B), A+1 == B.

{ on(A) : pos(A) }.

valid(A) :- pos(A), A \ 5 = 0.

:- on(A), on(B), n(A,B).
:- on(A), not valid(A).



#maximize { 1@1, A : on(A) }.
#show on/1.
