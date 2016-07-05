
#Alpha-beta pruning
2016-06-01

Alpha-beta pruning is a search algorithm that seeks to decrease the number of nodes that are evaluated by the *minimax algorithm* in its search tree. It is an adversarial search algorithm used commonly for machine playing of two-player games. It stops completely evaluating a move when at least one possibility has been found that proves the move to be worse than a previously examined move. Such moves need not be evaluated further. When applied to a standard minimax tree, it returns the same move as minimax would, but prunes away branches that cannot possibly influence the final decision.

In game theory it is also used as an algorithm to evaluate and search better options with minimax algorithm through the decision tree extended form of the game.

***Tags***: Game Theory, Graph, Algorithm

#### See also
[Game Theory](/game_theory)
## Papers
* Edwards, D.J.; Hart, T.P. (4 December 1961 to 28 October 1963). [The Alpha-beta Heuristic](http://dspace.mit.edu/bitstream/handle/1721.1/6098/AIM-030.pdf?sequence=2). (AIM-030) Massachusetts Institute of Technology.
* Knuth, D. E.; Moore, R. W. (1975). [An Analysis of Alpha–Beta Pruning](http://www.ime.usp.br/~rbrito/docs/1-s2.0-0004370275900193-main.pdf). Artificial Intelligence 6 (4): 293-326.
* Pearl, Judea; Korf, Richard (1987), [Search techniques](http://www.annualreviews.org/doi/pdf/10.1146/annurev.cs.02.060187.002315), Annual Review of Computer Science 2: 451-467


