#importing other files for using their functions
from ValidationDecimal import input_decimal
from ValidationBinary import input_binary
from Conversion import *
from Adder import adder_solution
from Three_digits import *

#function for running the whole program
def initialize():
    print('''
█── █ █▀▀ █── █▀█ █▀▀█ █▀▄▀█ █▀▀ █  ▀▀█▀▀ █▀▀█  █▀▀█    █▀▀█ ▀█▀ ▀▀█▀▀  ─█▀▀█ █▀▀▄ █▀▀▄ █▀▀ █▀▀█
█ █ █ █▀▀ █── █── █─ █ █ █ █ █▀▀ ▀   ─█── █─ █  ▄▀▀▄ ▀▀ █▀▀▄  █─ ─ █──   █▄▄█ █─ █ █─ █ █▀▀ █▄▄▀
█▄▀▄█ █▄▄ █▄▄ █▄█ █▄▄█ █── █ █▄▄ ▄   ─█── █▄▄█  █▄▄█    █▄▄█ ▄█▄ ─ █──   █─ █ █▄▄▀ █▄▄▀ █▄▄ █─ █
                        .------------------------------------------------.
                        |             Program Description!               |
                        |------------------------------------------------|
                        |   The main themes of this program are:         |
                        | ♦ To convert binary to decimal and vice versa. |
                        | ♦ To find the sum of given inputs in both:     |
                        |   binary and decimal.                          |
                        '------------------------------------------------'
    ''')
    process = False

    while (not process):
        store_bin = [] #for storing binary numbers provided by user
        store_dec = [] #for storing decimal numbers provided by user

        primary_input = input("Enter [b/B] for Binary OR [d/D] for Decimal calculaiton [b/d]: ")
        
        #if the user choose calculation by providing binary inputs
        if primary_input in ['b','B']:
            print ('''
.--------------------------------------------------.
| Consider following points for Binary calculation |
|--------------------------------------------------|
| ♠ Number should contain only '0' and '1'.        |
| ♠ Decimal, negative and number with alphabets or |
|   characters are taken as 'Invalid Input'.       |
| ♠ Input should not exceeds 8 digits for singal   |
|   input.                                         |
| ♠ Sum of numbers should be less than 256.        |
'--------------------------------------------------'
            ''')
            binary_process = False
            while (not binary_process):
                first_bin = input_binary() #calling function from ValidationBinary file
                print ("Now, For Second Input:")
                second_bin = input_binary()

                print ("\nLoading.... Please! Wait ♪ ♫ ")

                #checking if the sum of provided number is more than 255
                if (binary_to_decimal(first_bin) + binary_to_decimal(second_bin)>255):
                    print('''
.××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××.
| Sorry!, The sum of given inputs exceed the maximum limitation of 255 |
'××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××'
                    ''')
                    binary_process = False #for continuing the loop

                else:
                    
                    #storing the provided input in list
                    store_bin.append(first_bin)
                    store_bin.append(second_bin)

                    #converting binary to decimal by calling function from conversion file
                    dec_1 = binary_to_decimal(store_bin[0])
                    dec_2 = binary_to_decimal(store_bin[1])

                    #for converting given inputs to 8 bit
                    bin_1 = decimal_to_binary(dec_1)
                    bin_2 = decimal_to_binary(dec_2)

                    print ('''
.---------------------------------.
|        Decimal Conversion       |
|---------------------------------|
|  First input:  {} = {}   |
|  Second input: {} = {}   |
'---------------------------------'
                    '''.format(bin_1,three_digits(dec_1),bin_2,three_digits(dec_2))) #inserting values replacing curly braces

                    print ('''
.-------------------------------.
| Sum of provided inputs are:   |
|-------------------------------|
|    Binary     |    Decimal    |
|---------------|---------------|
|    {}   |      {}      |
|  + {}   |    + {}      |
|---------------|---------------|
|    {}   |      {}      |
'-------------------------------'
                '''.format(bin_1,three_digits(dec_1),bin_2,three_digits(dec_2),
                adder_solution(bin_1,bin_2),three_digits(dec_1 + dec_2))) #inserting values by calling function from Adder file 

                    print ('''
.-----------------------------------------.
| Therefore, the sum of given numbers is; |
|-----------------------------------------|
| In Binary  = {}                   |  
| In Decimal = {}                        |      
'-----------------------------------------'
                        '''.format(adder_solution(bin_1,bin_2),three_digits(dec_1 + dec_2)))
                    
                    binary_process = True #terminating the loop to take binary inputs

                    continue_process = False
                    while (not continue_process):
                        #for continuing the clculation or terminate the claculation
                        continue_calculation = input("Enter [Y/y] for calculation [N/n] for termination [y/n]: ")

                        if continue_calculation in ['Y','y']:
                            continue_process = True #terminating continuity process
                            process = False #for continuing to take binary inputs
                        elif continue_calculation in ['N','n']:
                            continue_process = True #terminating continuity process
                            print ("Thank You♥ For using the Program! See You Around☻")
                            process = True #terminating the whole program
                        else:
                            continue_process = False #continue the process to ask for continuity of program
        
        #if user choose calculation using decimal inputs
        elif primary_input in ['d','D']:
            print ('''
.---------------------------------------------------.
| Consider following points for Decimal calculation |
|---------------------------------------------------|
| ♣ Input should contain number with only 0 to 9    |
|   digits.                                         |
| ♣ Decimal, negative and number with alphabets or  |
|   characters are taken as 'Invalid Input'.        |
| ♣ Input should not exceeds 255 for singal input   |
| ♣ Sum of numbers should be less than 256.         |
'---------------------------------------------------'
            ''')
            decimal_process = False
            while (not decimal_process):
                first_dec = input_decimal() #calling function form ValidationDecimalFile
                print ("Now, For Second Input:")
                second_dec = input_decimal()

                print ("\nLoading.... Please! Wait ♪ ♫ ")

                #checking if sum of input is more than 255 by converting string to int
                if (int(first_dec) + int(second_dec) >255): 
                    print('''
.××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××.
| Sorry!, The sum of given inputs exceed the maximum limitation of 255 |
'××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××'
                    ''')
                    decimal_process = False #for repeating the loop
                
                else:
                    #for storing inputs from user in list
                    store_dec.append(first_dec)
                    store_dec.append(second_dec)

                    ## for converting given inputs (by changing them to integer) from
                    ## user to binary by calling function from Conversion file 
                    bin_1 = decimal_to_binary(int(store_dec[0]))
                    bin_2 = decimal_to_binary(int(store_dec[1]))

                    print ('''
.-------------------------------.
|       Binary Conversion       |
|-------------------------------|
|  First input:  {} = {} |
|  Second input: {} = {} |
'-------------------------------'
                    '''.format(three_digits(int(store_dec[0])),bin_1,three_digits(int(store_dec[1])),bin_2))

                    print ('''
.-------------------------------.
| Sum of provided inputs are:   |
|-------------------------------|
|    Binary     |    Decimal    |
|---------------|---------------|
|    {}   |      {}      |
|  + {}   |    + {}      |
|---------------|---------------|
|    {}   |      {}      |       
'-------------------------------'
                    '''.format(bin_1,three_digits(int(store_dec[0])),bin_2,three_digits(int(store_dec[1])),
                    adder_solution(bin_1,bin_2),three_digits(int(store_dec[0]) + int(store_dec[1])))) #inserting values replacing curly braces

                    print ('''
.-----------------------------------------.
| Therefore, the sum of given numbers is; |
|-----------------------------------------|
| In Binary  = {}                   |  
| In Decimal = {}                        |                        
'-----------------------------------------'
                    '''.format(adder_solution(bin_1,bin_2),three_digits(int(store_dec[0]) + int(store_dec[1]))))

                    decimal_process = True #terminating the process of calculation

                    continue_process = False
                    while (not continue_process):
                        continue_calculation = input("Enter [Y/y] for calculation [N/n] for termination [y/n]: ")

                        if continue_calculation in ['Y','y']:
                            continue_process = True #terminating continuity process
                            process = False #for continuing the calculation
                        elif continue_calculation in ['N','n']:
                            continue_process = True #terminating continuity process
                            print ("Thank You♥ For using the Program! See You Around☻")
                            process = True #terminating the calculation
                        else:
                            continue_process = False #for continuing the process for continuity

        #if user do not choose any given option
        else:
            print ('''
.×××××××××××××××××××××××××××××××××××××××××××.
| Error!-404, The provided input is Invalid |
'×××××××××××××××××××××××××××××××××××××××××××'       
            ''')
            process = False #restarting the whole process

#conditional statement for calling the initialize function
if __name__ == "__main__":
    initialize()
