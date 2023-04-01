
class UnitTestClass:

    def reverse_this(self, a): # we add parameter a
        # we check if input is a string or integer
        if isinstance(a, str):
            return a[::-1]  # we slice the string to reverse it
        elif isinstance(a, int):
            rev = 0
            while a > 0: # we make a>0 because dividing 0 by anything will result in 0
                rev = (rev * 10) + (a % 10)
                a //= 10 # we use floor division
            return rev
        else:
            return "Input must be a string or integer" # in case 'a' is not an integer or a string

    # this method squares every digit of a number and concatenates them
    def square_digits(self,num): # we add param num
        number = str(num) # we make num into a string called number
        digit = "" # we make an empty string called digit
        for i in range(len(number)): # we use a for loop to iterate through the len of the string 'number'
            digit = digit + str(int(number[i])**2) # we concatenate and we also square
        return int(digit) # return the 'digit' as a square

