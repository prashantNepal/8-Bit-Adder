#function for taking and checking the provided binary input
def input_binary():
    success = False
    while(not success):
        binary_number = input("Please Enter a Binary Number: ")

        #checking condition if it matches the condition provided by validation condition
        if (validation_binary(binary_number)[0]):
            print ("\nError-404 ",validation_binary(binary_number)[1]) #executing the possible errors
        else:
            success = True #terminating the loop
    
    #returning the error free input
    return binary_number
        
def validation_binary(input_binary_num):
    #checking if the no input is provided
    if (input_binary_num == ""):
        return[True,"Detected an Empty Field, Please! Enter a Number\n"]

    #for handling exception which can execute while converting input to integer
    try:
        check_number = int (input_binary_num)
    except:
        return [True,"Invalid Number or Charater Detected, Please! Enter a Valid Number\n"]
    
    #if number provided is negative
    if (check_number<0):
        return [True,"Invalid Input, Please! Enter Positive Number\n"]

    #if the number has other digits rather than '1' and '0' for binary input
    for i in input_binary_num:
        if (i != '0' and i != '1'):
            return[True,"Oops! Invalid Binary Number, Please! Enter Valid Binary Number\n"] 

    #if the input has more than eight bit
    if (len(input_binary_num)>8):
        return [True,"Oops! Invalid Binary Number, Please! Enter 8-Bit Binary Number\n"]

    return [False] #if the number do not meet above conditions

