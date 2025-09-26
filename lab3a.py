#!/usr/bin/env python3
# return_text_value() function
#Author ID: emolina3

def return_text_value():
   name = 'Terry'
   Greeting = 'Good Morning ' + name
   return Greeting



# return_number_value() function

def return_number_value(): 
    num1 = 10
    num2 = 5
    num3 = num1 + num2
    return num3
  

    
# Main Program

if __name__ == '__main__':
    print('python code')
    text = return_text_value()
    print(text)
    number = return_number_value()
    print(str(number))

import lab3a
text = lab3a.return_text_value()
print(text)
print(lab3a.return_text_value())

