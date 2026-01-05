% B. Family Tree Program
% This is the classic way to demonstrate how Prolog handles complex relationships using recursion and logical conjunctions.

%The Knowledge Base

% --- Facts: Gender ---
male(jack).
male(bill).
male(john).
female(alice).
female(sue).

% --- Facts: Parent Relationship (parent(Parent, Child)) ---
parent(jack, bill).
parent(jack, sue).
parent(alice, bill).
parent(alice, sue).
parent(bill, john).

% --- Rules ---

% A child is someone who has a parent
child(X, Y) :- parent(Y, X).

% A father is a male parent
father(X, Y) :- parent(X, Y), male(X).

% A mother is a female parent
mother(X, Y) :- parent(X, Y), female(X).

% Siblings share the same parents and are not the same person
sibling(X, Y) :- 
    parent(P, X), 
    parent(P, Y), 
    X \= Y.

% Grandparent relationship
grandparent(X, Z) :- 
    parent(X, Y), 
    parent(Y, Z).
