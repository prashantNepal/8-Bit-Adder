#functions for converting given binary input to decimal and vice-versa
def binary_to_decimal(binary_number):
    decimal_no=0
    length = len(binary_number)-1

    #for loop to run process till the length of given binary number
    for i in binary_number:
        decimal_no += int(i)*2**(length) #calculating and adding to decimal_no
        length=length-1
    return (decimal_no) #returning the final sum of decimal_no

def decimal_to_binary(decimal_number):
    ##declaring list to insert add the remainders when input is devided by 2
    ##also for making the eight bit binary numebr
    binary_list = ['0','0','0','0','0','0','0','0']
    i = 7
    while (decimal_number>0):
        r = decimal_number%2
        binary_list[i]=str(r) #appending the remainder to the last position of list
        i = i-1
        decimal_number = int (decimal_number/2)

    #joining the given list and returning it
    return ("".join(binary_list))



