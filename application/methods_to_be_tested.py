
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
        if isinstance(num, int):
            number = str(num) # we make num into a string called number
            digit = "" # we make an empty string called digit
            for i in range(len(number)): # we use a for loop to iterate through the len of the string 'number'
                digit = digit + str(int(number[i])**2) # we concatenate and we also square
            return int(digit) # return the 'digit' as a square
        else:
            return "Input must be an integer"

    # the following method receives a number and returns the sum of all numbers from 0 to that number.
    def sum_num(self, b):
        sum = 0
        for i in range(0, b + 1):
            sum = sum + i
        return sum

    # Function that receives a list of digits and returns a DICT that tells us how many times each digit appears.
    def count_digits(self,lista):
        count = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0
        }
        for i in count.keys():
            for j in lista:
                if i == j:
                    count[i] = count[i] + 1
        return count
