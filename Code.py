##Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
##Type "copyright", "credits" or "license()" for more information.
#Lecture 1. Data 
##>>> 'abc'
##'abc'
##>>> 'ac bc too bar'
##'ac bc too bar'
##>>> 53
##53
##>>> '52'
##'52'
##>>> 52*7
##364
##>>> '52*7'
##'52*7'
##>>> print 'ab'
##SyntaxError: Missing parentheses in call to 'print'. Did you mean print('ab')?
##>>> Y
##Traceback (most recent call last):
##  File "<pyshell#7>", line 1, in <module>
##    Y
##NameError: name 'Y' is not defined
##>>> print {'ab'}
##SyntaxError: Missing parentheses in call to 'print'. Did you mean print({'ab'})?
##>>> 'ab'
##'ab'
##>>> print('ab')
##ab
##>>> print (3*3)
##9
##>>> print('3*3')
##3*3
##>>> print 52a
##SyntaxError: Missing parentheses in call to 'print'. Did you mean print(52a)?
##>>> 3/5
##0.6
##>>> 3**5
##243
##>>> 3.0/5
##0.6
##>>> myString = 'eric'
##>>> myString
##'eric'
##>>> myString+Grimson
##Traceback (most recent call last):
##  File "<pyshell#19>", line 1, in <module>
##    myString+Grimson
##NameError: name 'Grimson' is not defined
##>>> 
##>>> myString+'Grimson'
##'ericGrimson'
##>>> 3*4
##12
##>>> 3*'ab'
##'ababab'
##>>> 'a'+'bcd'
##'abcd'
##>>> 3+'ab'
##Traceback (most recent call last):
##  File "<pyshell#25>", line 1, in <module>
##    3+'ab'
##TypeError: unsupported operand type(s) for +: 'int' and 'str'
##>>> str(3)+'ab'
##'3ab'
##>>> 'a'<3
##Traceback (most recent call last):
##  File "<pyshell#27>", line 1, in <module>
##    'a'<3
##TypeError: '<' not supported between instances of 'str' and 'int'
##>>> 'a' < 3
##Traceback (most recent call last):
##  File "<pyshell#28>", line 1, in <module>
##    'a' < 3
##TypeError: '<' not supported between instances of 'str' and 'int'
##>>> 4<'3'
##Traceback (most recent call last):
##  File "<pyshell#29>", line 1, in <module>
##    4<'3'
##TypeError: '<' not supported between instances of 'int' and 'str'
##>>> '4'<'3'
##False
##>>> '3'<'4'
##True
##>>> 9/5
##1.8
##>>> 9%5
##4
##>>> 3+4*5
##23
##>>> (3+4)*5
##35
##>>> x=3 # Create variable x and assign value 3 to it
##>>> x
##3
#Lecture 2.
##>>> #Example of assignment statements: print, and input. But not working   
##>>> x=3 # Create variable x and assign value 3 to it
##>>> x=x*x # bind x to value 9
##>>> print x
##SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
##>>> print(x)
##9
##>>> n=raw_input('Enter a number: ')
##print n
### print n/n
### The previous example was to notice that keywords like print can't be used 
##
##Example of branching programs.
##Conditional Format 1
##x = 15
##if (x/2)*2 == x:
##    print ('Even')
##else: print ('Odd')
#Phyton makes Integer Division. I this version is necesary to use // to use only integer part 
##x = 15
##if (x//2)*2 == x: print ('Even')
##else: print ('Odd')
# Particular Format
##z = 'b'
####if 'x'<z:
####    print ('Hello')
####    print ('Mom')
##z = 'b'
##if 'x'<z:
##    print ('Hello')
##print ('Mom')

##x=15
##y=5
##z=11
##print (x,y,z)
###Is this right?
##if x<y:
##    if x<z:print ('x is least')
##    else: print ('z is leats')
##else: print ('y is least')     
#Iteractions-Loop
##y = 0
##x = 15
##itersLeft = x
##while(itersLeft>0):
##    y = y + x
##    itersLeft = itersLeft-1
##    print ('y =' ,y,',itersLeft=',itersLeft)
##print (y)
#Lecture 3.
#Find the square root of a perfect square
##x = 16
##ans = 0
##while ans*ans < x:
##  ans = ans +1
##print (ans)  
# Note: With -16 the answer is 0 wich is a non-reasonable answer.
##x = 15
##if (x/2)*2 == x:
##    print ('Even')
##else:
##    print ('Odd')
#
##x = 1515361
##ans = 0
##if x >= 0:
##    while ans*ans < x:
##        ans = ans + 1
##        print ('ans =', ans)
##    if ans*ans |x:
##        print (x, 'is not prefect square')
##    else:
##        print (ans)
##else: print (x, 'is a negative number')
# ind all the divisors of some integers
##x = 10
##i = 1
##while i<x:
##    if x%i == 0:
##        print ('divisor ',i)
##    i= i+1
# For Loop. the variable update automatically
##x = 10
##for i in range (1,x):
##    if x%i ==0:
##         print ('divisor ',i)
#Compound Data Structures. Tuple
##How to select specific elemnts 
##test = (1,2,3,4,5)
##test
##test[0]
##Return the last element of the tuple
##test[-1]
##Return the seconf last element of the tuple
##test[-2]
##Selection foo[0]
##Return the second, and third elements but not include the fourth 
##test[1:3]
##Return the beginning of a tuple
##test[:3]
##Skip two first elements and give all the reminder pieces
##test[2:]
#range(1,10) # is a list not a tuple 

##x = 1515361
##if x >= 0:
##    for ans in range(1,x):
##        if ans*ans == x:
##            print ('ans')
##            break
## Get things into collections. Exm: adding pieces in the divisor example to create a divisor which is a collection of things
##x = 100
##divisors = ()
##for i in range(1,x):
##    if x%i ==0:
##        divisors = divisors + (i,)
# Don't get output?
# Lists supports selection, concatenation and slicing
##Example of concatenation
##s1 = 'abcdefg'
##s1
##s2 = 'hijklmn'
##s2
##s1+s2
##Example of selections in a list
##The fist element
##s1[0]
##All the elemnts between index 2 and index 4 not including index 4
##s1[2:4]
##The first five
##s1[:5]
## Exmaple of type convertion character into integer, and addition of all the digits inside a number
##sumDigits = 0
##for c in str(1952):
##     sumDigits += int(c)
##print (sumDigits)

#Lecture 4. Decomposition and abstratciion Throught functions, introduction to recursion
#Exmaple of applying Abstraction to the exmaple of getting the square root of a perfect square
##x = 1515361
##ans = 0
##if x >= 0:
##    while ans*ans < x:
##        ans = ans + 1
##        print ('ans =', ans)
##    if ans*ans |x:
##        print (x, 'is not prefect square')
##    else:
##        print (ans)
##else: print (x, 'is a negative number')
# Now we are gonna use a function to do the same
def sqrt(x):
##    **Returns the square root of x, if x is a perfect square. Prints an error
##         message and returns NOne otherwise** . Note that program create a syntax error with this comment
##    ans = 0
##    if x >= 0:
##        while ans*ans < x: ans = ans + 1
##        if ans*ans !=x:
##            print (x, 'is not a prefect square')
##            return None
##        else: return ans
##    else:
##          print (x, 'is a negative number')
##          return None
#Bindings. The following code was invalid to run
##def f(x)
##   x = x +1 
##   return x
# test is bound to a special name None from the sqrt function. Note when I ask test it doesn't print anything but it has bound a special name         
##def sqrt(x):
##    ans = 0
##    if x >= 0:
##        while ans*ans < x: ans = ans + 1
##        if ans*ans !=x:
##            print (x, 'is not a prefect square')
##            return None
##        else: return ans
##    else:
##          print (x, 'is a negative number')
##          return None
##test=sqrt(16)
##test
##test=sqrt(34)
##test
##test == None
### Using ideas of decomposition and abstraction in the Farm animals problem. Given a number of heads and legs how many pigs and chickens does the farmer have?
# The following code is getting an error. Expected an indented block. Not sure what is happening. The professor indented the last return withnthe first for, the program is doing a different indentation but no run in any of these two ways.  
##def solve(numLegs, numHeads):
##    for numChicks in range(0, numHeads+1):
##        numPigs = numHeads - numChicks
##        totLegs = 4*numPigs + 2*numChicks
##        if totLegs == numLegs:
##            return (numPigs, numChicks)
##        return (None,None)    
#In this function we will use solve directle
# The following code is getting an error. Expected an indented block. Not sure what is happening. 
##def barnYard():
##    heads = int(raw_input('Enter number of heads'))
##    legs = int (raw_input ('Enterg number of legs'))
##    pigs, chickens = solve(legs, heads)
##    if pigs == None:
##        print 'There is no soltion'
##    else:
##        print 'Number of pigs:', pigs
##        print 'Number of chickens:', chickens
## barnYard()
## Now we'll add spiders to the problem
###The code is getting the same error. expected an indented block
##def solve1 (numLegs, numHeads):
##   for numSpiders in range (0, numHeads+1):
##        for numChicks in range (0, numHeads-numSpiders+1):
##            numPigs = numHeads-numChicks-numSpiders
##            totLegs = 4*numPigs+2*numChicks+numSpiders
##            if totLegs == numLegs:
##                return (numPigs,numChicks, numSpiders)
##   return (None, None, None)
##def barnYard1()
##heads = int(raw_input('Enter number of heads:'))
##legs = int(raw_input('Enter number of legs:'))
##pigs, chickens, spiders =solve1(legs, heads)
##if pigs == None:
##    print 'Number of pigs', pigs
##    print 'Number of chickens', chickens
##    print 'Number of spiders', spiders
# To generalize the loop
##def solve2(numLegs,numHeads):
##    solutionFound = False
##    for numSpiders in range (0, numHeads+1):
##        for numChick in range (0, numHeads-numSpiders+1):
##            numPigs = numHeads-numChicks-numSpiders
##            totLegs = 4*numPigs+2*numChicks+8*numSpiders
##            if totaLegs == numLegs:
##                print 'NUmber of pigs:'+str(numPigs)+','
##                print 'Number of chickens:'+str(numChicks)+','
##                print 'Number of Spiedrs', numSpiders
##                solutionFound = True
##    if not solutionFound: print 'There is no solution'
#Introduction to Recursion
# Palindrome example, Error indentation as before.
##def isPalindrome(s):
##    ***Return True if s is a palindrome and False otherwise***
##    if len(s)<=1: return True
##    else: return s(0)==s(-1) and isPalindrome(s(1:-1))
# The same code with identation. Also i am getting teh same error
##def isPalindrome1(s,indent):
##    ***Return True if s is a Palindrome and False otherwise***
##    print indent, isPalindrome1 called with ',s
##    if len(s)<=1:
##        print indent, 'About to return True from base case'
##        return True
##    else:
##        ans = s(0) == s(-1) and isPalindrome1 (s(1:-1), indent+indent)
##        print indent, 'About to return',ans
##        return ans
####To invoke this function
##isPalindrome1('abcdedcba','')
#Other exmaple of recursion. Fibonacci Numbers
##def fib(x):
##    ***Return fibonacci of x, where x is a non-negative ***
##    if x ==0 or x==1:return1
##    else: return fib(x-1)+fib(x-2)
#fib(12)

    



    
    
    
   

    
        
            













         
         
         

         


   
   
   
 




