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

% --- Rule for Backward Chaining ---
eligible_for_promotion(E) :-
    employee(E),
    years_of_service(E, Y),
    Y >= 5.

% --- Query to Run Backward Chaining ---
% ?- eligible_for_promotion(alice).
% ?- eligible_for_promotion(X).
