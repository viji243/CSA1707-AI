% State: state(MonkeyPos, BoxPos, HasBanana)
% Monkey can move, push box, climb, grab banana

move(state(middle, middle, no), grab, state(middle, middle, yes)).

move(state(onfloor, Pos, H), walk(Pos, NewPos), state(onfloor, NewPos, H)).
move(state(onfloor, Pos, H), push(Pos, NewPos), state(onfloor, NewPos, H)) :- Pos = NewPos.
move(state(onfloor, Pos, H), climb, state(onbox, Pos, H)).

% Goal: reach state(_, _, yes)
solve(State) :-
    State = state(_, _, yes),
    write('Monkey has banana!'), !.

solve(State) :-
    move(State, Action, NewState),
    write('Action: '), writeln(Action),
    solve(NewState).

% Example:
% ?- solve(state(onfloor, left, no)).
