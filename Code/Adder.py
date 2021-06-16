#importing Bitwise_Operation file for using its functions
from Bitwise_operation import *

#function for finding the sum of binary numbers
def adder_solution(a,b):
    carry = 0
    final_binary_sum = ["0","0","0","0","0","0","0","0"] #for storing sum bit-wise in this list

    ##Solution for the sum
    ##runnig loop to add sum of binary numbers to the list
    for i in range (len(final_binary_sum)-1,-1,-1):
        first_bit = int(a[i]) #getting first bit from first input
        second_bit = int(b[i]) #getting first bit from second input

        XOR_output = XOR_GATE(first_bit,second_bit) #passing values inside function from Bitwise_Operation file
        AND_output = NAND_GATE(XOR_output,carry)
        OR_output = OR_GATE(XOR_output,carry)
        final_sum_bit = AND_GATE(AND_output,OR_output)
        final_binary_sum[i] = str(final_sum_bit) #placing final bit in the list by converting to the string
    
    #Solution for the carry
        AND_a = AND_GATE(first_bit,second_bit)
        AND_b = AND_GATE(carry,XOR_output)
        NOR_output = NOR_GATE(AND_a,AND_b)
        carry = NOT_GATE(NOR_output) #passing the carry bit to carry for using it to find sum

    return "".join(final_binary_sum) #joining the list with the sum of given input bits
    



    