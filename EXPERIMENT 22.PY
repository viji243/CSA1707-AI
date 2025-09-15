% hanoi(N, From, To, Aux)
hanoi(1, From, To, _) :-
    format('Move disk from ~w to ~w~n', [From, To]).
hanoi(N, From, To, Aux) :-
    N > 1,
    M is N - 1,
    hanoi(M, From, Aux, To),
    hanoi(1, From, To, Aux),
    hanoi(M, Aux, To, From).

% Example:
% ?- hanoi(3, left, right, middle).
