import numpy as np

def gradient_descent(x, y):
    m = 0
    c = 0
    Learning_rate = float(input("give a learning rate:"))
    l = Learning_rate  # The learning Rate
    precision = 0.000001  # This tells us when to stop the algorithm
    cost_func = 1  # This will be the value of Cost function
    iteration = int(input("Give total number iterations:"))
    i = iteration  # The number of iterations to perform gradient descent
    iters = 0  # Iteration counter
    n = len(x)  # Number of elements in x
    while cost_func > precision and iters < i:
        y_pred = m * x + c  # The current predicted value of y
        diff = y - y_pred  # Difference in value between actual y and predicted y
        cf = (1/n) * sum(diff ** 2)  # Finding the cost function
        D_m = (-2 / n) * sum(x * diff)  # partial differentiation wrt m
        D_c = (-2 / n) * sum(diff)  # partial differentiation wrt c
        m = m - l * D_m  # Update m
        c = c - l * D_c  # Update c
        cost_func = abs(cf)
        iters = iters + 1
        print("Iteration", iters, "\n M=", m, " C=", c, "Cost_function=", cf)

y = np.array([1,4])
x = np.array([0,1])

gradient_descent(x, y)
