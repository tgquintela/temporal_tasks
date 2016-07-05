
#Artificial Neural Networks
2016-06-01

Artificial neural networks (ANNs) are a family of bio-inspired models which are used to estimate or approximate functions that can depend on a large number of inputs and are generally unknown. Artificial neural networks are typically specified using three things:
* *Architecture*: which specifies what variables are involved in the network and their topological relationships along with activities of the neurons. The architecture is defined by the number of neurons for each layer and the relationship between each ones through the definition of its weights.
* *Activity Rule*: most neural network models have short time-scale dynamics: local rules define how the activities of the neurons change in response to each other. Typically the activity rule depends on the weights (the parameters) in the network.
* *Learning Rule*: the learning rule specifies the way in which the neural network's weights change with time. This learning is usually viewed as taking place on a longer time scale than the time scale of the dynamics under the activity rule. Usually the learning rule will depend on the activities of the neurons. It may also depend on the values of the target values supplied by a teacher and on the current value of the weights.


The ANNs in the 3 main learning paradigms are:
* In Supervised learning (regression and classification) using MSE and gradient descend and backpropagation.
* In Unsupervised learning used for clustering or the estimation of statistical distributions, compression and filtering.
* Dynamic programming, which tackles the progrem of a decision making agent who has to take decisions in an environment modeled as MDP. Dynamic programming has been coupled with ANNs (Neuro dynamic programming) by Bertsekas and Tsitsiklis.


The main learning algorithms:
* Gradient descent: Most of the algorithms used in training artificial neural networks employ some form of gradient descent, using backpropagation to compute the actual gradients. This is done by simply taking the derivative of the cost function with respect to the network parameters and then changing those parameters in a gradient-related direction. The backpropagation training algorithms are usually classified into three categories:
	* Steepest descent (with variable learning rate, with variable learning rate and momentum, resilient backpropagation)
	* Quasi-Newton (Broyden-Fletcher-Goldfarb-Shanno, one step secant)
	* Levenberg-Marquardt and conjugate gradient (Fletcher-Reeves update, Polak-Ribiére update, Powell-Beale restart, scaled conjugate gradient). The training problem is in fact an inverse problem where our goal is to estimate the parameters of the neural network model. The Levenberg-Marquardt algorithm is shown to be more reliable in obtaining appropriate solutions to inverse problems than Gauss-Newton and quasi-Newton methods.
* Evolutionary methods
* Gene expression programming
* Simulated annealing
* Expectation-maximization
* Non-parametric methods
* Particle swarm optimization
* ...

***Tags***: Artificial Intelligence, Connectomics, Machine Learning

### See also
[Random Forest](/random_forest), [Machine Learning](/machine_learning)
## Papers
* Bertsekas, D. P., & Tsitsiklis, J. N. (1995, December). [Neuro-dynamic programming: an overview](http://web.mit.edu/people/dimitrib/NDP_Encycl.pdf). In Decision and Control, 1995., Proceedings of the 34th IEEE Conference on (Vol. 1, pp. 560-564). IEEE.
* Van Roy, B., Bertsekas, D. P., Lee, Y., & Tsitsiklis, J. N. (1997, December). [A neuro-dynamic programming approach to retailer inventory management](http://neuron.tuke.sk/~hudecm/PDF_PAPERS/retail.pdf). In Decision and Control, 1997., Proceedings of the 36th IEEE Conference on (Vol. 4, pp. 4052-4057). IEEE.

## Books
* Mehrotra, K., Mohan, C. K., & Ranka, S. (1997). [Elements of artificial neural networks](https://www.goodreads.com/book/show/2046567.Elements_of_Artificial_Neural_Networks). MIT press.
* Hassoun, M. H. (1995). [Fundamentals of artificial neural networks](https://www.goodreads.com/book/show/1553951.Fundamentals_of_Artificial_Neural_Networks). MIT press.


