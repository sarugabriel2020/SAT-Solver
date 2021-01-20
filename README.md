# SAT-Solver --- THE MATRIX REPRESENTATION OF THE CNF FORMULA

--- Project objectives ---

-->The objectives are to implement in Python an algorithm for solving the SAT problem, determining the execution times for them and creating a simple graph to illustrate the complexity of the algorithm.

The algorithm uses the matrix form to represent a formula.
In the matrix, the rows correspond to the clauses in the formula, and the columns to the variables.
Each variable can be:
  (i)   not appear in a clause,
  (ii)  appear without denial,
  (iii) appear negative.
  
To find an interpretation, the algorithm will have a "backtracking" approach over all possible interpretations.
------------------------------------------------------------
          ------ IMPORTANCE -----------

  •• SAT was the first problem discovered to be NP-complete, thanks to the theorem Cook-Levin.
  
  •• As a result, it has been studied for a long time, with many being discovered heuristic algorithms that can find (most of the time) valid configurations in time polynomial, despite the fact that it is not yet known whether or not there is an exact algorithm
to solve SAT in polynomial time. 

  •• These solvers are very useful in the case of many other problems for which, in the same way, that no effective solutions have been formulated - by usually also NP-complete problems - because we can reduce them polynomially to SAT.

------------------------------------------------------------

In this project, we started in code by defining the function:

- def solve (fnc) -> which receives as a parameter the formula in natural conjunctive form, and in this function we first create a list of literals.

• Then we search iteratively through the formula in the natural conjunctive form if there is a literal negated m and if there is, we will replace it with '', and at the same time we separate by the character V.

• Then we iterate again with the variable j in the clause, adding the clause to the list of literals, and if there is a duplicate, we delete them using set (literals).

• We create the matrix as a list in which we add another list and initialize it all with 0 and iterate again through the formula from fnc and when we meet in V, we separate the formula, and if we find in the matrix the element ~, we replace it with '' and we put -1 in the clause, and if we do not find in the formula from fnc any negative element ~, we put 1.

• Then we go through the indexes of the iteration list and consider the interpretation True.

• We go through iteratively with variables in the matrix, if we consider that clause is false.

• If in the matrix we find on positions i, j the element 1 and in the list of iterations the same or in the matrix we find -1 and in the list of iterations 0, then we found an element true in a clause, it results that all our clause will be True .

• If a clause in an expression is false, then the whole interpretation is False and we stop.

• If the interpreter is True, we display 1.

• If the interpreter is False, we display 0.

-def interare (nr_element, literals) -> which receives as parameter the number of elements, and literals, and this function performs the exhaustive search over all interpretations.

-def sat_solver_algorithm ():

  • In this function we read the respective formula in the input
  
  • Put in fnc the read input in which we replace the parentheses with '' and divide after the input.
  
  • Call the solve function (fnc)
