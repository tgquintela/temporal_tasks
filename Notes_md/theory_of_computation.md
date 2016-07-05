
#Theory of computation
2016-06-01

The theory of computation is the branch that deals with how efficiently problems can be solved on a model of computation, using an algorithm. The field is divided into three major branches:
* Automata theory and language
* Computability theory
* Computational complexity theory, which are linked by the question: "What are the fundamental capabilities and limitations of computers?"

In order to perform a rigorous study of computation, computer scientists work with a mathematical abstraction of computers called a model of computation. There are several models in use, but the most commonly examined is the Turing machine. Computer scientists study the Turing machine because it is simple to formulate, can be analyzed and used to prove results, and because it represents what many consider the most powerful possible "reasonable" model of computation. It might seem that the potentially infinite memory capacity is an unrealizable attribute, but any decidable problem solved by a Turing machine will always require only a finite amount of memory. So in principle, any problem that can be solved (decided) by a Turing machine can be solved by a computer that has a finite amount of memory.


### Models of computation
Aside from a Turing machine, other equivalent models of computation are in use:
* Lambda calculus: A computation consists of an initial lambda expression (or two if you want to separate the function and its input) plus a finite sequence of lambda terms, each deduced from the preceding term by one application of Beta reduction.
* Combinatory logic: is a concept which has many similarities to ${\displaystyle \lambda }$-calculus, but also important differences exist (e.g. fixed point combinator Y has normal form in combinatory logic but not in ${\displaystyle \lambda }$-calculus). Combinatory logic was developed with great ambitions: understanding the nature of paradoxes, making foundations of mathematics more economic (conceptually), eliminating the notion of variables (thus clarifying their role in mathematics).
* μ-recursive functions: a computation consists of a mu-recursive function which are a class of partial functions from natural numbers to natural numbers that are "computable" in an intuitive sense. They take finite tuples of natural numbers and return a single natural number. Each entry in any function needs to be an application of a basic function or follow from the entries by using *composition*, *primitive recursion* or *μ recursion*.The computation terminates only if the final term gives the value of the recursive function applied to the inputs.
* Markov algorithm: a string rewriting system that uses grammar-like rules to operate on strings of symbols.
* Register machine: is a theoretically interesting idealization of a computer.

    is a theoretically interesting idealization of a computer. There are several variants. In most of them, each register can hold a natural number (of unlimited size), and the instructions are simple (and few in number), e.g. only decrementation (combined with conditional jump) and incrementation exist (and halting). The lack of the infinite (or dynamically growing) external store (seen at Turing machines) can be understood by replacing its role with Gödel numbering techniques: the fact that each register holds a natural number allows the possibility of representing a complicated thing (e.g. a sequence, or a matrix etc.) by an appropriate huge natural number - unambiguity of both representation and interpretation can be established by number theoretical foundations of these techniques.

In addition to the general computational models, some simpler computational models are useful for special, restricted applications. Regular expressions, for example, specify string patterns in many contexts, from office productivity software to programming languages. Another formalism mathematically equivalent to regular expressions, Finite automata are used in circuit design and in some kinds of problem-solving. Context-free grammars specify programming language syntax. Non-deterministic pushdown automata are another formalism equivalent to context-free grammars. Primitive recursive functions are a defined subclass of the recursive functions.

Different models of computation have the ability to do different tasks. One way to measure the power of a computational model is to study the class of formal languages that the model can generate; in such a way to the Chomsky hierarchy of languages is obtained.

***Tags***: Computer science, Artificial Intelligence

## See also
## See also:
[Artificial Intelligence](/artificial_intelligence), [Computer Complexity](/computer_complexity), [Church-Turing thesis](/church-turing_thesis), [Turing Machines](/turing_machines)
## Papers
* Alan Turing (1937). [On computable numbers, with an application to the Entscheidungsproblem](https://people.cs.umass.edu/~immerman/cs601/TuringPaper1936.pdf). Proceedings of the London Mathematical Society (IEEE) 2 (42): 230-265

## Books
* Sipser, Michael (2013). [Introduction to the Theory of Computation 3rd](https://www.goodreads.com/book/show/16599897-introduction-to-the-theory-of-computation-michael-sipser). Cengage Learning
* Lewis, F. D. (2007). [Essentials of theoretical computer science](https://www.goodreads.com/book/show/13607576-essentials-of-theoretical-computer-science)
* Hopcroft, John E., and Jeffrey D. Ullman (2006). [Introduction to Automata Theory, Languages, and Computation](https://www.goodreads.com/book/show/1384026.Introduction_to_Automata_Theory_Languages_and_Computation). 3rd ed Reading, MA: Addison-Wesley.
* Cooper, S. Barry (2004). [Computability Theory](https://www.goodreads.com/book/show/2366835.Computability_Theory). Chapman and Hall/CRC.
* Hodges, Andrew (2012). [Alan Turing: The Enigma](https://www.goodreads.com/book/show/150731.Alan_Turing). Princeton University Press


