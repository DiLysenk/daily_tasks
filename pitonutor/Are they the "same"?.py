# Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

def comp(array1, array2):
    if array1 == [] or array1 == None:
        result = array1 == array2
    elif array2 == [] or array2 == None:
        result = array1 == array2
    else:
        array1_x2 = [i * i for i in array1]
        array1_x2 = set(array1_x2)
        array2 = set(array2)

        result = array1_x2 == array2

    return result