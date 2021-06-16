#Operation using bitwise operators to calculate their result when passed to different gates

#for AND gate
def AND_GATE(a,b):
    return a & b 

#for OR gate
def OR_GATE(a,b):
    return a | b

#for NOT gate
def NOT_GATE(a):
    return ~(a)+2

#for XOR gate
def XOR_GATE(a,b):
    return a ^ b

#for NOR gate
def NOR_GATE(a,b):
    return NOT_GATE(OR_GATE(a,b))

#for NAND gate
def NAND_GATE(a,b):
    return NOT_GATE(AND_GATE(a,b))



    
    
    
