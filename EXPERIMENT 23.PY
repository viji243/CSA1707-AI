% bird(Name, CanFly)
bird(sparrow, yes).
bird(parrot, yes).
bird(penguin, no).
bird(ostrich, no).

can_fly(Bird) :- bird(Bird, yes).
cannot_fly(Bird) :- bird(Bird, no).

% Example:
% ?- can_fly(parrot).
% true.
% ?- cannot_fly(penguin).
% true.
