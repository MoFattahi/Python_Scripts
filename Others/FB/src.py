# Fizz Buzz Game

'''
Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

'''

def FizzBuzz():
    # Genrate numbers
    nums = list(range(1, 101))

    for k in nums: 
        if k % 3 == 0 and k % 5 == 0 : 
            print("Fizz Buzz")
        elif k % 3 == 0 :
            print("Fizz")
        elif k % 5 == 0 :
            print("Buzz")
        else :
            print(k)

if __name__ == "__main__" :
    FizzBuzz()
    





