
#Gamma process
2016-06-01

A gamma process ${\displaystyle \Gamma (t;\gamma ,\lambda )}$ is a random process with independent gamma distributed increments. It is a pure-jump increasing Lévy process with intensity measure ${\displaystyle \nu (x)=\gamma x^{-1}\exp(-\lambda x)}$ for $x > 0$. Thus jumps whose size lies in the interval ${\displaystyle [x,x+dx]}$ occur as a Poisson process with intensity ${\displaystyle \nu (x)dx}$.

### Formalization and properties

The main properties are:
* Mean: ${\displaystyle \gamma t/\lambda }$
* Variance ${\displaystyle \gamma t/\lambda ^{2}}$.
* Scaling: ${\displaystyle \alpha \Gamma (t;\gamma ,\lambda )=\Gamma (t;\gamma ,\lambda /\alpha )\,}$
* Adding independent processes: ${\displaystyle \Gamma (t;\gamma _{1},\lambda )+\Gamma (t;\gamma _{2},\lambda )=\Gamma (t;\gamma _{1}+\gamma _{2},\lambda )\,}$
* Moments: ${\displaystyle \mathbb {E} (X_{t}^{n})=\lambda ^{-n}\Gamma (\gamma t+n)/\Gamma (\gamma t),\ \quad n\geq 0}$, where ${\displaystyle \Gamma (z)}$ is the Gamma function.
* Moment generating function: ${\displaystyle \mathbb {E} {\Big (}\exp(\theta X_{t}){\Big )}=(1-\theta /\lambda )^{-\gamma t},\ \quad \theta <\lambda } \mathbb {E} {\Big (}\exp(\theta X_{t}){\Big )}=(1-\theta /\lambda )^{-\gamma t},\ \quad \theta <\lambda 
* Correlation: ${\displaystyle \operatorname {Corr} (X_{s},X_{t})={\sqrt {s/t}},\ s<t}$, for any gamma process ${\displaystyle X(t)}$.

***Tags***: Stochastic processes

## See also
## See also:
[Wiener process](/wiener_process), [Levy process](/levy_process), [Markov process](/markov_process), [Poisson process](/poisson_process)

