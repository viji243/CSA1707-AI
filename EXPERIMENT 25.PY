% best_first_search.pl
% Generic greedy Best-First Search.
% Needs domain predicates:
%   arc(State, Child)         : Child is successor of State.
%   heuristic(State, H)       : H is heuristic value (smaller = better).

:- module(best_first_search, [best_first/3]).

% best_first(+Start, +GoalTest, -Path)
% GoalTest is a predicate of arity 1: GoalTest(State) succeeds if State is a goal.
best_first(Start, GoalTest, Path) :-
    heuristic(Start, H0),
    best_first_loop([node(Start, H0, [Start])], GoalTest, Path).

% best_first_loop(+OpenList, +GoalTest, -Path)
% OpenList: list of node(State, H, PathSoFar)
best_first_loop([node(State, _H, PathSoFar) | _Rest], GoalTest, PathSoFar) :-
    call(GoalTest, State), !.           % success if chosen node meets goal
best_first_loop([node(State,_H,PathSoFar) | RestOpen], GoalTest, SolutionPath) :-
    findall(node(Child, Hchild, [Child | PathSoFar]),
            ( arc(State, Child),
              heuristic(Child, Hchild)
            ),
            ChildrenNodes),
    append(RestOpen, ChildrenNodes, NewOpen),
    sort_open_by_h(NewOpen, SortedOpen),
    best_first_loop(SortedOpen, GoalTest, SolutionPath).

% If open becomes empty, fail.
best_first_loop([], _GoalTest, _Path) :- fail.

% Sort open list ascending by H (smaller H = higher priority)
sort_open_by_h(Open, Sorted) :-
    map_list_to_pairs(node_h_key, Open, Pairs),
    keysort(Pairs, SortedPairs),
    pairs_values(SortedPairs, Sorted).

node_h_key(node(_State, H, _Path), H).
