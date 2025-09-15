% --- Facts ---
employee(alice).
employee(bob).
employee(charlie).

department(alice, sales).
department(bob, hr).
department(charlie, sales).

years_of_service(alice, 6).
years_of_service(bob, 3).
years_of_service(charlie, 7).

% --- Rules for Forward Chaining ---
:- dynamic eligible_for_promotion/1.

check_promotion :-
    employee(E),
    years_of_service(E, Y),
    Y >= 5,
    \+ eligible_for_promotion(E),   % prevent duplicates
    assertz(eligible_for_promotion(E)),
    fail.  % force backtracking to check all employees
check_promotion.  % succeed after all checks

% --- Query to Run Forward Chaining ---
% ?- check_promotion.
% ?- eligible_for_promotion(X).
