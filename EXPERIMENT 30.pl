% --- Facts ---
word(apple).
word(orange).
word(grape).

% --- Rule: Check if a word exists ---
match_word(Word) :-
    word(Word).

% --- Sample Queries ---
% ?- match_word(apple).
% Output: true.
% ?- match_word(banana).
% Output: false.
