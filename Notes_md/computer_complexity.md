
#Computer complexity
2016-06-01

Complexity theory is the field of theoretical computer science in which is studied whether a problem can be solved at all on a computer, but also how efficiently the problem can be solved. Two major aspects are considered: time complexity and space complexity, which are respectively how many steps does it take to perform a computation, and how much memory is required to perform that computation.

In order to analyze how much time and space a given algorithm requires, computer scientists express the time or space required to solve the problem as a function of the size of the input problem. For example, finding a particular number in a long list of numbers becomes harder as the list of numbers grows larger. If we say there are n numbers in the list, then if the list is not sorted or indexed in any way we may have to look at every number in order to find the number we're seeking. We thus say that in order to solve this problem, the computer needs to perform a number of steps that grows linearly in the size of the problem.

To simplify this problem, computer scientists have adopted **Big O notation**, which allows functions to be compared in a way that ensures that particular aspects of a machine's construction do not need to be considered, but rather only the asymptotic behavior as problems become large. So in our previous example we might say that the problem requires ${\displaystyle O(n)}$ steps to solve.

Perhaps the most important open problem in all of computer science is the question of whether a certain broad class of problems denoted NP can be solved efficiently. This is discussed further at Complexity classes P and NP, and P versus NP problem is one of the seven Millennium Prize Problems stated by the Clay Mathematics Institute in 2000. The Official Problem Description was given by Turing Award winner Stephen Cook.

***Tags***: Computer science, Artificial Intelligence

### See also
[Artificial Intelligence](/artificial_intelligence), [Computer Complexity](/computer_complexity), [Turing Machines](/turing_machines), [P versus NP problem](/p_versus_np_problem)
## Material
* https://en.wikipedia.org/wiki/File:Complexity_subsets_pspace.svg

## Papers
* S. Aaronson & A. Wigderson (2008). [Algebrization: A New Barrier in Complexity Theory](http://www.scottaaronson.com/papers/alg.pdf). Proceedings of ACM STOC'2008. pp. 731-740.

## Books
* Arora, Sanjeev; Barak, Boaz . [Computational complexity: a modern approach](https://www.goodreads.com/book/show/6535065-computational-complexity). Cambridge University Press, 2009.
* Papadimitriou, Christos H. (2003). [Computational complexity](https://www.goodreads.com/book/show/138562.Computational_Complexity). John Wiley and Sons Ltd., 2003.


