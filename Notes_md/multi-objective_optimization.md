
#Multi-objective optimization
2016-06-01

Multi-objective optimization (also known as multi-objective programming, vector optimization, multicriteria optimization, multiattribute optimization or Pareto optimization) is an area of multiple criteria decision making, that is concerned with mathematical optimization problems involving more than one objective function to be optimized simultaneously. Multi-objective optimization consist on balance the tradeoffs properly using a decided criteria.

For a nontrivial multi-objective optimization problem, there does not exist a single solution that simultaneously optimizes each objective. In that case, the objective functions are said to be conflicting, and there exists a (possibly infinite) number of Pareto optimal solutions. A solution is called nondominated, Pareto optimal, Pareto efficient or noninferior, if none of the objective functions can be improved in value without degrading some of the other objective values. Without additional subjective preference information, all Pareto optimal solutions are considered equally good (as vectors cannot be ordered completely). Researchers study multi-objective optimization problems from different viewpoints and, thus, there exist different solution philosophies and goals when setting and solving them. The goal may be to find a representative set of Pareto optimal solutions, and/or quantify the trade-offs in satisfying the different objectives, and/or finding a single solution that satisfies the subjective preferences of a human decision maker (DM).

### Examples
There are different real-world examples:
* **Macroeconomic policy-making**: A central bank must choose a stance for monetary policy that balances competing objectives (low inflation, low unemployment, low balance of trade deficit, etc...) To do this, the central bank uses a model of the economy that quantitatively describes the various causal linkages in the economy; it simulates the model repeatedly under various possible stances of monetary policy, in order to obtain a menu of possible predicted outcomes for the various variables of interest. Then in principle it can use an aggregate objective function to rate the alternative sets of predicted outcomes, although in practice central banks use a non-quantitative, judgement-based, process for ranking the alternatives and making the policy choice.
* **Finance**: choose a portfolio when there are two conflicting objectives (high outcome value, low risk value).
* **Optimal control**: balance trade-off between different variables which arises in control problems.
* **Electric systems**, **transportations systems** and other real-world problems: balance costs and services.
* ...

### Methods
There are different methods to solve multi-objective optimization problems:
* Scalarizing multi-objective optimization problems: (as in portfolio optimization with mean-variance analysis).
* No-preference methods: 
* A priori methods: based on a definition of an utility function.
* A posteriori methods: they aim at producing all the Pareto optimal solutions or a representative subset of the Pareto optimal solutions. Most a posteriori methods fall into either one of the following two classes: mathematical programming -based a posteriori methods, where an algorithm is repeated and each run of the algorithm produces one Pareto optimal solution, and evolutionary algorithms where one run of the algorithm produces a set of Pareto optimal solutions.
* Interactive methods: the solution process is iterative and the decision maker continuously interacts with the method when searching for the most preferred solution.
* Hybrid methods: most important are hybridizing MCDM (multi-criteria decision making) and EMO (evolutionary multi-objective optimization)

In engineering and economics, many problems involve multiple objectives which are not describable as the-more-the-better or the-less-the-better; instead, there is an ideal target value for each objective, and the desire is to get as close as possible to the desired value of each objective. For example, energy systems typically have a trade-off between performance and cost[3][4] or one might want to adjust a rocket's fuel usage and orientation so that it arrives both at a specified place and at a specified time; or one might want to conduct open market operations so that both the inflation rate and the unemployment rate are as close as possible to their desired values.

Often such problems are subject to linear equality constraints that prevent all objectives from being simultaneously perfectly met, especially when the number of controllable variables is less than the number of objectives and when the presence of random shocks generates uncertainty. Commonly a multi-objective quadratic objective function is used, with the cost associated with an objective rising quadratically with the distance of the objective from its ideal value. Since these problems typically involve adjusting the controlled variables at various points in time and/or evaluating the objectives at various points in time, intertemporal optimization techniques are employed


Multi-objective optimization has been applied in many fields of science, including engineering, economics and logistics (see the section on applications for detailed examples) where optimal decisions need to be taken in the presence of trade-offs between two or more conflicting objectives. Minimizing cost while maximizing comfort while buying a car, and maximizing performance whilst minimizing fuel consumption and emission of pollutants of a vehicle are examples of multi-objective optimization problems involving two and three objectives, respectively. In practical problems, there can be more than three objectives.

***Tags***: Computer science, Mathematics, Optimization, Economics, Operations Research

## See also
## See also:
[Mathematical Optimization](/mathematical_optimization), [Evolutionary algorithms](/evolutionary_algorithms), [Pareto efficiency](/pareto_efficiency)
## Material
* http://demonstrations.wolfram.com/EvolutionaryMultiobjectiveOptimization/
* http://www.openeering.com/sites/default/files/Multiobjective_Optimization_NSGAII_0.pdf
* http://esa.github.io/pygmo/
* https://github.com/esa/pagmo
* http://deap.readthedocs.io/en/master/

## Papers
* Ruzika, S.; Wiecek, M. M. (2005). "Approximation Methods in Multiobjective Programming". Journal of Optimization Theory and Applications 126 (3): 473-501.
* Meisel, W. L. (1973), J. L. Cochrane; M. Zeleny, eds., "Tradeoff decision in multiple criteria decision making", Multiple Criteria Decision Making (S.C. University of Columbia): 461-476
* Ozlen, Melih; Burton, Benjamin A.; MacRae, Cameron A.G. (2014). "Multi-Objective Integer Programming: An Improved Recursive Algorithm". Journal of Optimization Theory and Applications 160 (2): 470-482.

## Books
* Miettinen, Kaisa (1999). Nonlinear Multiobjective Optimization. Springer.
* Van Veldhuizen, David A. (2007). [Evolutionary Algorithms for Solving Multi-Objective Problems](https://www.goodreads.com/book/show/706562.Evolutionary_Algorithms_for_Solving_Multi_Objective_Problems). Springer
* Deb, Kalyanmoy (2001). [Multi-Objective Optimization Using Evolutionary Algorithms](https://www.goodreads.com/book/show/3337028-multi-objective-optimization-using-evolutionary-algorithms). Wiley


