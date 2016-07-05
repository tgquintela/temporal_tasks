
#Data-driven programming
2016-06-01

Data-driven programming is a programming paradigm in which the program statements describe the data to be matched and the processing required rather than defining a sequence of steps to be taken.

Some data-driven languages are:
* sed (text-processing languages)
* AWK (text-processing languages)
* maildrop (Mail filtering language)
* procmail (Mail filtering language)
* Sieve (Mail filtering language)

Data-driven programming is typically applied to streams of structured data, for filtering, transforming, aggregating (such as computing statistics), or calling other programs. Typical streams include log files, delimiter-separated values, or email messages, notably for email filtering. Some data-driven languages are Turing-complete, such as AWK and even sed, while others are intentionally very limited, notably for filtering.

Data-driven languages frequently have a default action: if no condition matches, line-oriented languages may print the line (as in sed), or deliver a message (as in sieve). In some applications, such as filtering, matching is may be done exclusively (so only first matching statement), while in other cases all matching statements are applied. In either case, failure to match any pattern may be "default behavior" or can be seen as an error, to be caught by a catch-all statement at the end.

While the benefits and issues may vary between implementation, there are a few big potential benefits of and problems with this paradigm:
* Simplify interaction with data problems.
* prevent coupling of data and functionality
* Sometimes it has been argued to lead to bad object-oriented design, especially when dealing with more abstract data.

***Tags***: Computer engineering, Programming

## See also
## See also:
[Programming paradigm](/programming_paradigm), [Concurrent programming](/concurrent_programming)

