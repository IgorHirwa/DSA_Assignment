# Implement a basic measure of tracking the space used by an algorithm

from memory_profiler import profile

@profile # the function decorator that will on every process track storage used by the function
def algorithm():
    # An algorithm to print the x values whose f(x) for f(x) = x^2 are divisible by 2
    x = 1
    # x and y lists for x and y values to be saved
    x_values = []
    y_values = []
    while x < 10:
        y = x ** 2
        if y % 2 == 0:
            x_values.append(x)
            y_values.append(y)
        x = x + 1
    print("The x values are", x_values)
    print("The y values are", y_values)

algorithm() # function call
