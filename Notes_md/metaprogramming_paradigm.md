
#Metaprogramming paradigm
2016-06-01

Metaprogramming is the programming paradigm about writing of computer programs with the ability to treat programs as their data. It means that a program could be designed to read, generate, analyse or transform other programs, and even modify itself while running. In some cases, this allows programmers to minimize the number of lines of code to express a solution (hence reducing development time), or it gives programs greater flexibility to efficiently handle new situations without recompilation.

The language in which the metaprogram is written is called the metalanguage. The language of the programs that are manipulated is called the object language. The ability of a programming language to be its own metalanguage is called reflection or reflexivity.

Reflection is a valuable language feature to facilitate metaprogramming. Having the programming language itself as a first-class data type (as in Lisp, Prolog, SNOBOL, or Rebol) is also very useful; this is known as homoiconicity. Generic programming invokes a metaprogramming facility within a language, in those languages supporting it.

Metaprogramming usually works in one of three ways:
* Exposing the internals of the run-time engine to the programming code through application programming interfaces (APIs). 
* Dynamic execution of expressions that contain programming commands, often composed from strings, but can also be from other methods using arguments or context. Thus, "programs can write programs." Although both approaches can be used in the same language, most languages tend to lean toward one or the other.
* Step outside the language entirely. General purpose program transformation systems such as compilers, which accept language descriptions and can carry out arbitrary transformations on those languages, are direct implementations of general metaprogramming. This allows metaprogramming to be applied to virtually any target language without regard to whether that target language has any metaprogramming abilities of its own.

### TODO:
* Relate that with Templates and Macros.

***Tags***: Computer engineering, Programming

### See also
[Programming paradigm](/programming_paradigm)
## Books
* Perrota, Paolo (2010). [Metaprogramming Ruby](https://www.goodreads.com/book/show/7183279-metaprogramming-ruby). Pragmatic Bookshelf


