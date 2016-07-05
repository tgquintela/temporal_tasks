
#Linear-fractional programming
2016-06-01

Linear-fractional programming (LFP) is a generalization of linear programming (LP). Whereas the objective function in a linear program is a linear function, the objective function in a linear-fractional program is a ratio of two linear functions. A linear program can be regarded as a special case of a linear-fractional program in which the denominator is the constant function one.

Formally, a linear-fractional program is defined as the problem of maximizing (or minimizing) a ratio of affine functions over a polyhedron,

$${\displaystyle {\begin{aligned}{\text{maximize}}\quad &{\frac {\mathbf {c} ^{T}\mathbf {x} +\alpha }{\mathbf {d} ^{T}\mathbf {x} +\beta }}\\{\text{subject to}}\quad &A\mathbf {x} \leq \mathbf {b} ,\end{aligned}}}$$

where ${\displaystyle \mathbf {x} \in \mathbb {R} ^{n}}$ represents the vector of variables to be determined, ${\displaystyle \mathbf {c} ,\mathbf {d} \in \mathbb {R} ^{n}}$ and ${\displaystyle \mathbf {b} \in \mathbb {R} ^{m}}$ are vectors of (known) coefficients, ${\displaystyle A\in \mathbb {R} ^{m\times n}}$ is a (known) matrix of coefficients and ${\displaystyle \alpha ,\beta \in \mathbb {R} }$ are constants. The constraints have to restrict the feasible region to ${\displaystyle \{\mathbf {x} |\mathbf {d} ^{T}\mathbf {x} +\beta >0\}}$ , i.e. the region on which the denominator is positive. Alternatively, the denominator of the objective function has to be strictly negative in the entire feasible region.

There is the possiblity to transform a linear-fractional optimization problem to a linear optimization problem.

***Tags***: Computer science, Mathematics, Optimization, Economics, Operations Research

### See also
[Mathematical Optimization](/mathematical_optimization), [Linear programming](/linear_programming)

