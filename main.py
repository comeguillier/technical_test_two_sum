"""
FUNCTION check_for_sum

Input :
the_array : python list with integer values
the_sum_value : integer 

Output : 
boolean : whether or not there exist two elements in the_array whose sum is exactly the_sum_value.

"""
def sum_array(the_array):
    # Creation of a new list with the sum of all the elements of the list
    A = []
    len_array = len(the_array)
    B = the_array
    sum = 0
    j = 0
    while j <= len_array -1:
        i = j + 1
        while i <= len_array - 1:
            sum = B[j] + B[i]
            A.append(sum)
            i = i + 1
        j = j + 1
    return A

def check_for_sum(the_array, the_sum_value):
    # Check if the element is in the list
    A = sum_array(the_array)
    for i in range(len(A)):
        if (A[i] == the_sum_value):
            return True
    return False
"""
MAIN

"""
def main():

    the_array = [0, -1, 2, -3, 1]
    the_sum = -2

    if check_for_sum(the_array, the_sum):
        print("Your algorithm returned the right answer. Good for you!")
    else:
        print("You got it wrong. Please try again.")


if __name__ == '__main__':
    main()
