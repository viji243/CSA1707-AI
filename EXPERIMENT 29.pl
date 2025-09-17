% --- Facts ---
visited(john, homepage).
visited(john, about).
visited(mary, homepage).
visited(alex, contact).

% --- Rule: Find all pages visited by a user ---
pages_visited(User, Page) :-
    visited(User, Page).

% --- Sample Queries ---
% ?- pages_visited(john, Page).
% Output: Page = homepage ; Page = about.
