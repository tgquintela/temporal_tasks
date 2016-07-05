
#Convex optimization
2016-06-01

Convex optimization is the subfield of mathematical optimization which studies the specific problems in which the objective function is convex (minimization) or concave (maximization) and the constraint set is convex. The convexity property can make optimization in some sense "easier" than the general case since any local minimum must be a global minimum.

The convexity of the objective function makes the powerful tools of convex analysis applicable. In finite-dimensional normed spaces, _the Hahn–Banach theorem_ and the existence of subgradients lead to a particularly satisfying theory of necessary and sufficient conditions for optimality, a _duality theory_ generalizing that for linear programming, and effective computational methods.

The fields where they use convex optimization:
* Automatic control systems: get optimal moves between all the possibilities. There is the field of optimal control theory.
* Estimation and signal processing: reduce noise-signal ratio.
* Communications, transports and networks: less infrastructure with robust and stable functionality.
* Electronic circuit design: less infrastructure with robust and stable functionality.
* Data analysis and modeling: fit a model to a data using a measure of fitness.
* Statistics (optimal design): how to optimal design an experiment in order to reduce uncertainty and get most information.
* Finance: in problems as portfolio optimization.


### Formalization

The general formulation is:

$${\displaystyle f(x^{\ast })=\min\{f(x):x\in {\mathcal {X}}\},} f(x^\ast) = \min \{f(x):x \in \mathcal{X}\},$$

for some feasible set ${\displaystyle {\mathcal {X}}\subset \mathbb {R} ^{n}}$ and objective function f${\displaystyle f(x):\mathbb {R} ^{n}\rightarrow \mathbb {R}}$. The optimization problem is called a convex optimization problem if ${\displaystyle {\mathcal {X}}}$ is a convex set and ${\displaystyle f(x)}$ is a convex function defined on ${\displaystyle \mathbb {R} ^{n}}$.

Alternatively, an optimization problem of the form:

$${\displaystyle {\begin{aligned}&\operatorname {minimize} &&f(x)\\&\operatorname {subject\;to} &&g_{i}(x)\leq 0,\quad i=1,\dots ,m\end{aligned}}}$$

is called convex if the functions ${\displaystyle f,g_{1}\ldots g_{m}:\mathbb {R} ^{n}\rightarrow \mathbb {R} }$ are all convex functions.

Even that, it is usually written in the standard form. Standard form is the usual and most intuitive form of describing a convex minimization problem. It consists of the following three parts:
* A **convex function** ${\displaystyle f(x):\mathbb {R} ^{n}\to \mathbb {R} }$ to be minimized over the variable ${\displaystyle x}$
* **Inequality constraints** of the form ${\displaystyle g_{i}(x)\leq 0}$, where the functions ${\displaystyle g_{i}}$ are convex
* **Equality constraints** of the form ${\displaystyle h_{i}(x)=0}$, where the functions ${\displaystyle h_{i}}$ are affine. In practice, the terms "linear" and "affine" are often used interchangeably. Such constraints can be expressed in the form ${\displaystyle h_{i}(x)=a_{i}^{T}x+b_{i}}$, where ${\displaystyle a_{i}}$ is a column-vector and ${\displaystyle b_{i}}$ a real number.

Convex optimization problems has the special properties of:
* if a local minimum exists, then it is a global minimum.
* the set of all (global) minima is convex.
* for each strictly convex function, if the function has a minimum, then the minimum is unique.

These results are used by the theory of convex minimization along with geometric notions from functional analysis (in Hilbert spaces) such as the Hilbert projection theorem, the separating hyperplane theorem, and Farkas' lemma.

For ease the problem formulation sometimes is useful the *Lagrange multipliers* formulation.

### Methods
* "Bundle methods" (Wolfe, Lemaréchal, Kiwiel), and
* Subgradient projection methods (Polyak),
* Interior-point methods (Nemirovskii and Nesterov).
* Cutting-plane methods
* Ellipsoid method
* Subgradient method
* Dual subgradients and the drift-plus-penalty method


### Future TODO:
* Duality
* Karush-Kuhn-Tucker conditions
* Quasiconvex minimization

***Tags***: Computer science, Mathematics, Optimization, Economics, Operations Research

### See also
[Mathematical Optimization](/mathematical_optimization)
## Material
* http://cvxr.com/cvx/
* http://www.pyomo.org/

## Papers
* Ben-Tal, Aharon; Nemirovski, Arkadi (1998). Robust convex optimization. Mathematics of operations research, 23(4), 769-805.

## Books
* Boyd, Stephen; Vandenberghe, Lieven (2004). [Convex Optimization](https://www.goodreads.com/book/show/148030.Convex_Optimization). Cambridge University Press
* Bertsekas, Dimitri P. (2009). [Convex Optimization Theory](https://www.goodreads.com/book/show/6902482-convex-optimization-theory). Athena Scientific
* Bertsekas, Dimitri P. (2003). [Convex Analysis and Optimization](https://www.goodreads.com/book/show/148032.Convex_Analysis_and_Optimization). Athena Scientific
* Nesterov, Yurii (2013). [Introductory lectures on convex optimization: A basic course](https://www.goodreads.com/book/show/148031.Introductory_Lectures_on_Convex_Optimization). Vol. 87. Springer Science & Business Media.
* Hiriart-Urruty, Jean-Baptiste; Lemaréchal, Claude (1996). [Convex analysis and minimization algorithms: Fundamentals](https://www.goodreads.com/book/show/8362832-convex-analysis-and-minimization-algorithms-i)


