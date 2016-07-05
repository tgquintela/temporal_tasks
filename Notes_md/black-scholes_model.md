
#Black-Scholes model
2016-06-01

The Black–Scholes or Black-Scholes-Merton model is a mathematical model of a financial market containing derivative investment instruments. From the model, one can deduce the Black-Scholes formula, which gives a theoretical estimate of the price of European-style options. The formula led to a boom in options trading and legitimised scientifically the activities of the Chicago Board Options Exchange and other options markets around the world. It is widely used, although often with adjustments and corrections, by options market participants. Many empirical tests have shown that the Black-Scholes price is "fairly close" to the observed prices, although there are well-known discrepancies such as the "option smile".

The Black-Scholes model was first published by Fischer Black and Myron Scholes in their 1973 paper, "The Pricing of Options and Corporate Liabilities", published in the Journal of Political Economy. They derived a partial differential equation, now called the Black–Scholes equation, which estimates the price of the option over time. The key idea behind the model is to hedge the option by buying and selling the underlying asset in just the right way and, as a consequence, to eliminate risk. This type of hedging is called delta hedging and is the basis of more complicated hedging strategies such as those engaged in by investment banks and hedge funds.

Robert C. Merton was the first to publish a paper expanding the mathematical understanding of the options pricing model, and coined the term "Black-Scholes options pricing model". Merton and Scholes received the 1997 Nobel Memorial Prize in Economic Sciences for their work. Though ineligible for the prize because of his death in 1995, Black was mentioned as a contributor by the Swedish Academy.

The model's assumptions have been relaxed and generalized in many directions, leading to a plethora of models that are currently used in derivative pricing and risk management. It is the insights of the model, as exemplified in the Black-Scholes formula, that are frequently used by market participants, as distinguished from the actual prices. These insights include no-arbitrage bounds and risk-neutral pricing. The Black-Scholes equation, a partial differential equation that governs the price of the option, is also important as it enables pricing when an explicit formula is not possible.

The Black–Scholes formula has only one parameter that cannot be observed in the market: the average future volatility of the underlying asset. Since the formula is increasing in this parameter, it can be inverted to produce a "volatility surface" that is then used to calibrate other models, e.g. for OTC derivatives.

### Model description
The model is based in the next terms:
* The price of the stock ($S$), which will sometimes be a random variable and other times a constant.
* The price of a derivative as a function of time and stock price ($V(S,t)$).
* The price of a European call option ($C(S,t)$).
* The price of a European put option ($P(S,t)$).
* The strike price of the option ($K$).
* The annualized risk-free interest rate, continuously compounded ($r$).
* The drift rate of the price stock $S$ annualized ($\mu$).
* The standard deviation of the stock's returns; this is the square root of the quadratic variation of the stock's log price process ($\sigma$).
* A time in years; we generally use: now=0, expiry=T ($t$).
* The value of a portfolio ($\Pi$).

assumptions on the assets:
* *riskless rate*: The rate of return on the riskless asset is constant and thus called the risk-free interest rate.
* *random walk*: the instantaneous log return of stock price is an infinitesimal random walk with drift; more precisely, it is a geometric Brownian motion, and we will assume its drift and volatility is constant (if they are time-varying, we can deduce a suitably modified Black–Scholes formula quite simply, as long as the volatility is not random).
* The stock does not pay a dividend.

assumptions on the market:
* There is no arbitrage opportunity (i.e., there is no way to make a riskless profit).
* It is possible to borrow and lend any amount, even fractional, of cash at the riskless rate.
* It is possible to buy and sell any amount, even fractional, of the stock (this includes short selling).
* The above transactions do not incur any fees or costs (i.e., frictionless market).


As above, the Black-Scholes equation is a partial differential equation, which describes the price of the option over time. The equation is:

$${\displaystyle {\frac {\partial V}{\partial t}}+{\frac {1}{2}}\sigma ^{2}S^{2}{\frac {\partial ^{2}V}{\partial S^{2}}}+rS{\frac {\partial V}{\partial S}}-rV=0}$$

***Tags***: Economics

## Material
* [Explanation Black-Scholes equation from Terence Tao](https://terrytao.wordpress.com/2008/07/01/the-black-scholes-equation/)
* [Step-by-step solution of the Black-Scholes PDE](http://planetmath.org/encyclopedia/AnalyticSolutionOfBlackScholesPDE.html), planetmath.org.
* Ian Stewart, (2012). [The mathematical equation that caused the banks to crash](https://www.theguardian.com/science/2012/feb/12/black-scholes-equation-credit-crunch). TheGuardian

## Papers
* Black, F., & Scholes, M. (1973). [The pricing of options and corporate liabilities](https://www.cs.princeton.edu/courses/archive/fall02/cs323/links/blackscholes.pdf). The journal of political economy, 637-654.
* MacBeth, J. D., & Merville, L. J. (1979). [An Empirical Examination of the Black‐Scholes Call Option Pricing Model](http://efinance.org.cn/cn/fe/19791204An%20Empirical%20Examination%20of%20the%20Black-Scholes%20Call%20Option%20Pricing%20Model,%20pp..pdf). The Journal of Finance, 34(5), 1173-1186.

## Books
* Stewart, I. (2012). [In pursuit of the unknown: 17 equations that changed the world](https://www.goodreads.com/book/show/13237758-in-pursuit-of-the-unknown). Basic Books.
* Chriss, N. (1996). [Black Scholes and Beyond: Option Pricing Models](https://www.goodreads.com/book/show/59615.Black_Scholes_and_Beyond). McGraw-Hill.


