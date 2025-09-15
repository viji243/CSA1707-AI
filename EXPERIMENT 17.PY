% sum_to_n(N, Sum) : Sum is 1+2+...+N
sum_to_n(0, 0).
sum_to_n(N, Sum) :-
    N > 0,
    N1 is N - 1,
    sum_to_n(N1, Prev),
    Sum is Prev + N.

% Example Query:
% ?- sum_to_n(5, S).
% S = 15.
