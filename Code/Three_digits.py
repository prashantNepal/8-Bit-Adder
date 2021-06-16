# for converting any decimal numbers in three digits format

def three_digits(x):
     to_reverse_string = str(x)[::-1]

     final_digit = ['0','0','0']
     a = 2
     for i in to_reverse_string:
          final_digit[a] = i
          a -= 1

     return ''.join(final_digit)     
