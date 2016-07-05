
#Linear programming
2016-06-01

Linear programming (LP; also called linear optimization) is a type of optimization problem in which requirements are represented by linear relationships. Linear programming is a special case of mathematical programming (mathematical optimization).

More formally, linear programming is a technique for the optimization of a linear objective function, subject to linear equality and linear inequality constraints. Its feasible region is a convex polytope, which is a set defined as the intersection of finitely many half spaces, each of which is defined by a linear inequality. Its objective function is a real-valued affine (linear) function defined on this polyhedron. A linear programming algorithm finds a point in the polyhedron where this function has the smallest (or largest) value if such a point exists.

Linear programs are problems that can be expressed in *canonical form* as:

$${\displaystyle {\begin{aligned}&{\text{maximize}}&&\mathbf {c} ^{\mathrm {T} }\mathbf {x} \\&{\text{subject to}}&&A\mathbf {x} \leq \mathbf {b} \\&{\text{and}}&&\mathbf {x} \geq \mathbf {0} \end{aligned}}}$$

where x represents the vector of variables (to be determined), c and b are vectors of (known) coefficients, A is a (known) matrix of coefficients, and ${\displaystyle (\cdot )^{\mathrm {T} }}$ is the matrix transpose. The expression to be maximized or minimized is called the objective function (cTx in this case). The inequalities Ax ≤ b and x ≥ 0 are the constraints which specify a convex polytope over which the objective function is to be optimized. In this context, two vectors are comparable when they have the same dimensions. If every entry in the first is less-than or equal-to the corresponding entry in the second then we can say the first vector is less-than or equal-to the second vector.

Linear programming can be applied to various fields of study. It is widely used in business and economics, and is also utilized for some engineering problems. Industries that use linear programming models include transportation, energy, telecommunications, and manufacturing. It has proved useful in modeling diverse types of problems in planning, routing, scheduling, assignment, and design.


For each problem there is an associate dual problem. Sometimes it is easier to solve the dual problem.

### Main methods
The main methods for solving linear programming are:
* Simplex algorithm of Dantzig: a basis-exchange algorighm.
* Criss-cross algorithm: a basis-exchange algorighm.
* Ellipsoid algorithm, following Khachiyan: interior point algorithm.
* Projective algorithm of Karmarkar: interior point algorithm.
* Affine scaling: interior point algorithm.
* ...

***Tags***: Computer science, Mathematics, Optimization, Economics, Operations Research

### See also
[Mathematical Optimization](/mathematical_optimization)
## Papers
* Bland, Robert G. (1977). "New Finite Pivoting Rules for the Simplex Method". Mathematics of Operations Research 2 (2): 103–107

## Books
* George B. Dantzig and Mukund N. Thapa. 1997. [Linear programming 1: Introduction](https://www.goodreads.com/book/show/1595942.Linear_Programming_1). Springer-Verlag.
* George B. Dantzig and Mukund N. Thapa. 2003. [Linear Programming 2: Theory and Extensions](https://www.goodreads.com/book/show/545097.Linear_Programming_2). Springer-Verlag.
* Alexander Schrijver, (1998). [Theory of Linear and Integer Programming](https://www.goodreads.com/book/show/3400135-theory-of-linear-and-integer-programming). John Wiley & Sons.
* Bazaraa, Mokhtar S.; Jarvis, John J.; Sherali, Hanif D. (2004). [Linear Programming and Network Flows](https://www.goodreads.com/book/show/153419.Linear_Programming_and_Network_Flows). Wiley-Interscience


