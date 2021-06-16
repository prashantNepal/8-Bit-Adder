#function for taking and checking the provided decimal input
def input_decimal():
    success = False
    while(not success):
        decimal_number = input("Please Enter a Decimal Number: ")

        #checking condition if it matches the condition provided by validation condition
        if (validation_decimal(decimal_number)[0]):
            print ("\nError-404 ",validation_decimal(decimal_number)[1]) #executing the possible errors
        else:
            success = True #terminating the loop
            
    #returning the error free input
    return decimal_number
        
def validation_decimal(input_decimal_number):
    #checking if the no input is provided
    if (input_decimal_number == ""):
        return[True,"Detected an Empty Field, Please! Enter a Number\n"]

    #for handling exception which can execute while converting input to integer
    try:
        check_num = int (input_decimal_number)
    except:
        return [True,"Invalid Number or Charater Detected, Please! Enter a Valid Number\n"]

    #checking if the provided number is negative
    if (check_num<0):
        return [True,"Invalid Input, Please! Enter Positive Number\n"]

    #checking if the number is larger than 255
    if (check_num>255):
        return [True,"Input Exceeds the Highest Possible Value, Please! Enter Number Below 256\n"]

    return [False] #if the number do not meet above conditions
    

