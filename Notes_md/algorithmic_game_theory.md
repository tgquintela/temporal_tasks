
#Algorithmic game theory
2016-06-01

Algorithmic game theory is an area in the intersection of game theory and algorithm design, whose objective is to design algorithms in strategic environments. Typically, in Algorithmic Game Theory problems, the input to a given algorithm is distributed among many players who have a personal interest in the output. In those situations, the agents might not report the input truthfully because of their own personal interests. On top of the usual requirements in classical algorithm design, say polynomial-time running time, good approximation ratio, ... the designer must also care about incentive constraints. We can see Algorithmic Game Theory from two perspectives:
* Analysis: look at the current implemented algorithms and analyze them using Game Theory tools: calculate and prove properties on their Nash equilibria, price of anarchy, best-response dynamics ...
* Design: design games that have both good game-theoretical and algorithmic properties. This area is called algorithmic mechanism design.

The field was started when Nisan and Ronen in STOC'99 drew the attention of the Theoretical Computer Science community to designing algorithms for selfish (strategic) users. As they claim in the abstract:

"We consider algorithmic problems in a distributed setting where the participants cannot be assumed to follow the algorithm but rather their own self-interest. As such participants, termed agents, are capable of manipulating the algorithm, the algorithm designer should ensure in advance that the agents’ interests are best served by behaving correctly.
Following notions from the field of mechanism design, we suggest a framework for studying such algorithms. In this model the algorithmic solution is adorned with payments to the participants and is termed a mechanism. The payments should be carefully chosen as to motivate all participants to act as the algorithm designer wishes. We apply the standard tools of mechanism design to algorithmic problems and in particular to the shortest path problem."

***Tags***: Game Theory, Multi-agent systems, Algorithmics

#### See also
[Game Theory](/game_theory)
## Material
* [Gambit: Software Tools for Game Theory](http://gambit.sourceforge.net/)
* [GAMUT](http://gamut.stanford.edu/) a suite of game generators designated for testing game-theoretic algorithms.
* [Stanford course: CS364A Fall 2013](http://theory.stanford.edu/~tim/f13/f13.html)
* [Éva Tardos' Cornell course: CS684 Spring 2004](http://www.cs.cornell.edu/courses/cs684/2004sp/)
* [Columbia course: COMS 6998-3](http://www.cs.columbia.edu/coms6998-3/)

## Papers
* Adkins, Robert. [Algorithmic Game Theory](https://www.semanticscholar.org/paper/Algorithmic-Game-Theory-Final-Report-for-Cmsc451-Adkins-Advisor/1afd6b07eefaff73f937eeb4dda37680949bdcc3/pdf). (2015). Random University Report

## Books
* Vazirani, Vijay V.; Nisan, Noam; Roughgarden, Tim; Tardos, Éva (2007), [Algorithmic Game Theory](http://www.cambridge.org/journals/nisan/downloads/Nisan_Non-printable.pdf), Cambridge, UK: Cambridge University Press.
* John von Neumann, Oskar Morgenstern (1944) [Theory of Games and Economic Behavior](https://www.goodreads.com/book/show/483055.Theory_of_Games_and_Economic_Behavior). Princeton Univ. Press.
* Nisan, N., Roughgarden, T., Tardos, E., & Vazirani, V. V. (2007). [Algorithmic game theory](https://www.goodreads.com/book/show/617100.Algorithmic_Game_Theory). (Vol. 1). Cambridge: Cambridge University Press.


