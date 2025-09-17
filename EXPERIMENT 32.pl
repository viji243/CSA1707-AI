% --- Facts: Possible outcomes ---
dice(1). dice(2). dice(3). dice(4). dice(5). dice(6).

% --- Rule: Roll a dice ---
roll(D) :- dice(D).

% --- Sample Queries ---
% ?- roll(D).
% Output: D = 1 ; D = 2 ; D = 3 ; D = 4 ; D = 5 ; D = 6.
