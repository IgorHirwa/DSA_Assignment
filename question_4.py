def time_complexity(n):
    return max(n)

if __name__ == '__main__':
    import random
    import timeit
    import matplotlib.pyplot as plt


    # Creation of different inputs
    # input is increasing the size
    item1 = random.sample(range(1,100),20)
    item2 = random.sample(range(1,100),45)
    item3 = random.sample(range(1,100),90)
    item4 = random.sample(range(1,100001),10000)

    # Define the size of the input (it's increasing)
    input_size =[20, 45, 90, 10000]

    # Define the time taken as input size
    time_taken = [timeit.timeit("time_complexity(\"item1\")", setup="from__main__import time_complexity"),
                  timeit.timeit("time_complexity(\"item2\")", setup="from__main__import time_complexity"),
                  timeit.timeit("time_complexity(\"item3\")", setup="from__main__import time_complexity")]
    big_size_input = [timeit.timeit("time_complexity(\'item4\')", setup="from__main__import time_complexity")]

    print(f'The big_size item range input is:{time_complexity(item1)}')
    print(f'The big_size item  range input is:{time_complexity(item2)}')
    print(f'The big_size item  range input is:{time_complexity(item3)}')
    print(f' respective time complexities is: {time_taken}')
    print(f'the estimated time complexity when input size is 10000 = {big_size_input}')

    # plotting the graph of input size and the time taken
    plt.plot(input_size, time_taken)

    # naming the axis
    plt.xlabel("input size")
    plt.ylabel("time taken")
    plot.show()







