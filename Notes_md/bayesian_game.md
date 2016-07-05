
#Bayesian game
2016-06-01

A Bayesian game is one in which information about characteristics of the other players (i.e. payoffs) is incomplete. Such games can be converted into games of complete but imperfect information under the "common prior assumption".

Following John C. Harsanyi's framework, a Bayesian game can be modelled by introducing Nature as a player in a game. Nature assigns a random variable to each player which could take values of types for each player and associating probabilities or a probability density function with those types (in the course of the game, nature randomly chooses a type for each player according to the probability distribution across each player's type space). Harsanyi's approach to modeling a Bayesian game in such a way allows games of incomplete information to become games of imperfect information (in which the history of the game is not available to all players). The type of a player determines that player's payoff function. The probability associated with a type is the probability that the player, for whom the type is specified, is that type. In a Bayesian game, the incompleteness of information means that at least one player is unsure of the type (and so the payoff function) of another player.

Such games are called Bayesian because of the probabilistic analysis inherent in the game. Players have initial beliefs about the type of each player (where a belief is a probability distribution over the possible types for a player) and can update their beliefs according to Bayes' rule as play takes place in the game, i.e. the belief a player holds about another player's type might change on the basis of the actions they have played. The lack of information held by players and modeling of beliefs mean that such games are also used to analyse imperfect information scenarios.

A Bayesian game can be formally defined as a 7-tuple (${\displaystyle G=\langle N,\Omega ,\langle A_{i},u_{i},T_{i},\tau _{i},p_{i},C_{i}\rangle _{i\in N}\rangle }$) in which:
* ${\displaystyle N}$ is the set of players.
* ${\displaystyle \Omega }$ is the set of states of nature. For instance, in a card game, it can be any order of the cards.
* ${\displaystyle A_{i}}$ is the set of actions for player ${\displaystyle i}$. Let ${\displaystyle A=A_{1}\times A_{2}\times \dotsb \times A_{N}}$.
* ${\displaystyle T_{i}}$ is the type of player ${\displaystyle i}$, decided by the function ${\displaystyle \tau _{i}\colon \Omega \rightarrow T_{i}}$. So for each state of the nature, the game will have different types of players. The outcome of the players is what determines its type. Players with the same outcome belong to the same type.
* ${\displaystyle C_{i}\subseteq A_{i}\times T_{i}}$ defines the available actions for player ${\displaystyle i}$ of some type in ${\displaystyle T_{i}}$.
* ${\displaystyle u_{i}\colon \Omega \times A\rightarrow R}$ is the payoff function for player ${\displaystyle i}$. More formally, let ${\displaystyle L=\{(\omega ,a_{1},\dotsc ,a_{N})\mid \omega \in \Omega ,\forall i,(a_{i},\tau _{i}(\omega ))\in C_{i}\}}$, and ${\displaystyle u_{i}\colon L\rightarrow R}$.
* ${\displaystyle p_{i}}$ is the probability distribution over ${\displaystyle \Omega }$ for each player ${\displaystyle i}$, that is to say, each player has different views of the probability distribution over the states of the nature. In the game, they never know the exact state of the nature.

A pure strategy is the ones which has only one strategy in the bayesian density. We can defined a *Bayesian Equilibrium* of the game ${\displaystyle G}$ is defined to be a (possibly mixed strategy) Nash equilibrium of the game. Each Bayesian Game always have at least one Bayesian Equilibria.

***Tags***: Game Theory

## See also
## See also:
[Game Theory](/game_theory)
## Material
* [Game Theory Coursera's course](https://class.coursera.org/gametheory-003/lecture/109). Coursera. Retrieved 2016-06-16.

## Papers
* Harsanyi, John C., 1967/1968. [Games with Incomplete Information Played by Bayesian Players, I-III](). Management Science 14 (3): 159-183 (Part I), 14 (5): 320-334 (Part II), 14 (7): 486-502 (Part III).


