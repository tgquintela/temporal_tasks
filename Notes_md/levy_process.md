
#Levy process
2016-06-01

Lévy process, named after the French mathematician Paul Lévy, is a càdlàg stochastic process with independent, stationary increments: it represents the motion of a point whose successive displacements are random and independent, and statistically identical over different time intervals of the same length. A Lévy process may thus be viewed as the continuous-time analog of a random walk.

The most well known examples of Lévy processes are Brownian motion and the Poisson process. Aside from Brownian motion with drift, all other proper Lévy processes have discontinuous paths.

### Formalization

A stochastic process $X_t$ is said to be a Lévy process if it satisfies the following properties:
* ${\displaystyle X_{0}=0\}$, almost surely
* Independence of increments: For any ${\displaystyle 0\leq t_{1}<t_{2}<\cdots <t_{n}<\infty }$, ${\displaystyle X_{t_{2}}-X_{t_{1}},X_{t_{3}}-X_{t_{2}},\dots ,X_{t_{n}}-X_{t_{n-1}}}$ are independent
* Stationary increments: For any ${\displaystyle s<t\}$, ${\displaystyle X_{t}-X_{s}\}$, is equal in distribution to ${\displaystyle X_{t-s}}.
* Continuity in probability: For any ${\displaystyle \epsilon >0} and ${\displaystyle t\geq 0}$ it holds that ${\displaystyle \lim _{h\rightarrow 0}P(|X_{t+h}-X_{t}|>\epsilon )=0}$

If ${\displaystyle X}$ is a Lévy process then one may construct a version of ${\displaystyle X}$ such that ${\displaystyle t\mapsto X_{t}}$ is almost surely right continuous with left limits.

***Tags***: Stochastic processes

## See also
## See also:
[Wiener process](/wiener_process)
## Papers
* Eberlein, E. (2001). [Application of generalized hyperbolic Lévy motions to finance](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.469.5237&rep=rep1&type=pdf). In Lévy processes (pp. 319-336). Birkhäuser Boston.
* Rosiński, J. (2001). [Series representations of Lévy processes from the perspective of point processes](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.606.8241&rep=rep1&type=pdf). In Lévy processes (pp. 401-415). Birkhäuser Boston.

## Books
* Bertoin, J. (1998). [Lévy processes](https://www.goodreads.com/book/show/5109634-livy-processes). Cambridge university press.
* Sato, Ken-iti (1999). [Lévy processes and infinitely divisible distributions](https://www.goodreads.com/book/show/1197049.Levy_Processes_and_Infinitely_Divisible_Distributions). Cambridge university press.
* Applebaum, D. (2009). [Lévy processes and stochastic calculus](https://www.goodreads.com/book/show/796448.Levy_Processes_and_Stochastic_Calculus). Cambridge university press.
* Tankov, P. (2003). [Financial modelling with jump processes](https://www.goodreads.com/book/show/342669.Financial_Modelling_with_Jump_Processes). CRC press.
* Schoutens, Wim (2003). [Levy Processes in Finance](https://www.goodreads.com/book/show/16784702-levy-processes-in-finance). John Wiley & Sons.


