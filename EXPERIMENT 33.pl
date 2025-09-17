% --- Facts ---
parent(john, alice).
parent(john, bob).
parent(mary, alice).
parent(mary, bob).

% --- Rules ---
father(F, C) :- parent(F, C), F = john.
mother(M, C) :- parent(M, C), M = mary.

% --- Sample Queries ---
% ?- father(john, X).
% Output: X = alice ; X = bob.
