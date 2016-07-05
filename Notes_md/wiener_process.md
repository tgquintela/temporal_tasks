
#Wiener process
2016-06-01

The Wiener process, also known as Brownian motion after Robert Brown, is a continuous-time stochastic process named in honor of Norbert Wiener. It is one of the best known Lévy processes

It is often called standard Brownian motion, after Robert Brown. It is one of the best known Lévy processes and occurs frequently in pure and applied mathematics, economics, quantitative finance, and physics. Wiener process gave rise to the study of continuous time martingales. It is a key process in terms of which more complicated stochastic processes can be described.

The Wiener process has applications throughout the mathematical sciences:
* To study Brownian motion
* The diffusion of minute particles suspended in fluid
* Other types of diffusion via the Fokker-Planck and Langevin equations
* The basis for the rigorous path integral formulation of quantum mechanics (by the Feynman-Kac formula, a solution to the Schrödinger equation can be represented in terms of the Wiener process)
* The study of eternal inflation in physical cosmology
* Theory of finance, in particular the Black-Scholes option pricing model


### Formalization

Basic properties that define a Wiener process $W_t$:
* $W_0$ = 0
* $W$ has independent increments: $W_{t+u} - W_t$ is independent of $\sigma(W_s : s \leq t)$ for $u \geq 0$.
* $W$ has Gaussian increments: $W_{t+u} - W_t$ is normally distributed with mean 0 and variance $u$, $W_{t+u}-W_t \sim  N(0, u)$
* $W$ has continuous paths: With probability 1, $W_t$ is continuous in t.

Basic properties:
* It is scale invariant, meaning that the $\alpha$-family ${\displaystyle \alpha ^{-1}W_{\alpha ^{2}t}}$ is also a Wiener process for $\alpha \neq 0$.
* The *unconditional probability density function* follows *normal distribution* with mean = 0 and variance = t.
* ${\displaystyle E[W_{t}]=0}$.
* ${\displaystyle \operatorname {Var} (W_{t})=E\left[W_{t}^{2}\right]-E^{2}[W_{t}]=E\left[W_{t}^{2}\right]-0=E\left[W_{t}^{2}\right]=t}$.
* It is a martingale.
* As quadratic variation [$W_t$, $W_t$] = $t$ the process $W_t - t$ it is also a martingale.

***Tags***: Stochastic processes

#### See also
[Markov process](/markov_process), [Levy process](/levy_process)
## Papers
* Shlesinger, Michael F.; Klafter, Joseph; Zumofen, Gert (December 1999). [Above, below and beyond Brownian motion](http://caos.fs.usb.ve/~srojas/Teaching/USB/MC_Intro/MC_readings_a/MC_a4_brownian_1.pdf). American Journal of Physics 67 (12): 1253-1259.

## Books
* Kleinert, Hagen (2004). [Path Integrals in Quantum Mechanics, Statistics, Polymer Physics, and Financial Markets](http://users.physik.fu-berlin.de/~kleinert/b5/psfiles/pi.pdf) (4th ed.). Singapore: World Scientific
* Revuz, Daniel; Yor, Marc (1994). [Continuous martingales and Brownian motion]() (Second ed.). Springer-Verlag.


