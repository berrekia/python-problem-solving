from string_scripts import String
from sort_scripts import SortAlgos
from recursion_scripts import Recursion

import time
start = time.process_time()

n = int(input("Enter a number, please : \n"))

if __name__ == "__main__":
    test = String('hello dff', ["hello", "hola"])
    test2 = SortAlgos( ["hello", "hola","aio", "eeA","EeA"])
    recur = Recursion(["hello", "hola","aio", "eeA","EeA"])

    print("The sequence to be changed {} : ".format(test.get_seq()))
    print("The seq splited : \n{}".format(test.string_split()))
    print("The seq sorted : \n{}".format(test.string_sort()))

    print("----------sort-----------")
    print("sort by len ", test2.check_type())

    print("----------Recursion-----------")
    print("Factorial of {} is {} :".format(n, recur.factorial(n)))
    print("Fibonaci of {} is {} ".format(n, recur.fibonacci(n)))