# Question 1
# A code to measure the time taken to run an algorithm
# importing time
import time
# Importing the algorithm whose runtime should be timed
import list_complexity_qn3
# Setting the starting time
start_time = time.time()
# Running the algorithm
list_complexity_qn3
time.sleep(1)
# Storing the end time
end_time = time.time()
time_difference = end_time - start_time
# Printing the time taken
print("The time taken to run the algorithm is", time_difference)

