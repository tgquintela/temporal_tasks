
# How to code a framework software?

## What is a framework?
First of all, what is a framework and what is the differences with other types of software? In software a framework is an standard way to solve a problem. There are frameworks to encapsulate methodologies of team management and software development, but here I am talking about a code framework. A software coded to tackle some general and diverse problem. This software has to be adaptable to all the diversity that this general problem can bring to us. That  means that the framework by itself is not able to solve any problem but it gives the possibility for the programmers to solve problems with little effort (less than facing the problem from scratch).
The main properties of a framework are:
* _Flow control_: the framework controls the main flow of the program. It is said that software frameworks rely on the *Hollywood Principle*: "Don't call us, we'll call you." (or technically known as [inversion of control](https://en.wikipedia.org/wiki/Inversion_of_control)).
* _Extensibility_: the framework, even it usually has a default behaviour, it has _holes_ (or _hot spots_ in opposite to the _frozen spots_) in which the user has to put functions (precoded and come with the framework) or coded by the user to provided specific functionality.
* _Immutability of code_: in order to get some functionality the user should not modify the framework code.

The requirements and exigences that this class of software produce to the programmers who have to code it are different from the ones required to code scripts, simple software structure or even coding complex structure software. It requires high level of abstraction, well knowledge of the family of problems you are willing to tackle with this framework and taking decisions in form of internal standards which will condition the future coding of other parts of the framework.

## Planning
As all the programming task, previously to start coding you have to know what you are going to code, which tools can help you, how are going to develop your project and how are you going to manage your time. 

All these questions sometimes are well known in theory but nonetheless we are not planning properly. Usually, short projects can be solved on the fly when you are coding, but this is not the case. Planning probably is the most tough task between the ones related with the development of any project, but even harder in the case of the framework software development.
The main questions we have to answer previously even to start a coding or management planning are:
* It is really a need to code this framework? A framework is a really costly process, intellectually and in time. Before you start, you need to be sure this effort will be worthwhile. You have to be sure to know the possible alternatives in the community or in private solutions which try to tackle this same problem, and consider them to your problem. If these alternatives are not valuable for your problem you will have to consider if your problem is enough general and the investment of efforts will be rewarded in the future (if it is going to be a 1-use program forget it).
If your response is '*no*', try to solve your problem without overloading your task and overgeneralizing your code. You could easily suffer of some well known anti-patterns in software engineering as [Lasagna code](https://en.wikipedia.org/wiki/Lasagna_code), [Yo-yo problem](https://en.wikipedia.org/wiki/Yo-yo_problem) or [Object orgy](https://en.wikipedia.org/wiki/Object_orgy) all of them related to the act of being more ambitious than the problem requires from you.
* Which programming language are you going to use? This decision is usually complicated.
The main different variables you have to consider before you take the decision are:
- Good knowledge of the language from the major part of the programmers involved in the project.
- Tools which can help to save time and efforts.
- Stability in future time.

* Which external tools do you want to use? It is convenient to not reinvent the wheel but external dependencies could be dangerous and you can lose the control of your own code. The balance is up to you but there are ways to isolate these dependences in order to quick substitution if it is needed in the future.

After solving these main initial questions it starts the moment of planning. In order to do that we have to solve another set of questions:
* What are our resources in time and labor power? A very extensive team creates problems of communication, but we have to balance that with our time resources.
It is always dangerous to have loose deadlines or deadlines with a very big workload. Small goals and strong deadlines could always help. The use of coordinations tools as the ones it give to us the software development methodologies and paradigms in software engineering could help us to reach better productivity.

This is the moment to select how to track the project and how to organize the team if there are more than one developer in the project.
The selection has to be in coherence with the resources you have available. There are tracking methodologies that are time expensive but worthwhile in the long-term, others by the contrary are better adapted for the short projects and other ones are more focused in coordinations and communication from the team. Depending on the size of the team developing the project or how connected are the different tasks related with the code that each part of the team has to develop.

After selecting methodology of management team and time it is the hour of planning the code path. There are a lot of ways to build the software but there are better ways to do it than others. It is important:
* Keep as much time as you can a covered development (the code is useful and can be tested and even can give partial result if it is possible). In the other case the programmers can be unmotivated and frustrated without short-term incentives.
* Select which parts of the code are the framework _frozen spots_ and which ones are the _hot spots_ or holes which the programmers and users has to fill with their code.
* Plan the design of the code which tries to reduce the conceptual distance between the code and the problem to tackle. 
* Model all the possible family of problems by preparing artificial data which simulates all the possible problems we think, the framework will have to tackle with.

A good planning design has to be easy to understand to all the developers of the team and has to fill the first developing tasks of the first days.


## Development and tracking the project
After setting the plan and the methodologies we are going to use, it is time to keep the plan going. That seems an easy task but, without experience or even the good routine, it is not as easy as it seems. We are always tempted to avoid small but long-term worthwhile efforts.
The control of the times has to be strict, and incentives and motivations has to be present all along the process.
If the methodologies you are going to use are new for most of the team, the best practice, if it is possible, is to get some external person to track the team and the development management.

My main recommendations about development and tracking project are:
* For not experts it is better to use natural periods (days, weeks, months) rather than periods related with the development of the own project. It is better to have the feeling you are leading the project and not that the project is leading you and your work (so better don't start with [Chaos model software development](https://en.wikipedia.org/wiki/Chaos_model) ;))
* Be regular and try to use the same methodology from the start till then end of the project. There will be for sure other projects and other opportunities to use other methodologies, but do not change methodologies in the middle of them.
* Be strict, work harder, keep your motivation and help to keep the motivation of your partners.


## Coding
At the end, the final product is the code. All written text in that post and all the extra efforts recommended are to put more quality in the resultant code with the least final effort as possible.
A good planning of code is critical to have a good framework but also a good development.

The development of the code will be highly dependent of the code planning. Depending of the project is useful to have a good plan of the whole software using tools as UML or others related, but others it is better to have a more open planning. An open planning it usually only indicates not the whole structure by itself but the relation of the new updates of code with the actual structure.

The most valuable recommendations I could give to you in the framework coding are:
* Code the artificial data generators with all possible cases we want to tackle.
* Code an example for each of the _hot spots_, or 'holes' (the personalization parts of the framework code)
* Code possible experiments for possible real cases you have available.

If we have followed properly the recommendations given in the planning part, we should be able to code more or less easily a primer version of all these points.
Once we have code a primer version of these points, the development will be more or less covered. The work of the developers will be: to code versions of the framework, to create partial test for these new parts of the code, to adapt the general tests for the new reality of the code and to adapt internal structures of interaction between the parts of the code.

Each project is very different and if there was able to give all the possible good recommendations, the project managers would not be needed.
My summary of general, and for that reason valuable for most of the projects, advises are:
* It is better to do an adaptable class (in parameters and in functions) rather to do a lot of different classes for each cases.
* Exploit the power of combination. That is related to the previous advises.
Study and explore the possible combinations of parameters which gives similar and factorizable properties that can be faced with same coding tools. These natural groups you can create by adaptation to the nature of the problem has to be translated into different classes or methods in the code. A proper balance comes from putting as most number of natural combinations of parameters as possible but keeping the global structure recognizable and without turning the code into a [spaghetti code](https://en.wikipedia.org/wiki/Spaghetti_code) or with too much ifs.
* If there are object methods, which are going to be called a lot of times, try to adapt the class to the problem in the instantiation, by formatting functions and parameters properly in order to avoid useless extra computations.
* Try to not fall in the '_factorization trap_', in which you start factoring classes and building 3 or 4 level of inheritance classes when it is not required (see [Lassagna code](https://en.wikipedia.org/wiki/Lasagna_code)).
* Use tests but not let the tests lead the code for you (see [Tester Driven Development](https://en.wikipedia.org/wiki/Tester_Driven_Development))
* Use control versions properly. Do not store in the last version useless and deprecated code ([Boat anchor](https://en.wikipedia.org/wiki/Tester_Driven_Development))
* Do not try to do a premature re-factorization or premature optimization.
* Do not copy paste code. It is not beautiful and a not very efficient strategy.
* [Stackoverflow](http://stackoverflow.com/) is your friend ;)
* Have patience in the lasts steps of the project. Each change of the code implies to worry about too many other lines dispersed around all the code due to the *strong correlations* there are in framework codes or other codes with strong structure. It is easy to fail trying to guess the time remaining. This is known as the [90-90 rule](https://en.wikipedia.org/wiki/Ninety-ninety_rule).
* Enjoy programming a lot else there are other easier programming projects.


# Conclusions
Bad organization in a long project can make the difference. The productivity between a well lead project and an uncoordinated and uncontrolled one is usually huge. Having a good control of the times and a good coordination between the efforts of each one of the team is a differential factor.
Indeed, all the exposed in that blog post is a general theory that almost everybody knows when they start coding or developing big projects. But this knowledge don't avoid people to get lost and go wrong in most of the essential parts. That is why the actual content is in the between-lines messages and the balances that the post mention. These are the really differential factor.
Experience and failing is part of the process of learning to check the balances intuitively and apply all the things mentioned in a proper way. And of course, try to not be arbitrary.

If you are thinking to start a project of coding a framework I hope this post was useful. Be patient and good luck.





