% diagnosis_example.pl
% Example disease knowledgebase and diagnosis helper predicates.

:- use_module(best_first_search).

% disease(Name, SymptomsList).
disease(flu,       [fever, cough, sore_throat, fatigue, headache]).
disease(common_cold, [cough, sore_throat, sneezing, runny_nose]).
disease(malaria,   [fever, chills, sweating, headache, nausea]).
disease(dengue,    [fever, headache, joint_pain, rash, bleeding]).
disease(typhoid,   [fever, weakness, stomach_pain, headache, diarrhea]).

/* -------------------------
   Simple diagnosis: rank diseases by symptom match
   ------------------------- */

% diagnose(+ObservedSymptoms, -Results)
% Results = [Name-ScorePercent, ...] ordered from best to worst match.
diagnose(Observed, ResultsSorted) :-
    findall(Name-Percent,
            ( disease(Name, Symptoms),
              intersection_size(Observed, Symptoms, Matches),
              length(Symptoms, Total),
              Percent is round(Matches * 100 / Total)
            ),
            Pairs),
    % sort by descending Percent
    sort_by_score_desc(Pairs, ResultsSorted).

intersection_size(A, B, N) :-
    intersection(A, B, I),
    length(I, N).

intersection([], _, []).
intersection([H|T], List, [H|Out]) :-
    memberchk(H, List), !,
    intersection(T, List, Out).
intersection([_|T], List, Out) :-
    intersection(T, List, Out).

sort_by_score_desc(Pairs, SortedDesc) :-
    % convert to pairs Score-Name to use keysort, then reverse
    map_list_to_pairs(snd_as_key, Pairs, PairsByKey),
    keysort(PairsByKey, SortedAsc),
    reverse(SortedAsc, Rev),
    pairs_values(Rev, SortedDesc).

% helper to convert Name-Score into Score-Name key
snd_as_key(Name-Score, Score-Name).

/* -------------------------
   Greedy Best-First usage example (adapting to generic code)
   We make a dummy start 'start' whose children are disease(Name).
   heuristic(disease(Name), H) computes H = 1/(1+Matches) so more matches => smaller H.
   ------------------------- */

% prepare observed symptoms for heuristic calculation
% we thread Observed via a dynamic predicate to keep heuristic/2 simple.
:- dynamic current_observed/1.

set_observed(Obs) :-
    retractall(current_observed(_)),
    asserta(current_observed(Obs)).

% arc(start, disease(Name)) - each disease is a child of start
arc(start, disease(Name)) :-
    disease(Name, _).

% no further expansion from disease nodes (they are leaves)
% (If you wanted to expand further, define arc(disease(Name), Next)...)

% heuristic(disease(Name), H)
% smaller H means better (we use H = 1/(1 + Matches))
heuristic(start, 9999).  % start has high heuristic so it's chosen first then expanded
heuristic(disease(Name), H) :-
    current_observed(Obs),
    disease(Name, Symptoms),
    intersection_size(Obs, Symptoms, Matches),
    H is 1 / (1 + Matches).   % more matches -> smaller H

% Goal test: when chosen node is a disease, we treat it as a candidate; here we can accept any disease
goal_is_disease(disease(_)).

% diagnose_best_first(+Observed, -BestCandidates)
% BestCandidates will be a list of disease(Name)-Matches pairs in order found by greedy expansion.
diagnose_best_first(Observed, Results) :-
    set_observed(Observed),
    % Run best_first starting from 'start' and gather expansion order.
    % The generic best_first returns one Path (first goal found). To see ranking,
    % we'll simulate by generating all disease nodes, computing their H, and sorting.
    findall(Name-Matches,
            ( disease(Name, Symptoms),
              intersection_size(Observed, Symptoms, Matches)
            ),
            Pairs),
    % sort by descending Matches
    sort_by_matches_desc(Pairs, Results).

sort_by_matches_desc(Pairs, Sorted) :-
    map_list_to_pairs(second_as_key_desc, Pairs, KPairs),
    keysort(KPairs, Asc),
    reverse(Asc, Rev),
    pairs_values(Rev, Sorted).

second_as_key_desc(Name-Matches, Matches-Name).
