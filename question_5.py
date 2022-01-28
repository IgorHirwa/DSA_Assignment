# number 3(1)
import time
start= time.time()

def maximun_value():
    the_list = [89, 93, 45, 20, 54, 93.4, 92, 39, 93]
    maximum = max(the_list)
    print("The maximum value in the list is", maximum)
maximun_value()

end = time.time()
final=(end-start)
print("The time taken to run the algorithm is",final)


# number 3(2)
import time

start= time.time()

def lower_case():
    text = "WelcOME To MicroSOFT OFFICE, to contINUE, PURCHase the lATEST mIcrOSOft device"
    reviewed_text = text.casefold()
    print(reviewed_text)
lower_case() # function call
end = time.time()
final=(end-start)# variable to hold the time difference
print("The time taken to run the algorithm is",final)


# number 3(3)
import time
start= time.time()

def list_sorting():
    integer_list = [89, 93, 45, 20, 54, 93.4, 92, 39, 93]
    # Sorting the list from lowest to highest
    integer_list.sort()
    print("The sorted list from lowest to highest is", integer_list)
    # Sorting in the reverse order
    integer_list.sort(reverse=True)
    print("The sorted list from highest to lowest is", integer_list)
list_sorting() # function call

end = time.time()
final=(end-start)
print("The time taken to run the algorithm is",final)

