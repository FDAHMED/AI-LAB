% a. Simple Facts and Querying
% In Prolog, a fact ends with a period (.). Predicates and atoms must start with a lowercase letter.

% Facts
likes(mary, pizza).
likes(john, sushi).
likes(mary, sushi).
hungry(john).
hungry(sara).

% A simple Rule: Someone is happy if they like sushi and are hungry.
happy(Person) :- 
    likes(Person, sushi), 
    hungry(Person).
