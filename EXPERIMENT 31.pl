% --- Facts: Define vowels ---
vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).

% --- Rule: Count vowels in a list ---
count_vowels([], 0).
count_vowels([H|T], Count) :-
    vowel(H),                     % If head is a vowel
    count_vowels(T, RestCount),
    Count is RestCount + 1.

count_vowels([H|T], Count) :-
    \+ vowel(H),                  % If head is NOT a vowel
    count_vowels(T, Count).

% --- Sample Queries ---
% ?- count_vowels([h,e,l,l,o], N).
% Output: N = 2.
%
% ?- count_vowels([p,r,o,l,o,g], N).
% Output: N = 2.
