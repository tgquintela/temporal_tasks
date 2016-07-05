
#Python
2016-06-01

Python is a widely used high-level, general-purpose, interpreted, dynamic programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java. The language provides constructs intended to enable clear programs on both a small and large scale.


The main features of Python language are:
* It supports multiple programming paradigms, including object-oriented, imperative and functional programming or procedural styles.
* Dynamic type system.
* Automatic memory management.
* Large and comprehensive standard library.
* Cross-platform. There are Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems.
* Strict but easy-to-read syntax. Python structures depends on indentation.

When we should use Python:
* If you want to use complex statistical models and structured programs to tackle statistical problems and not scripts (in that case is better R).
* For interactions with DB, web or others.
* General purpose programs but high-level programming projects.


The main statements and control flow are:
* if statement, which conditionally executes a block of code, along with else and elif (a contraction of else-if).
* for statement, which iterates over an iterable object, capturing each element to a local variable for use by the attached block.
* while statement, which executes a block of code as long as its condition is true.
* try statement, which allows exceptions raised in its attached code block to be caught and handled by except clauses; it also ensures that clean-up code in a finally block will always be run regardless of how the block exits.
* class statement, which executes a block of code and attaches its local namespace to a class, for use in object-oriented programming.
* def statement, which defines a function or method.
* with statement (from Python 2.5), which encloses a code block within a context manager (for example, acquiring a lock before the block of code is run and releasing the lock afterwards, or opening a file and then closing it), allowing Resource Acquisition Is Initialization (RAII)-like behavior.
* pass statement, which serves as a NOP. It is syntactically needed to create an empty code block.
* assert statement, used during debugging to check for conditions that ought to apply.
* yield statement, which returns a value from a generator function. From Python 2.5, yield is also an operator. This form is used to implement coroutines.
* import statement, which is used to import modules whose functions or variables can be used in the current program.
* print statement was changed to the print() function in Python 3.

### Syntax
The main special object types we have in python are:
* Iterator: an object which has the __iter__ function and returns with yield partial results using the statement for.
* Context manager: a user-defined runtime context that is entered before the statement body is executed and exited when the statement ends. The object has the functions __enter__ and __exit__ to define the enter functionality and the exit function when some error arises.
* Decorators: a function which is able to get a function or a class and call it surrounded by the decorator definition. It is used with '@' to call the function and it is placed in the previous line to the function or class we want to decorate.

***Tags***: Computer science, Computer engineering, Programming language

## See also
## See also:
[R](/r), [Julia](/julia), [SAS](/sas), [Matlab](/matlab), [Go (Programming language)](/go_(programming_language)), [Java](/java), [C](/c), [Fortran](/fortran), [Sage](/sage)
## Material
* https://www.python.org/
* https://en.wikibooks.org/wiki/Python_Programming
* https://wiki.python.org/moin/BeginnersGuide
* https://docs.python.org/devguide/

## Books
* Pilgrim, Mark. (2004) [Dive Into Python](https://www.goodreads.com/book/show/24038.Dive_Into_Python). Apress
* Matthes, Eric. (2015) [Python Crash Course: A Hands-On, Project-Based Introduction to Programming](https://www.goodreads.com/book/show/23241059-python-crash-course). No Starch Press
* Lutz, Mark (2006) [Programming Python](https://www.goodreads.com/book/show/80436.Programming_Python). O'Reilly Media
* Martelli, Alex; Ravenscroft, Anna; Ascher, David (2005) [Python Cookbook](https://www.goodreads.com/book/show/80437.Python_Cookbook). O'Reilly Media
* Shaw, Zed; Newman, Greg (2010) [Learn Python The Hard Way](https://www.goodreads.com/book/show/8341335-learn-python-the-hard-way).
* Martelli, Alex (2006) [Python in a Nutshell](https://www.goodreads.com/book/show/80438.Python_in_a_Nutshell). O'Reilly Media
* Sweigart, Albert (2014) [Automate the Boring Stuff with Python: Practical Programming for Total Beginners](https://www.goodreads.com/book/show/22514127-automate-the-boring-stuff-with-python). No Starch Press
* Dierbach, Charles (2013) [Introduction to Computer Science Using Python: A Computational Problem-Solving Focus](https://www.goodreads.com/book/show/19825917-introduction-to-computer-science-using-python). Wiley
* Lambert, Kenneth A. (2013) [Fundamentals of Python: Data Structures](https://www.goodreads.com/book/show/17993410-fundamentals-of-python). Cengage Learning
* Danjou, Julien (2014) [The Hacker's Guide to Python](https://www.goodreads.com/book/show/21796023-the-hacker-s-guide-to-python). Lulu.com
* Bird, Steven; Klein, Ewan; Loper, Edward (2009) [Natural Language Processing with Python](https://www.goodreads.com/book/show/6392569-natural-language-processing-with-python). O'Reilly Media
* Garrad, Chris (2016) [Geoprocessing with Python](https://www.goodreads.com/book/show/27037122-geoprocessing-with-python). Manning Publications
* Lawhead, Joel (2013) [Learning Geospatial Analysis with Python](https://www.goodreads.com/book/show/18766948-learning-geospatial-analysis-with-python). Packt Publishing
* Westra, Erick (2013). [Python Geospatial Development](https://www.goodreads.com/book/show/17991315-python-geospatial-development-second-edition). 2nd Edition, Packt Publishing
* Toms, Silas (2015). [ArcPy and ArcGIS - Geospatial Analysis with Python](https://www.goodreads.com/book/show/25049835-arcpy-and-arcgis---geospatial-analysis-with-python). Packt Publishing
* Bahgat, Karim (2015). [Python Geospatial Development Essentials](https://www.goodreads.com/book/show/28452854-python-geospatial-development-essentials). Packt Publishing
* Richert, Willi; Coelho, Luis Pedro (2013). [Building Machine Learning Systems with Python](https://www.goodreads.com/book/show/18248285-building-machine-learning-systems-with-python). Packt Publishing Limited
* McKinney, Wes (2012) [Python for Data Analysis](https://www.goodreads.com/book/show/14744694-python-for-data-analysis). O'Reilly Media
* Pierfederici, Francesco (2016) .[Distributed Computing with Python](https://www.goodreads.com/book/show/29929574-distributed-computing-with-python). Packt Publishing
* Julien, David (2016). [Designing Machine Learning Systems with Python](https://www.goodreads.com/book/show/29902360-designing-machine-learning-systems-with-python). Packt Publishing
* Boschetti, Alberto;Massaron, Luca   (2015). [Python Data Science Essentials](https://www.goodreads.com/book/show/25527772-python-data-science-essentials). Packt Publishing


