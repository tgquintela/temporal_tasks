
#Integer programming
2016-06-01

An integer programming problem is a mathematical optimization or feasibility program in which some or all of the variables are restricted to be integers. In many settings the term refers to integer linear programming (ILP), in which the objective function and the constraints (other than the integer constraints) are linear.

Integer programming is NP-hard. A special case, 0-1 integer linear programming, in which unknowns are binary, and only the restrictions must be satisfied, is one of Karp's 21 NP-complete problems.

The formalization of this problem is:

$${\displaystyle {\begin{aligned}&{\text{maximize}}&&\mathbf {c} ^{\mathrm {T} }\mathbf {x} \\&{\text{subject to}}&&A\mathbf {x} \leq \mathbf {b} ,\\&&&\mathbf {x} \geq \mathbf {0} ,\\&{\text{and}}&&\mathbf {x} \in \mathbb {Z} ^{n},\end{aligned}}}$$

where the entries of ${\displaystyle \mathbf {c} ,\mathbf {b} }$ are vectors and A {\displaystyle A} is a matrix, having integer values. Note that similar to linear programs, ILPs not in standard form can be converted to standard form by eliminating inequalities by introducing slack variables ( s {\displaystyle \mathbf {s} } ) and replacing variables that are not sign-constrained with the difference of two sign-constrained variables.


### Common methods
The most common methods used to solve an integer programming problem are:
* Using total unimodularity.
* Exact algorithms: as the cutting plane methods.
* Heuristic methods: as tabu search, hill climbing, simulated annealing, reactive search optimization, ant colony optimization, hopfield neural networks.

***Tags***: Computer science, Mathematics, Optimization, Economics, Operations Research

#### See also
[Mathematical Optimization](/mathematical_optimization)
## Papers
* Nemhauser, George L., and Laurence A. Wolsey. [Integer programming and combinatorial optimization](https://www.researchgate.net/profile/George_Nemhauser/publication/230596114_The_Scope_of_Integer_and_Combinatorial_Optimization/links/53d6964a0cf2f57be98eb884.pdf). Wiley, Chichester. GL Nemhauser, MWP Savelsbergh, GS Sigismondi (1992). Constraint Classification for Mixed Integer Programming Formulations. COAL Bulletin 20 (1988): 8-12.
* Glover, Fred. [Future paths for integer programming and links to artificial intelligence](http://s3.amazonaws.com/academia.edu.documents/45553153/Future-paths-for-integer-programming-and-links-to-artificial-intelligence_1986_Computers-and-Operations-Research.pdf?AWSAccessKeyId=AKIAJ56TQJRTWSMTNPEA&Expires=1466343826&Signature=RPYmJ%2FqOs4srrd8AoBywF5qsRuw%3D&response-content-disposition=inline%3B%20filename%3DFUTURE_PATHS_FOR_INTEGER_PROGRAMMING_AND.pdf). Computers & operations research 13.5 (1986): 533-549.

## Books
* Taha, Hamdy A. (1975). [Integer Programming: Theory, Applications, and Computations](https://www.goodreads.com/book/show/1301179.Integer_Programming). Academic Press
* Wolsey, Laurence A. (1998). [Integer Programming](https://www.goodreads.com/book/show/2438135.Integer_Programming). Wiley-Interscience
* Schrijver, Alexander (1998). [Theory of Linear and Integer Programming](https://www.goodreads.com/book/show/3400135-theory-of-linear-and-integer-programming). John Wiley & Sons.
* Garfinkel, Robert S.; Nemhauser, George L. (1972). [Integer programming](https://www.goodreads.com/book/show/6832254-integer-programming). Vol. 4. New York: Wiley, 1972.


