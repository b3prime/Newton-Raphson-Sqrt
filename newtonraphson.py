from timeit import default_timer as timer
import math


def sqrt(num):  #ex, 3
    #the nth guess, starting with the positive integer
    xn = num

    # let w = some root ex. root(2), or ~1.414... 
    # let xn = the current guess

    # f(x) = x^2 - w^2
    # this defines a parabola where the root is the intercepts of the function

    # no matter the input, x will always be squared. Thus, the derivative
    # always is 2x

    # THEORY:
    # once we have this current guess (xn), we'll find the tangeant line
    # of f at x = xn. Then, we'll find the x-intercept of this line,
    # and set that equal to the next guess! Repeat this.
    # it is clear that these rapidly converge to the solution of the function

    # point-slope formula is y-y1 = m(x-x1)
    # thus, the equation for our tangent line is y = 2xn * (x-xn) + (x^2-w^2)
    # x^2-w^2 is simply the y-value of the function

    # when y = 0,  0 = (2xn*x)-(2xn^2)+xn^2-w^2
    #           => 0 = (2xn*x)-(xn^2) +xn^2-s^2
    # isolating x, we get:
    #                        x = (xn^2 + w^2)/(2xn)
    
    # this is our x intercept for the current guess, xn !
    # we iteratively repeat this step, in order to converge to the solution

    for i in range(100):
        # find the x-intercept of the tangent line, this becomes the (n+1)th guess
        xint = ((xn ** 2) + num) / (2 * xn)
        xn = xint # update the guess/answer value

    return xn

while True:
    # our algorithm:
    case = float(input())

    start = timer()
    root = round(sqrt(case), 14)
    end = timer()

    print("Newton-Raphson Method:   Ans = " + str(root) + " in " + str(end-start) + " secs") # state our answer, the algorithm's time


    # python's algorithm

    start = timer()
    root = round(math.sqrt(case), 14)
    end = timer()

    print("Python's Builtin Method: Ans = " + str(root) + " in " + str(end-start) + " secs") # state the answer, and Python's time



